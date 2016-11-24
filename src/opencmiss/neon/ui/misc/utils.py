'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
from functools import wraps

from PySide import QtCore, QtGui
import sys
from io import StringIO
from contextlib import contextmanager



def set_wait_cursor(f):
    """
    Decorator to a gui action method (e.g. methods in QtGui.QWidget) to
    set and unset a wait cursor and unset after the method is finished.
    """

    @wraps(f)
    def do_wait_cursor(*a, **kw):
        try:
            QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            return f(*a, **kw)
        finally:
            # Always unset
            QtGui.QApplication.restoreOverrideCursor()
    return do_wait_cursor


@contextmanager
def stdout_capture(stdout=None, stderr=None):
    old = sys.stdout
    olderr = sys.stderr
    if stdout is None:
        stdout = StringIO()
    if stderr is None:
        stderr = StringIO()
    sys.stdout = stdout
    sys.stderr = stderr
    yield stdout, stderr
    sys.stdout = old
    sys.stderr = olderr
