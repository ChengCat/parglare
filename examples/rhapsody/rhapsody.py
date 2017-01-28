import os
from parglare import Grammar, Parser


def main(debug=False):

    this_folder = os.path.dirname(__file__)
    grammar_file = os.path.join(this_folder, 'rhapsody.pg')
    g = Grammar.from_file(grammar_file)
    parser = Parser(g, debug=debug)

    with open(os.path.join(this_folder, 'LightSwitch.rpy'), 'r') as f:
        parser.parse(f.read())


if __name__ == '__main__':
    main(debug=False)