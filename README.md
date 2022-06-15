# pyqt-color-picker
PyQt color picker dialog

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-color-picker`

## Class, Method Overview
* `ColorPickerDialog(color=QColor(255, 255, 255), orientation='horizontal')`
  * `color` argument's type can be `QColor` or `str`.
  * `orientation` argument decides the overall layout direction of the dialog. There are two values. `'horizontal'`, `'vertical'`. See layout preview below.
* `getColor() -> QColor` - get the color.

### Layout type

Horizontal

![image](https://user-images.githubusercontent.com/55078043/173719486-4955a299-3dec-4f86-8d39-65848d1b8f54.png)

Vertical

![image](https://user-images.githubusercontent.com/55078043/173719694-b11e544f-4f03-4818-85aa-6095014d1817.png)

## Usage
Code Sample

```python
dialog = ColorPickerDialog()
reply = dialog.exec()
if reply == QDialog.Accepted: 
  color = dialog.getColor() # return type is QColor
  //..
```

## Preview

https://user-images.githubusercontent.com/55078043/144693507-7b078c86-8c71-4df5-869f-8380885b9108.mp4



