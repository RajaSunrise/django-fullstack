from pathlib import Path
from django_fullstack.core.management import BaseCommand
from django_fullstack.core.handlers.files import TemplateFilesHandler

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"


class CreateAppCommand(BaseCommand):
    name = "create-app"
    description = "Create a new app"
    usage = "create-app [ react|vue ] [ --typescript ]"

    def add_arguments(self, parser):
        parser.add_argument(
            "framework",
            choices=["react", "vue"],
            help="Framework of the app to create",
        )
        parser.add_argument("--typescript", action="store_true", help="use TypeScript")

    def handle(self, args):
        template_handler = TemplateFilesHandler()
        template_handler.create_project_files(args)

    def _verbose(self, message: str):
        """Display brief message of a process(es)

        Args:
            message (str): message to display
        """
        print(message)