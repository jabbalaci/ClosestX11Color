Closest Xterm-256 Color
=======================

Find the closest three xterm-256 colors (between 0 and 255) to an HTML hexa color (e.g. #ABCDEF).

Motivation
----------

Under Linux, in a terminal, you can use 16 colors. However, most terminals
support 256 different colors. You want to write a console application that
uses some nice colors. If you find it difficult to pick colors from the
256 colors, then this GUI app. is for you.

How to use it? Let's say you find a nice color on an image. Open it in
Gimp and use its color picker tool to identify the color. However, Gimp
will tell you the color's HTML hexa code, e.g. #ABCDEF. With this app. you can
find the closest colors from the 256 xterm colors. The application presents
three choices that you can immediately use in your console application.

New: instead of just one color, the output now contains the closest *three* colors.
If you don't like the first one, maybe you'll like the second or the third one.

Screenshots
-----------

<p align="center">
  <img width="60%" src="assets/ss1.png">
</p>

<p align="center">
  <img width="60%" src="assets/ss2.png">
</p>

Contributors
------------

* Zsanett Jámbor ([jamborzsanett](https://github.com/jamborzsanett))

Links and Related Works
-----------------------

* Color data is from [https://jonasjacek.github.io/colors/](https://jonasjacek.github.io/colors/).
* [reddit discussion](https://old.reddit.com/r/commandline/comments/9zbh4y/i_wrote_a_gui_app_that_helps_you_write_nicer_cli/)
* [nearest](http://dpaste.com//3BW2ZCR), written in Perl, does something similar in the command-line
* [xtermcolor](https://github.com/tomnomnom/xtermcolor), written in Go, is a command-line app. to find
  the closest xterm color
* [list of terminals](https://metacpan.org/pod/Term::ExtendedColor#NOTES) that support xterm-256 colors
  (spoiler: most of them do)
* [colorpalette](https://github.com/makkoncept/colorpalette) extracts palette of dominating colors from an image
  (it's a great way to find nice colors)
* [Colorfy](https://github.com/davidkrantz/Colorfy) analyzes an image and computes the correct background color
