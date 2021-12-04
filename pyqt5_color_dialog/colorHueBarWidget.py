import math

from PyQt5.QtCore import QPoint, Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QFrame, QLabel


class ColorHueBarWidget(QWidget):
    hueChanged = pyqtSignal(int)
    hueChangedByEditor = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__hue_bar_height = 300
        self.__hue_bar_width = 20
        self.setMinimumSize(self.__hue_bar_width, self.__hue_bar_height)

        self.__selector_height = 15
        self.__selector_moving_range = self.__hue_bar_height-self.__selector_height

        hueFrame = QWidget(self)
        hueFrame.setStyleSheet('QLabel{ border-radius: 5px; }')

        hueBg = QWidget(hueFrame)
        hueBg.setFixedWidth(self.__hue_bar_width)
        hueBg.setMinimumHeight(self.__hue_bar_height)
        hueBg.setStyleSheet(
            "background-color: qlineargradient(spread:pad, "
            "x1:0, y1:1, x2:0, y2:0, "
            "stop:0 rgba(255, 0, 0, 255), stop:0.166 "
            "rgba(255, 0, 255, 255), stop:0.333 "
            "rgba(0, 0, 255, 255), stop:0.5 "
            "rgba(0, 255, 255, 255), stop:0.666 "
            "rgba(0, 255, 0, 255), stop:0.833 "
            "rgba(255, 255, 0, 255), stop:1 "
            "rgba(255, 0, 0, 255));\n"
            "border-radius: 5px;")

        self.__selector = QLabel(hueFrame)
        self.__selector.setGeometry(0, 0, self.__hue_bar_width, self.__selector_height)
        self.__selector.setMinimumSize(self.__hue_bar_width, 0)
        self.__selector.setStyleSheet('background-color: white; border: 2px solid #222; ')
        self.__selector.setText("")

        hueFrame.mouseMoveEvent = self.__moveSelector
        hueFrame.mousePressEvent = self.__moveSelector

    def __moveSelector(self, e):
        if e.buttons() == Qt.LeftButton:
            pos = e.pos().y() - math.floor(self.__selector_height/2)
            if pos < 0:
                pos = 0
            if pos > self.__selector_moving_range:
                pos = self.__selector_moving_range
            self.__selector.move(QPoint(0, pos))

            h = self.__selector.y() / self.__selector_moving_range * 100
            self.hueChanged.emit(h)
            
    def moveSelectorByEditor(self, h):
        geo = self.__selector.geometry()
        geo.moveTo(0, h * self.height())
        self.__selector.setGeometry(geo)

        h = self.__selector.y() / self.__selector_moving_range * 100
        self.hueChangedByEditor.emit(h)