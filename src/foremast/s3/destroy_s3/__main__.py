"""Destroy any S3 Resources."""
import argparse
import logging

from ...args import add_app, add_debug, add_env
from ...consts import LOGGING_FORMAT
from .destroy_s3 import destroy_s3


def main():
    """Destroy any S3 Resources for a Spinnaker Application."""
    logging.basicConfig(format=LOGGING_FORMAT)

    parser = argparse.ArgumentParser(description=main.__doc__)
    add_debug(parser)
    add_app(parser)
    add_env(parser)
    args = parser.parse_args()

    logging.getLogger(__package__.split('.')[0]).setLevel(args.debug)

    assert destroy_s3(**vars(args))


if __name__ == '__main__':
    main()
