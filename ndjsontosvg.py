#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys

from ndjsontosvg.ui.ndjsontosvg_command_line import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
