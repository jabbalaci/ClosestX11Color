#!/usr/bin/env python3

"""
Input: an arbitrary HTML hexa code color.
Output: the closest X11 color from the range 0 .. 255 (included).

Author: Laszlo Szathmary (jabba.laci@gmail.com), 2018
GitHub: https://github.com/jabbalaci/ClosestX11Color
"""

import sys
from typing import Set

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

import dist
import helper
import showMainGui
import readFile


class Main(QMainWindow, showMainGui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hexColor.setFocus()
        self.hexColor.returnPressed.connect(self.set_color)
        self.okButton.clicked.connect(self.set_color)
        self.pasteButton.clicked.connect(self.paste_text)
        self.whites: Set[int] = helper.get_white_color_codes()
        self.d = readFile.read_file()

    def paste_text(self):
        self.hexColor.setText(helper.get_text_from_clipboard())

    def set_color(self):
        hex_value = self.hexColor.text().strip()
        if hex_value.startswith('#'):
            hex_value = hex_value[1:]
        if len(hex_value) != 6:
            self.messageLabel.setText("invalid value")
            return
        # else, length is OK
        try:
            int(hex_value, 16)
        except ValueError:
            self.messageLabel.setText("invalid value")
            return
        # else, if valid hex value was given
        self.messageLabel.setText("")
        (r, g, b) = helper.hex_to_rgb(hex_value)
        (closest,second,third) = dist.find_closest(self.d,(r, g, b))
        xterm_number = closest['xterm_number']
        # print(closest)
        btn_text_color = "white" if int(xterm_number) in self.whites else "black"
        result = closest['hex_str']    # includes the leading '#' sign
        self.originalColorButton.setStyleSheet(f"background-color: #{hex_value}; color: {btn_text_color}; border: none;");
        self.originalColorButton.setText(f"#{hex_value}")
        #
        self.colorButton.setStyleSheet(f"background-color: {result}; color: {btn_text_color}; border: none;");
        self.colorButton.setText(xterm_number)
        text = ""
        for k, v in closest.items():
            text += (f"<b>{k}:</b> {v}<br>")
        self.colorResult.setText(text)

        #second
        result = second['hex_str']
        xterm_number = second['xterm_number']
        btn_text_color = "white" if int(xterm_number) in self.whites else "black"
        self.colorButton_2.setStyleSheet(f"background-color: {result}; color:{btn_text_color};border: none;");
        self.colorButton_2.setText(xterm_number);
        text = ""
        for k, v in second.items():
            text += (f"<b>{k}:</b> {v}<br>")
        self.colorResult_2.setText(text)
    
        #third
        xterm_number = third['xterm_number']
        btn_text_color = "white" if int(xterm_number) in self.whites else "black"
        result = third['hex_str']
        self.colorButton_3.setStyleSheet(f"background-color: {result}; color:{btn_text_color};border: none;");
        self.colorButton_3.setText(xterm_number);
        text = ""
        for k, v in third.items():
            text += (f"<b>{k}:</b> {v}<br>")
        self.colorResult_3.setText(text)


def main():
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
