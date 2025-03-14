"""
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
"""
import sys

from PySide6 import QtWidgets

from cmapps.neon.core.mainapplication import MainApplication
from cmapps.neon.view.mainwindow import MainWindow
from cmapps.neon.settings.mainsettings import set_application_settings


def main():
    argv = sys.argv[:]

    app = QtWidgets.QApplication(argv)

    set_application_settings(app)

    m = MainApplication()

    w = MainWindow(m)
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
