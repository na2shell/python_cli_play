import logging
from sample_hoge import lib

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info('Hello World!')
    lib.lib()

if __name__ == "__main__":
    main()