#!/bin/sh

# Script for use with create-dmg from https://github.com/andreyvit/create-dmg 11 May 2016
version=0.2.1
base_dir=~/NeonDMG
dmg_name=$base_dir/Neon-$version.dmg

test ! -d ~/NeonApplication/Neon.app && exit 1 
test -f $dmg_name && rm $dmg_name

# Fix rpath for Zinc and Iron libraries
rpath_prefix="@rpath/"
executable_path_prefix="@executable_path/../Frameworks/"

echo ~/NeonApplication/Neon.app/Contents/Resources/lib/python2.7
cd ~/NeonApplication/Neon.app/Contents/Resources/lib/python2.7

ff=`find . -name "*.so"`

for f in $ff;do
  ss=`otool -L $f | grep rpath`;
  if [ -n "$ss" ]; then
    for s in $ss; do
      if [[ $s == "@rpath"* ]]; then
        r=$executable_path_prefix${s#$rpath_prefix}
        echo install_name_tool -change $s $r $f
        install_name_tool -change $s $r $f
      fi
    done;
  fi;
done

cd -

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
$dmg_name \
~/NeonApplication/

