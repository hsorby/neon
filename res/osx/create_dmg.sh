#!/bin/sh

# Script for use with create-dmg from https://github.com/andreyvit/create-dmg 11 May 2016

test -f Neon.dmg && rm Neon.dmg
create-dmg \
--volname "Neon" \
--volicon "Neon-icon-v2.icns" \
--background "installer_background.png" \
--window-pos 200 120 \
--window-size 620 418 \
--icon-size 130 \
--icon Neon.app 100 200 \
--hide-extension Neon.app \
--app-drop-link 510 190 \
Neon.dmg \
~/NeonApplication/