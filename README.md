# pyqt-color-picker
PyQt color picker dialog

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-color-picker`

## Class, Method Overview
* `ColorPickerDialog(color=QColor(255, 255, 255))` - Color argument's type can be `QColor`, `str`.
* `getColor() -> QColor`

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



