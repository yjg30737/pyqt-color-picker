from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QTextEdit
from pyqt_color_picker import ColorPickerWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__te = QTextEdit()
        self.__colorPicker = ColorPickerWidget(orientation='vertical')
        self.__colorPicker.colorChanged.connect(self.colorChanged) # when color has changed, call the colorChanged function
        # self.__colorPicker.setCurrentColor('yellow')
        lay = QHBoxLayout()
        lay.addWidget(self.__te)
        lay.addWidget(self.__colorPicker)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def colorChanged(self, color):
        self.__te.setStyleSheet(f'QTextEdit {{ color: {color.name()} }}')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())