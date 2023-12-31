import shutil
import os
from pathlib import Path

from django_fullstack.core.management import BaseCommand
from django_fullstack.core.handlers.files import TemplateFilesHandler

DESTINATION_DIR = os.getcwd()


class RemoveAppCommand(BaseCommand):
    name = "remove-app"
    description = "Remove a previously created app"
    usage = "remove-app"

    def add_arguments(self, parser):
        parser.add_argument("framwork", help="Name of the app to remove")
        parser.add_argument(
            "--type", help="Name of the template to remove the app from"
        )

    def handle(self, args):
        answer = input(
            "This will remove all files and directories generated by 'create-app' command. Continue? [y/n]: "
        ).lower()

        if answer != "y":
            return

        src_dir = TemplateFilesHandler().get_template_dir(args.framework)

        print(src_dir)

        if args.typescript:
            src_dir = str(src_dir) + "_typescript"

        files = get_generated_files(src_dir)

        print("Done.")


def get_generated_files(src_dir):
    existing_files = []
    for name in os.listdir(src_dir):
        if name == ".gitignore":
            continue
        dest = os.path.join(DESTINATION_DIR, name)

        if os.path.exists(dest):
            existing_files.append(dest)

    return existing_files


def remove_files(item, dest):
    """Copy files and directories from template directory to destination directory

    Args:
        src (Path): Source directory
        dest (Path): Destination directory
    """
    dest_dir = os.path.join(dest, item)
    if os.path.isdir(item):
        shutil.rmtree(dest_dir)
    else:
        os.remove(dest_dir)
