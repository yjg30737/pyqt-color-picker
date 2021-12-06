import math, colorsys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect


class ColorSquareWidget(QWidget):
    colorChanged = pyqtSignal(float, float, float)

    def __init__(self, color: QColor = QColor(255, 255, 255)):
        super().__init__()
        self.__initUi(color)

    def __initUi(self, color: QColor):
        self.setMinimumSize(300, 300)

        self.__h, \
        self.__s, \
        self.__l = colorsys.rgb_to_hsv(color.redF(), color.greenF(), color.blueF())

        # Multiply 100 for insert into stylesheet code
        self.__h *= 100

        self.__colorView = QWidget()
        self.__colorView.setStyleSheet(f'''
            background-color: qlineargradient(x1:1, x2:0, 
            stop:0 hsl({self.__h}%,100%,50%), 
            stop:1 #fff);
            border-radius: 5px;
        ''')

        self.__blackOverlay = QWidget()
        self.__blackOverlay.setStyleSheet('''
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, 
            stop:0 rgba(0, 0, 0, 0), 
            stop:1 rgba(0, 0, 0, 255));
            width:100%;
            border-radius: 5px;
        ''')

        self.__blackOverlay.mouseMoveEvent = self.__moveSelectorByCursor
        self.__blackOverlay.mousePressEvent = self.__moveSelectorByCursor

        self.__selector_diameter = 12

        self.__selector = QWidget(self.__blackOverlay)
        self.__selector.setGeometry(math.floor(self.__selector_diameter/2) * -1,
                                    math.floor(self.__selector_diameter/2) * -1,
                                    self.__selector_diameter,
                                    self.__selector_diameter)
        self.__selector.setStyleSheet('''
            background-color: none;
            border: 1px solid white;
            border-radius: 5px;
        ''')

        self.__blackRingInsideSelector = QLabel(self.__selector)
        self.__blackRingInsideSelector_diameter = self.__selector_diameter-2
        self.__blackRingInsideSelector.setGeometry(QRect(1, 1, self.__blackRingInsideSelector_diameter,
                                                               self.__blackRingInsideSelector_diameter))
        self.__blackRingInsideSelector.setStyleSheet('''
            background-color: none;
            border: 1px solid black;
            border-radius: 5px;
        ''')

        self.__blackRingInsideSelector.setText("")
        
        lay = QGridLayout()
        lay.addWidget(self.__colorView, 0, 0, 1, 1)
        lay.addWidget(self.__blackOverlay, 0, 0, 1, 1)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

        self.__initSelector()

    def __moveSelectorNotByCursor(self, s, l):
        geo = self.__selector.geometry()
        x = self.minimumWidth() * s
        y = self.minimumHeight() - self.minimumHeight() * l
        geo.moveCenter(QPoint(x, y))
        self.__selector.setGeometry(geo)

    def __initSelector(self):
        self.__moveSelectorNotByCursor(self.__s, self.__l)

    def __moveSelectorByCursor(self, e):
        if e.buttons() == Qt.LeftButton:
            pos = e.pos()
            if pos.x() < 0:
                pos.setX(0)
            if pos.y() < 0:
                pos.setY(0)
            if pos.x() > 300:
                pos.setX(300)
            if pos.y() > 300:
                pos.setY(300)

            self.__selector.move(pos - QPoint(math.floor(self.__selector_diameter/2),
                                              math.floor(self.__selector_diameter/2)))
            
            self.__setSaturation()
            self.__setLightness()

            self.colorChanged.emit(self.__h, self.__s, self.__l)

    def changeHue(self, h):
        self.__h = h
        self.__colorView.setStyleSheet(f'''
            border-radius: 5px;
            background-color: qlineargradient(x1:1, x2:0,
            stop:0 hsl({self.__h}%,100%,50%),
            stop:1 #fff);
        ''')

        self.colorChanged.emit(self.__h, self.__s, self.__l)

    def changeHueByEditor(self, h):
        # Prevent hue from becoming larger than 100
        # if hue becomes larger than 100, hue of square will turn into dark.
        self.__h = min(100, h)
        self.__colorView.setStyleSheet(f'''
            border-radius: 5px;
            background-color: qlineargradient(x1:1, x2:0,
            stop:0 hsl({self.__h}%,100%,50%),
            stop:1 #fff);
        ''')

    def __setSaturation(self):
        self.__s = (self.__selector.pos().x()+math.floor(self.__selector_diameter/2)) / self.minimumWidth()

    def getSaturatation(self):
        return self.__s

    def __setLightness(self):
        self.__l = abs(((self.__selector.pos().y()+math.floor(self.__selector_diameter/2)) / self.minimumHeight()) - 1)

    def getLightness(self):
        return self.__l

    def moveSelectorByEditor(self, s, l):
        self.__moveSelectorNotByCursor(s, l)