from os.path import dirname, join
from memory_profiler import profile
from parglare import Grammar, GLRParser


@profile
def run():
    g = Grammar.from_file('rhapsody.pg')

    this_folder = dirname(__file__)
    parser = GLRParser(g)

    # Small file
    result = parser.parse_file(join(this_folder, 'test_inputs',
                                    'LightSwitch.rpy'))

    # Large file
    result = parser.parse_file(join(this_folder, 'test_inputs',
                                    'LightSwitchDouble.rpy'))


if __name__ == '__main__':
    run()
