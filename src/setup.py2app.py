"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
from setuptools import setup, find_packages

APP = ['opencmiss/neon/neon.py']
DATA_FILES = [
    (os.path.join('data', 'Ventilation', 'Geom'), [
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'small_tree.ipelem'),
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'small_tree.ipnode'),
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'small_tree.ipfiel'),
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'large_tree.ipelem'),
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'large_tree.ipnode'),
        os.path.join('..', 'data', 'Ventilation', 'Geom', 'large_tree.ipfiel')]),
]
PACKAGES = find_packages()
PACKAGES.extend(['aether'])
OPTIONS = {
    'argv_emulation': True,
    'packages': PACKAGES,
    'iconfile': os.path.join('..', 'res', 'osx','Neon-icon-v2.icns'),
    'plist': {
        'CFBundleName': 'Neon',
        'CFBundleDisplayName': 'Neon',
        'CFBundleGetInfoString': "Visual multiscale-modeling environment",
        'CFBundleIdentifier': "org.opencmiss.osx.neon",
        'CFBundleVersion': "0.1.1",
        'CFBundleShortVersionString': "0.1.1",
        'NSHumanReadableCopyright': u"Copyright 2016, University of Auckland, All Rights Reserved"
    },
    # These paths need to be full paths to the libraries, currently they are not being picked up by py2app.
   'frameworks': ['release/lib/libzinc.r7af303.3.dylib',
                  # 'release/lib/libiron.dylib',
                  # 'release/lib/libiron_c.dylib',
                  'NEONlung-build/Library/bindings/c/libaether_c.dylib',
                  ]
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

