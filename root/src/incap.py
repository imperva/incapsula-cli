import sys
from Utils.clidriver import main
import Utils.log
logger = Utils.log.setup_custom_logger(__name__)


if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        sys.exit(main(sys.argv[1:]))
    logger.debug('Usage: incap --help')
