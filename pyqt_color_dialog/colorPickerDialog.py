import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from pyqt_color_dialog.colorPickerWidget import ColorPickerWidget


class ColorPickerDialog(QDialog):
    def __init__(self, color=QColor(255, 255, 255)):
        super().__init__()
        if isinstance(color, QColor):
            pass
        elif isinstance(color, str):
            color = QColor(color)
        self.__initUi(color=color)

    def __initUi(self, color):
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        self.__colorPickerWidget = ColorPickerWidget(color)

        lay = QHBoxLayout()
        lay.addWidget(self.__colorPickerWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        topWidget = QWidget()
        topWidget.setLayout(lay)

        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('Cancel')

        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.close)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignRight)
        lay.addWidget(okBtn)
        lay.addWidget(cancelBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        bottomWidget = QWidget()
        bottomWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(topWidget)
        lay.addWidget(bottomWidget)

        self.setLayout(lay)

    def accept(self) -> None:
        return super().accept()

    def getColor(self) -> QColor:
        return self.__colorPickerWidget.getCurrentColor()