# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.windowBar.setFont(font)
        self.windowBar.setStyleSheet("QWidget#windowBar{\n"
"background:gray;\n"
"border-top:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-top-left-radius:7px;\n"
"border-top-right-radius:7px;\n"
"}\n"
"#windowBar>QPushButton{\n"
"border-radius:8px\n"
"}")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout.setContentsMargins(7, 3, 7, 3)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(715, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.miniPushButton = QtWidgets.QPushButton(self.windowBar)
        self.miniPushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.miniPushButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.miniPushButton.setFont(font)
        self.miniPushButton.setStyleSheet("QPushButton{\n"
"    background:#FEE66E;\n"
"}\n"
"QPushButton::hover{\n"
"    background:#c5b355;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#c5b355;\n"
"}\n"
"")
        self.miniPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/miniShow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.miniPushButton.setIcon(icon)
        self.miniPushButton.setIconSize(QtCore.QSize(10, 10))
        self.miniPushButton.setObjectName("miniPushButton")
        self.horizontalLayout.addWidget(self.miniPushButton)
        self.closePushButton = QtWidgets.QPushButton(self.windowBar)
        self.closePushButton.setMinimumSize(QtCore.QSize(16, 16))
        self.closePushButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.closePushButton.setFont(font)
        self.closePushButton.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton::hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton::pressed{\n"
"    background:#aa3e3e;\n"
"}\n"
"")
        self.closePushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon1)
        self.closePushButton.setIconSize(QtCore.QSize(10, 10))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        self.verticalLayout.addWidget(self.windowBar)
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.mainWidget.setFont(font)
        self.mainWidget.setStyleSheet("QWidget#mainWidget{\n"
"background:#e9eaed;\n"
"border-bottom:1px solid gray;\n"
"border-right:1px solid gray;\n"
"border-left:1px solid gray;\n"
"border-bottom-left-radius:7px;\n"
"border-bottom-right-radius:7px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    border:1px solid gray;\n"
"    background:white;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border:1px solid gray;\n"
"    background:white;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    width: 20px;\n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-left-color: gray; \n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    border-image:url(:/icon/down.png);\n"
"}\n"
"\n"
"QComboBox>QAbstractItemView \n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"}\n"
"     \n"
"QComboBox QAbstractItemView::item\n"
"{\n"
"    height: 24px;\n"
"}\n"
"     \n"
"QComboBox QAbstractItemView::item:selected\n"
"{    \n"
"    background-color: rgba(54, 98, 180);\n"
"}\n"
"\n"
"QSpinBox,QDoubleSpinBox{\n"
"    border:1px solid gray;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"}\n"
"\n"
"/*spinbox 抬起样式*/\n"
"QDoubleSpinBox::up-button,QSpinBox::up-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"QDoubleSpinBox::down-button,QSpinBox::down-button {\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"    border-image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}\n"
"/*按钮按下样式*/\n"
"QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"    subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/icon/add.png);\n"
"    width: 16px;\n"
"    height: 20px;       \n"
"}\n"
"  \n"
"QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"    image: url(:/icon/remove.png);\n"
"    width: 16px;\n"
"    height: 17px;\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 8, 10, 8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.widget.setFont(font)
        self.widget.setStyleSheet("QWidget>QPushButton{\n"
"    border:none;\n"
"    color:white;\n"
"    border-radius:10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setContentsMargins(4, 2, 4, 2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.device_list = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.device_list.setFont(font)
        self.device_list.setStyleSheet("QAbstractItemView \n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: lightgray;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    border-radius:10px;\n"
"}\n"
"     \n"
"QAbstractItemView::item\n"
"{\n"
"    height: 26px;\n"
"}\n"
"     \n"
"QAbstractItemView::item:selected\n"
"{    \n"
"    background-color: rgba(54, 98, 180);\n"
"}")
        self.device_list.setObjectName("device_list")
        self.device_list.addItem("")
        self.device_list.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.device_list)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ip_edit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.ip_edit.setFont(font)
        self.ip_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.ip_edit.setObjectName("ip_edit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ip_edit)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sure_button = QtWidgets.QPushButton(self.widget)
        self.sure_button.setMinimumSize(QtCore.QSize(0, 20))
        self.sure_button.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.sure_button.setFont(font)
        self.sure_button.setStyleSheet("QPushButton{\n"
"    background:#6CE872;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#53b357;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#53b357;\n"
"}")
        self.sure_button.setObjectName("sure_button")
        self.horizontalLayout_3.addWidget(self.sure_button)
        self.stop_button = QtWidgets.QPushButton(self.widget)
        self.stop_button.setMinimumSize(QtCore.QSize(0, 20))
        self.stop_button.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet("QPushButton{\n"
"    background:#F95D5C;\n"
"}\n"
"QPushButton:hover{\n"
"    background:#aa3e3e;\n"
"}\n"
"QPushButton:pressed{\n"
"    border:1px solid white;\n"
"    background:#aa3e3e;\n"
"}")
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_3.addWidget(self.stop_button)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.port_edit = QtWidgets.QSpinBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(False)
        font.setWeight(50)
        self.port_edit.setFont(font)
        self.port_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.port_edit.setMinimum(1)
        self.port_edit.setMaximum(65535)
        self.port_edit.setProperty("value", 7777)
        self.port_edit.setObjectName("port_edit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.port_edit)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.setStretch(1, 7)
        self.horizontalLayout_2.addWidget(self.widget)
        self.wave_widget = QtWidgets.QWidget(self.mainWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.wave_widget.setFont(font)
        self.wave_widget.setObjectName("wave_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wave_widget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2.addWidget(self.wave_widget)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.mainWidget)
        self.verticalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.closePushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "输入设备："))
        self.device_list.setItemText(0, _translate("MainWindow", "1"))
        self.device_list.setItemText(1, _translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "输出IP："))
        self.ip_edit.setInputMask(_translate("MainWindow", "000.000.000.000;0"))
        self.label_4.setText(_translate("MainWindow", "运行端口："))
        self.sure_button.setText(_translate("MainWindow", "启动"))
        self.stop_button.setText(_translate("MainWindow", "停止"))
        self.label.setText(_translate("MainWindow", "运行日志"))
import icons_rc
