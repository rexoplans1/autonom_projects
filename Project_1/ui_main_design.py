# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(994, 528)
        icon = QIcon()
        icon.addFile(u":/newPrefix/Icons8-Windows-8-Military-Grenade.qrc", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actiongelicek = QAction(MainWindow)
        self.actiongelicek.setObjectName(u"actiongelicek")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout_2 = QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setMinimumSize(QSize(0, 1))
        self.refreshButton.setMaximumSize(QSize(0, 1))

        self.gridLayout.addWidget(self.refreshButton, 0, 1, 1, 1)

        self.comboboxBaudrate = QComboBox(self.centralwidget)
        self.comboboxBaudrate.addItem("")
        self.comboboxBaudrate.addItem("")
        self.comboboxBaudrate.addItem("")
        self.comboboxBaudrate.setObjectName(u"comboboxBaudrate")
        self.comboboxBaudrate.setMinimumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboboxBaudrate.setFont(font)

        self.gridLayout.addWidget(self.comboboxBaudrate, 2, 1, 1, 1)

        self.disconnectButton = QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.disconnectButton.setFont(font1)

        self.gridLayout.addWidget(self.disconnectButton, 5, 1, 1, 1)

        self.readTextEdit = QTextEdit(self.centralwidget)
        self.readTextEdit.setObjectName(u"readTextEdit")
        self.readTextEdit.setMinimumSize(QSize(0, 0))
        self.readTextEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.readTextEdit, 6, 1, 1, 1)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setMinimumSize(QSize(0, 40))
        self.connectButton.setFont(font1)

        self.gridLayout.addWidget(self.connectButton, 4, 1, 1, 1)

        self.comboboxPort = QComboBox(self.centralwidget)
        self.comboboxPort.addItem("")
        self.comboboxPort.setObjectName(u"comboboxPort")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboboxPort.sizePolicy().hasHeightForWidth())
        self.comboboxPort.setSizePolicy(sizePolicy1)
        self.comboboxPort.setMinimumSize(QSize(400, 50))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.comboboxPort.setFont(font2)

        self.gridLayout.addWidget(self.comboboxPort, 1, 1, 1, 1)

        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.sendButton, 8, 1, 1, 1)

        self.writeLineEdit = QLineEdit(self.centralwidget)
        self.writeLineEdit.setObjectName(u"writeLineEdit")

        self.gridLayout.addWidget(self.writeLineEdit, 7, 1, 1, 1)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiongelicek.setText(QCoreApplication.translate("MainWindow", u"gelicek", None))
        self.refreshButton.setText("")
        self.comboboxBaudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Baudrate", None))
        self.comboboxBaudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboboxBaudrate.setItemText(2, QCoreApplication.translate("MainWindow", u"115200", None))

        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.comboboxPort.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Port", None))

        self.comboboxPort.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Port", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

