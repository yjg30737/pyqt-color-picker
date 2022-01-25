from setuptools import setup, find_packages

setup(
    name='pyqt-color-dialog',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_color_dialog.style': ['black_overlay.css', 'black_ring_of_color_selector.css',
                                              'color_selector.css', 'hue_bg.css', 'hue_frame.css',
                                              'hue_selector.css']},
    description='PyQt Color Dialog',
    url='https://github.com/yjg30737/pyqt-color-dialog.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)