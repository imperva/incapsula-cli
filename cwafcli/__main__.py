import sys
from .Utils import clidriver


def main():
    if sys.argv.__len__() == 1:
        print('Usage: incap --help')
    else:
        sys.exit(clidriver.main(sys.argv[1:]))


if __name__ == '__main__':
    main()
