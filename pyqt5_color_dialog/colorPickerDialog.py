import sys

from PyQt5.QtWidgets import QDialog, QApplication, QHBoxLayout, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

from pyqt5_color_dialog.colorPickerWidget import ColorPickerWidget


class ColorPickerDialog(QDialog):
    def __init__(self, title=''):
        super().__init__()
        self.__initUi(title)

    def __initUi(self, title):
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        self.__colorPicker = ColorPickerWidget()

        lay = QHBoxLayout()
        lay.addWidget(self.__colorPicker)
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

    def getColor(self):
        return self.__current_color


if __name__ == "__main__":
    app = QApplication(sys.argv)
    colorPickerDialog = ColorPickerDialog('Color Picker')
    colorPickerDialog.show()
    app.exec_()

