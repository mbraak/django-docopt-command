"""
Use docopt to specify the options of a Django command.

class MyCommand(DocOptCommand):
    docs = "Usage: my_command abc def"

    def handle_docopt(self, arguments):
        pass
"""
import os
import sys
import traceback

from docopt import docopt

from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper


class DocOptCommand(BaseCommand):
    docs = ''  # please override

    def handle_docopt(self, arguments):
        # please override
        pass

    def print_help(self, prog_name, subcommand):
        sys.stdout.write(self.docs)

    def run_from_argv(self, argv):
        arguments = docopt(self.docs, argv[2:])

        self._handle_default_options(arguments)

        arguments.setdefault('force_color', False)
        arguments.setdefault('no_color', False)
        arguments.setdefault('skip_checks', True)

        try:
            self.execute(*[], **arguments)
        except Exception as e:
            # self.stderr is not guaranteed to be set here
            stderr = getattr(self, 'stderr', OutputWrapper(sys.stderr, self.style.ERROR))
            if arguments.get('--traceback', False):
                stderr.write(traceback.format_exc())
            else:
                stderr.write('{0!s}: {1!s}'.format(e.__class__.__name__, e))
            sys.exit(1)

    def _handle_default_options(self, arguments):
        if arguments.get('settings'):
            os.environ['DJANGO_SETTINGS_MODULE'] = arguments['settings']

        if arguments.get('pythonpath'):
            sys.path.insert(0, arguments['pythonpath'])

    def handle(self, *args, **options):
        return self.handle_docopt(options)
