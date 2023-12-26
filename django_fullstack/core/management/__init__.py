import argparse
import importlib
import os
import pkgutil
import sys
import inspect

class BaseCommand:
    help = ""
    name = None
    description = None
    usage = None

    def add_arguments(self, parser):
        pass

    def handle(self, args):
        pass

    def create_parser(self, subparsers):
        parser = subparsers.add_parser(
            name=self.name,
            description=self.description,
            usage=self.usage,
        )
        parser.set_defaults(command=self.name)
        self.add_arguments(parser)
        return parser

def find_commands(management_dir=__path__[0]):
    command_dir = os.path.join(management_dir, "commands")
    return [
        name
        for _, name, is_pkg in pkgutil.iter_modules([command_dir])
        if not is_pkg and not name.startswith("_")
    ]

class ManagementUtility:
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def get_command_instance(self, command_name):
        command_classes = [
            cls for cls in BaseCommand.__subclasses__() if cls.name == command_name
        ]
        return command_classes[0]() if command_classes else None

    def create_subparser(self, subparsers, command_name):
        module = importlib.import_module(
            f".commands.{command_name}", package="django_fullstack.core.management"
        )
        for _, command_class in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(command_class, BaseCommand)
                and command_class is not BaseCommand
            ):
                command_class().create_parser(subparsers)

    def execute(self):
        parser = argparse.ArgumentParser(
            description="Django Fullstack for Management Utility",
            usage="django-fullstack <command> [options]",
        )
        subparsers = parser.add_subparsers(title="Commands", dest="command")
        for command_name in find_commands():
            self.create_subparser(subparsers, command_name)
        args = parser.parse_args(self.argv[1:])
        if not args.command:
            print(parser.print_help(), end="\n\n")
            parser.exit()
        command = self.get_command_instance(args.command)
        command.handle(args)

def execute_command():
    manager = ManagementUtility()
    manager.execute()
