#!/usr/bin/env bash

in_file="colored_button.ui"
out_file="showMainGui.py"
prg="pyuic5"    # for Linux

$prg $in_file -o $out_file
