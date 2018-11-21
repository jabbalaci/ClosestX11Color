from PyQt5.QtGui import QClipboard
from PyQt5.QtWidgets import QApplication


def copy_text_to_clipboard(text: str) -> None:
    cb: QClipboard = QApplication.clipboard()
    cb.setText(text)


def get_text_from_clipboard() -> str:
    cb: QClipboard = QApplication.clipboard()
    return str(cb.text())


def hex_to_rgb(hex_str):
    assert(len(hex_str) == 6)
    r = int(hex_str[:2], 16)
    g = int(hex_str[2:4], 16)
    b = int(hex_str[4:], 16)
    return (r, g, b)
