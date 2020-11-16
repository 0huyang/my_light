# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 20:54
# @Author  : Jaywatson
# @File    : main.py
# @Soft    : new_control
import sys

from PyQt5.QtWidgets import QApplication

from uiImpl.mainWindowImpl import mainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('WindowsVista')
    mainWindow = mainWindow()
    mainWindow.show()
    sys.exit(app.exec_())