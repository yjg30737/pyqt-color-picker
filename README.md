# pyqt-color-dialog
PyQt Color Dialog

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-color-dialog.git --upgrade```

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



