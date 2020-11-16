# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 17:16
# @Author  : Jaywatson
# @File    : micThread.py
# @Soft    : new_control
from PyQt5.QtCore import QThread, pyqtSignal
from util.microphone import start_stream


class micSend(QThread):
    getCallbackSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(micSend, self).__init__(parent)
        self.index = -1

    def run(self):
        start_stream(self.callback, self.index)

    def callback(self,y):
        self.getCallbackSignal.emit(y)

    def setIndex(self,index):
        self.index = index