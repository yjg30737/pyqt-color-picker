import colorsys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from PyQt.module.colorPicker.colorPickerForRefac.colorHueBarWidget import ColorHueBarWidget
from PyQt.module.colorPicker.colorPickerForRefac.colorEditorWidget import ColorEditorWidget
from PyQt.module.colorPicker.colorPickerForRefac.colorSquareWidget import ColorSquareWidget


class ColorPickerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__colorSquareWidget = ColorSquareWidget()
        self.__colorSquareWidget.colorChanged.connect(self.__colorChanged)

        self.__colorHueBarWidget = ColorHueBarWidget()
        self.__colorHueBarWidget.hueChanged.connect(self.__hueChanged)
        self.__colorHueBarWidget.hueChangedByEditor.connect(self.__hueChangedByEditor)

        self.__colorEditorWidget = ColorEditorWidget()
        self.__colorEditorWidget.setColor(255, 255, 255)
        self.__colorEditorWidget.colorChanged.connect(self.__colorChangedByEditor)

        lay = QHBoxLayout()
        lay.addWidget(self.__colorSquareWidget)
        lay.addWidget(self.__colorHueBarWidget)
        lay.addWidget(self.__colorEditorWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def __hueChanged(self, h):
        self.__colorSquareWidget.changeHue(h)
        
    def __hueChangedByEditor(self, h):
        self.__colorSquareWidget.changeHueByEditor(h)
        
    def hsv2rgb(self, h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
        
    def __colorChanged(self, h, s, l):
        r, g, b = self.hsv2rgb(h / 100, s, l)
        self.__colorEditorWidget.setColor(r, g, b)

    def __colorChangedByEditor(self, color: QColor):
        h, s, v = colorsys.rgb_to_hsv(color.redF(), color.greenF(), color.blueF())
        self.__colorHueBarWidget.moveSelectorByEditor(h)
        self.__colorSquareWidget.moveSelectorByEditor(s, v)
        
    def getCurrentColor(self):
        return self.__colorEditorWidget.getCurrentColor()