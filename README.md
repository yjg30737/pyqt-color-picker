# pyqt-color-picker
PyQt color picker dialog which contains color picker widget.

You can either use dialog or widget.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-color-picker`

## Class, Method Overview
### `ColorPickerDialog`
* `ColorPickerDialog(color=QColor(255, 255, 255), orientation='horizontal')`
  * `color` argument's type can be `QColor` or `str`.
  * `orientation` argument decides the overall layout direction of the dialog. There are two values. `'horizontal'`, `'vertical'`. See layout preview below.
* `getColor() -> QColor` - get the color.

If you only want to use this as a part of window(not as whole dialog), use `ColorPickerWidget(color=QColor(255, 255, 255), orientation='horizontal')`. See the example below.

### `ColorPickerWidget`
* `colorChanged` - signal. After color being changed, this will be emitted.
* `getCurrentColor` - get the current color.

### Layout type

Horizontal

![image](https://user-images.githubusercontent.com/55078043/173719486-4955a299-3dec-4f86-8d39-65848d1b8f54.png)

Vertical

![image](https://user-images.githubusercontent.com/55078043/173719694-b11e544f-4f03-4818-85aa-6095014d1817.png)

## Usage
### Dialog

#### Code Sample

```python
dialog = ColorPickerDialog()
reply = dialog.exec()
if reply == QDialog.Accepted: 
  color = dialog.getColor() # return type is QColor
  //..
```

#### Result

https://user-images.githubusercontent.com/55078043/144693507-7b078c86-8c71-4df5-869f-8380885b9108.mp4

### Using as a part of window

#### Code Sample
```python
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QTextEdit
from pyqt_color_picker import ColorPickerWidget


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        te = QTextEdit()
        colorPicker = ColorPickerWidget(orientation='vertical')
        lay = QHBoxLayout()
        lay.addWidget(te)
        lay.addWidget(colorPicker)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
```

#### Result

![image](https://user-images.githubusercontent.com/55078043/173720243-f7867319-dd44-44f4-9569-56cee298330f.png)


