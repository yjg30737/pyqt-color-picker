import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-color-picker',
    version='0.0.20',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_color_picker.style': ['black_overlay.css', 'black_ring_of_color_selector.css',
                                              'color_selector.css', 'hue_bg.css', 'hue_frame.css',
                                              'hue_selector.css']},
    description='PyQt color picker dialog',
    url='https://github.com/yjg30737/pyqt-color-picker.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
    ]
)