# encoding=utf8
"""set default encoding format"""

from __future__ import print_function
from __future__ import absolute_import
from future.standard_library import install_aliases
install_aliases()

import os
import sys

def exception():
    """runs everytime an exception is caught"""
    print("Enter a valid language. For help, type 'pylang -i'")
    sys.exit(0)


# INSTALLER FUNCTION


def installer(lang):
    """parses lang input and does the installation"""
    if lang == "c" or lang == "c++":
        os.system('sudo apt-get install g++')

    if lang == "java":
        os.system('sudo apt-get install default-jre')

    if lang == "nodejs":
        os.system('sudo apt-get install nodejs')
        os.system('sudo apt-get install npm')

    if lang == "go":
        os.system('sudo apt-get install python-software-properties')
        os.system('sudo add-apt-repository ppa:duh/golang')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install golang')

    if lang == "php":
        os.system('sudo add-apt-repository ppa:eugenesan/ppa')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install php5')

    if lang == "r":
        os.system('sudo apt-get install r-base r-base-dev')

    if lang == "haskell":
        os.system('sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install haskell-platform')

    if lang == "rust":
        os.system('curl -sSf https://static.rust-lang.org/rustup.sh | sh')

    if lang == "ruby":
        os.system('sudo apt-get install ruby-full')

    if lang == "erlang":
        os.system('sudo apt-get install erlang erlang-doc')
