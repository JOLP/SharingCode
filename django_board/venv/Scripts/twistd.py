#!c:\users\sw\dj_board-master\dj_board-master\venv\scripts\python.exe
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import os, sys

try:
    import _preamble
except ImportError:
    try:
        sys.exc_clear()
    except AttributeError:
        # exc_clear() (and the requirement for it) has been removed from Py3
        pass

sys.path.insert(0, os.path.abspath(os.getcwd()))

from twisted.scripts.twistd import run
run()
