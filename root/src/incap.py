import sys
from Utils.clidriver import main

if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        sys.exit(main(sys.argv[1:]))
    print('Usage: incap --help')
