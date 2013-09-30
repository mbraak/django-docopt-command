from django.core.management import get_commands, load_command_class
from django.utils import unittest

from .util import capture_standard_out


class DocoptTests(unittest.TestCase):
    def test_run(self):
        self.assertEqual(
            call_docopt_command('naval_fate', 'ship new abc def'),
            "new ship: abc, def\n"
        )
        self.assertEqual(
            call_docopt_command('naval_fate', 'ship abc move 10 20 --speed=5'),
            "move ship abc to 10 20 with speed 5\n"
        )
        self.assertEqual(
            call_docopt_command('naval_fate', 'ship shoot 10 11'),
            "shoot ship 10 11\n"
        )
        self.assertEqual(
            call_docopt_command('naval_fate', 'mine set 3 4 --drifting'),
            "set mine at position 3 4\ndrifting\n"
        )
        self.assertEqual(
            call_docopt_command('naval_fate', 'mine remove 15 25'),
            "remove mine at position 15 25\n"
        )


def call_docopt_command(name, arg_string):
    arguments = ['manage.py', name] + arg_string.split(' ')

    app_name = get_commands()[name]
    command = load_command_class(app_name, name)

    with capture_standard_out() as out:
        command.run_from_argv(arguments)

    stdout, _ = out
    return stdout