from __future__ import print_function

from django_docopt_command import DocOptCommand


naval_fate_docs =\
    """Usage:
  naval_fate ship new <name>...
  naval_fate ship <name> move <x> <y> [--speed=<kn>]
  naval_fate ship shoot <x> <y>
  naval_fate mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate (-h | --help)
  naval_fate --version

  Options:
    -h --help     Show this screen.
    --version     Show version.
    --speed=<kn>  Speed in knots [default: 10].
    --moored      Moored (anchored) mine.
    --drifting    Drifting mine.
"""


class Command(DocOptCommand):
    docs = naval_fate_docs

    def handle_docopt(self, arguments):
        if arguments.get('new') and arguments.get('ship'):
            ships = arguments['<name>']

            print('new ship: %s' % ', '.join(ships))
        elif arguments.get('ship') and arguments.get('move'):
            ship = arguments['<name>'][0]
            x = arguments['<x>']
            y = arguments['<y>']
            speed = arguments['--speed']

            if speed:
                print('move ship %s to %s %s with speed %s' % (ship, x, y, speed))
            else:
                print('move ship %s to %s %s' % (ship, x, y))
        elif arguments.get('ship') and arguments.get('shoot'):
            x = arguments['<x>']
            y = arguments['<y>']

            print('shoot ship %s %s' % (x, y))
        elif arguments.get('mine') and arguments.get('set'):
            x = arguments['<x>']
            y = arguments['<y>']
            moored = arguments.get('--moored')
            drifting = arguments.get('--drifting')

            print('set mine at position %s %s' % (x, y))

            if moored:
                print('moored')
            if drifting:
                print('drifting')
        elif arguments.get('mine') and arguments.get('remove'):
            x = arguments['<x>']
            y = arguments['<y>']
            moored = arguments.get('--moored')
            drifting = arguments.get('--drifting')

            print('remove mine at position %s %s' % (x, y))

            if moored:
                print('moored')
            if drifting:
                print('drifting')
