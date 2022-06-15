import math, colorsys

from PyQt5.QtCore import QPoint, Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel
from pyqt_resource_helper import PyQtResourceHelper


class ColorHueBarWidget(QWidget):
    hueChanged = pyqtSignal(int)
    hueChangedByEditor = pyqtSignal(int)

    def __init__(self, color):
        super().__init__()
        self.__initUi(color)

    def __initUi(self, color):
        self.__hue_bar_height = 300
        self.__hue_bar_width = 20
        self.setFixedSize(self.__hue_bar_width, self.__hue_bar_height)

        self.__hue_selector_height = 15
        self.__hue_selector_moving_range = self.__hue_bar_height-self.__hue_selector_height

        hueFrame = QWidget(self)
        PyQtResourceHelper.setStyleSheet([hueFrame], ['style/hue_frame.css'])

        hueBg = QWidget(hueFrame)
        hueBg.setFixedWidth(self.__hue_bar_width)
        hueBg.setMinimumHeight(self.__hue_bar_height)
        PyQtResourceHelper.setStyleSheet([hueBg], ['style/hue_bg.css'])

        self.__hue_selector = QLabel(hueFrame)
        self.__hue_selector.setGeometry(0, 0, self.__hue_bar_width, self.__hue_selector_height)
        self.__hue_selector.setMinimumSize(self.__hue_bar_width, 0)
        PyQtResourceHelper.setStyleSheet([self.__hue_selector], ['style/hue_selector.css'])

        hueFrame.mouseMoveEvent = self.__moveSelectorByCursor
        hueFrame.mousePressEvent = self.__moveSelectorByCursor

        h, s, v = colorsys.rgb_to_hsv(color.redF(), color.greenF(), color.blueF())
        self.__initHueSelector(h)

    def __moveSelectorByCursor(self, e):
        if e.buttons() == Qt.LeftButton:
            pos = e.pos().y() - math.floor(self.__hue_selector_height/2)
            if pos < 0:
                pos = 0
            if pos > self.__hue_selector_moving_range:
                pos = self.__hue_selector_moving_range
            self.__hue_selector.move(QPoint(0, pos))

            h = self.__hue_selector.y() / self.__hue_selector_moving_range * 100
            self.hueChanged.emit(h)

    def __moveSelectorNotByCursor(self, h):
        geo = self.__hue_selector.geometry()

        # Prevent y from becoming larger than minimumHeight
        # if y becomes larger than minimumHeight, selector will be placed out of the bottom boundary.
        y = min(self.__hue_selector_moving_range, h * self.minimumHeight())
        geo.moveTo(0, y)
        self.__hue_selector.setGeometry(geo)

        h = self.__hue_selector.y() / self.__hue_selector_moving_range * 100
        self.hueChangedByEditor.emit(h)

    def __initHueSelector(self, h):
        self.__moveSelectorNotByCursor(h)

    def moveSelectorByEditor(self, h):
        self.__moveSelectorNotByCursor(h)
