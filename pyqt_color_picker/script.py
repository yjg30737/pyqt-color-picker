from PyQt5.QtGui import QColor


def getColorByInstance(color):
    if isinstance(color, QColor):
        pass
    elif isinstance(color, str):
        color = QColor(color)
    return color