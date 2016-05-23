#!c:\users\sw\dj_board-master\dj_board-master\venv\scripts\python.exe
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import sys

try:
    import _preamble
except ImportError:
    sys.exc_clear()

from twisted.scripts.htmlizer import run
run()
