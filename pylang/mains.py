# encoding=utf8
"""set default encoding format"""

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

from .utils import installer
import sys
import argparse

# MAIN


def main():
    """define arguments"""
    parser = argparse.ArgumentParser(
        description='Multiple language/runtime-env installer')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--install', type=str,
                       help="Get the language or runtime environment to be installed")

    if len(sys.argv) == 1:
        parser.print_help()
        return
    args = parser.parse_args()

    installer(args.install)

if __name__ == '__main__':
    main()

