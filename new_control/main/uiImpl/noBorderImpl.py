# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 22:46
# @Author  : Jaywatson
# @File    : noBorderImpl.py
# @Soft    : tomato_farm
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QEnterEvent
from PyQt5.QtWidgets import QMessageBox
Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class noBorderImpl:

    flag = False
    _m_Position = None
    Margins = 3
    Direction = None

    def move(self, pos):
        if self.windowState() == QtCore.Qt.WindowMaximized or self.windowState() == QtCore.Qt.WindowFullScreen:
            # 最大化或者全屏则不允许移动
            return

    # 无边框移动窗体
    def mousePressEvent(self, QMouseEvent):
        try:
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                self.flag = True
                self._m_Position = QMouseEvent.globalPos() - self.pos()
                if self.Direction == None or self.Direction not in range(8):
                    self.setCursor(QtCore.Qt.ClosedHandCursor)
                QMouseEvent.accept()
        except Exception as e:
            self.confnoborder.error(e)
            pass

    def mouseMoveEvent(self, QMouseEvent):
        try:
            pos = QMouseEvent.pos()
            xPos, yPos = pos.x(), pos.y()
            wm, hm = self.width() - self.Margins, self.height() - self.Margins
            if QtCore.Qt.LeftButton and self.flag:
                if self.Direction == None or self.Direction not in range(8):
                    self.move(QMouseEvent.globalPos() - self._m_Position)
                    # QMouseEvent.accept()
                else:
                    self._resizeWidget(pos)
            elif xPos <= self.Margins and yPos <= self.Margins:
                # 左上角
                self.Direction = LeftTop
                self.setCursor(QtCore.Qt.SizeFDiagCursor)
            elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
                # 右下角
                self.Direction = RightBottom
                self.setCursor(QtCore.Qt.SizeFDiagCursor)
            elif wm <= xPos and yPos <= self.Margins:
                # 右上角
                self.Direction = RightTop
                self.setCursor(QtCore.Qt.SizeBDiagCursor)
            elif xPos <= self.Margins and hm <= yPos:
                # 左下角
                self.Direction = LeftBottom
                self.setCursor(QtCore.Qt.SizeBDiagCursor)
            elif 0 <= xPos <= self.Margins and self.Margins <= yPos <= hm:
                # 左边
                self.Direction = Left
                self.setCursor(QtCore.Qt.SizeHorCursor)
            elif wm <= xPos <= self.width() and self.Margins <= yPos <= hm:
                # 右边
                self.Direction = Right
                self.setCursor(QtCore.Qt.SizeHorCursor)
            elif self.Margins <= xPos <= wm and 0 <= yPos <= self.Margins:
                # 上面
                self.Direction = Top
                self.setCursor(QtCore.Qt.SizeVerCursor)
            elif self.Margins <= xPos <= wm and hm <= yPos <= self.height():
                # 下面
                self.Direction = Bottom
                self.setCursor(QtCore.Qt.SizeVerCursor)
            else:
                self.Direction = None
                self.setCursor(QtCore.Qt.ArrowCursor)
        except Exception as e:
            self.confnoborder.error(e)
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        try:
            self.flag = False
            self.setCursor(QtCore.Qt.ArrowCursor)
        except Exception as e:
            self.confnoborder.error(e)
            pass
        finally:
            self.setCursor(QtCore.Qt.ArrowCursor)

    # 调整窗体大小
    def _resizeWidget(self, pos):
        """调整窗口大小"""
        if self.Direction == None:
            return
        mpos = pos - self._m_Position
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:  # 右下角
            if w + xPos > self.minimumWidth():
                w += xPos
                self._m_Position = pos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._m_Position = pos
        elif self.Direction == RightTop:  # 右上角
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
                self._m_Position.setX(pos.x())
        elif self.Direction == LeftBottom:  # 左下角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._m_Position.setY(pos.y())
        elif self.Direction == Left:  # 左边
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + xPos > self.minimumWidth():
                w += xPos
                self._m_Position = pos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + yPos > self.minimumHeight():
                h += yPos
                self._m_Position = pos
            else:
                return
        self.setGeometry(x, y, w, h)