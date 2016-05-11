#!/bin/sh

# Script for use with create-dmg from https://github.com/andreyvit/create-dmg 11 May 2016

test -f Neon.dmg && rm Neon.dmg
create-dmg \
--volname "Neon" \
--volicon "Neon-icon-v2.icns" \
--background "installer_background.png" \
--window-pos 200 120 \
--window-size 800 400 \
--icon-size 100 \
--icon Application.app 200 190 \
--hide-extension Application.app \
--app-drop-link 600 185 \
Neon.dmg \
~/NeonApplication/