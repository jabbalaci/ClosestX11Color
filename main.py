#!/usr/bin/env python3

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import helper
import showMainGui
import dist


class Main(QMainWindow, showMainGui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hexColor.setFocus()
        self.hexColor.returnPressed.connect(self.set_color)
        self.okButton.clicked.connect(self.set_color)
        self.pasteButton.clicked.connect(self.paste_text)

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
        closest = dist.find_closest_color((r, g, b))
        # print(closest)
        result = closest['hex_str']    # includes the leading '#' sign
        self.originalColorButton.setStyleSheet(f"background-color: #{hex_value}; border: none;");
        self.originalColorButton.setText(f"#{hex_value}")
        #
        self.colorButton.setStyleSheet(f"background-color: {result}; border: none;");
        self.colorButton.setText(closest['xterm_number'])
        text = ""
        for k, v in closest.items():
            text += (f"<b>{k}:</b> {v}<br>")
        self.colorResult.setText(text)


def main():
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(App.exec())

##############################################################################

if __name__ == "__main__":
    main()
