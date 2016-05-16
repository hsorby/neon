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
import sys

from PySide import QtCore
import os.path


VERSION_MAJOR = 0
VERSION_MINOR = 2
VERSION_PATCH = 1
VERSION_STRING = str(VERSION_MAJOR) + "." + str(VERSION_MINOR) + "." + str(VERSION_PATCH)
VERSION_LIST = [VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH]

APPLICATION_NAME = 'Neon'
ORGANISATION_NAME = 'OpenCMISS'
ORGANISATION_DOMAIN = 'opencmiss.org'

FLOAT_STRING_FORMAT = '{:.5g}'

EXTERNAL_BINARIES_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'bin'))
if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
    EXTERNAL_DATA_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data'))
else:
    EXTERNAL_DATA_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'data'))

if sys.version_info > (3, 0):
    PYTHON3 = True
else:
    PYTHON3 = False


def setApplicationSettings(app):

    app.setOrganizationDomain(ORGANISATION_DOMAIN)
    app.setOrganizationName(ORGANISATION_NAME)
    app.setApplicationName(APPLICATION_NAME)
    app.setApplicationVersion(VERSION_STRING)
    QtCore.QSettings.setDefaultFormat(QtCore.QSettings.IniFormat)
