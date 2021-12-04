import math

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QRect


class ColorSquareWidget(QWidget):
    colorChanged = pyqtSignal(float, float, float)

    def __init__(self):
        super().__init__()
        self.__h = 0
        self.__s = 0
        self.__l = 1
        self.__initUi()

    def __initUi(self):
        self.setMinimumSize(300, 300)

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

        self.__blackOverlay.mouseMoveEvent = self.__moveSelector
        self.__blackOverlay.mousePressEvent = self.__moveSelector

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

    def __moveSelector(self, e):
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
        self.__h = h
        self.__colorView.setStyleSheet(f'''
            border-radius: 5px;
            background-color: qlineargradient(x1:1, x2:0,
            stop:0 hsl({self.__h}%,100%,50%),
            stop:1 #fff);
        ''')

    def __setSaturation(self):
        self.__s = (self.__selector.pos().x()+math.floor(self.__selector_diameter/2)) / self.width()

    def getSaturatation(self):
        return self.__s

    def __setLightness(self):
        self.__l = abs(((self.__selector.pos().y()+math.floor(self.__selector_diameter/2)) / self.height()) - 1)

    def getLightness(self):
        return self.__l

    def moveSelectorByEditor(self, s, l):
        geo = self.__selector.geometry()
        x = self.width() * s
        y = self.height() - self.height() * l
        geo.moveCenter(QPoint(x, y))
        self.__selector.setGeometry(geo)