# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 9:47
# @Author  : Jaywatson
# @File    : TipImpl.py
# @Soft    : tomato_farm
from PyQt5.QtWidgets import QMessageBox


class tipImpl:
    # 提示窗口
    def Tips(self, message):
        QMessageBox.about(self, "提示", message)