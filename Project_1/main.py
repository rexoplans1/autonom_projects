from ui_main_design import Ui_MainWindow

from PySide2.QtWidgets import*
from PySide2.QtGui import QIcon
from PySide2.QtSerialPort import QSerialPortInfo,QSerialPort
from PySide2.QtCore import QIODevice
from PySide2 import QtSerialPort
from serial.tools import list_ports
import serial

from PySide2.QtCore import*
from PySide2 import QtCore
from PySide2.QtGui import QIcon, QColor 
from PySide2.QtWidgets import*
from PySide2 import QtWidgets
from PySide2 import QtSerialPort

class mainClass(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Click button
        self.connectButton.clicked.connect(self.serial_test)  
        self.disconnectButton.clicked.connect(self.serial_close) 
        self.sendButton.clicked.connect(self.portSendData)

        #Refresh Button
        self.refreshButton.setShortcut("F5")  
        self.refreshButton.clicked.connect(self.refresh)

        self.check_ports()
       

    def serial_test(self):
        self.serial = QtSerialPort.QSerialPort(self)
        self.serial.setPortName(self.comboboxPort.currentText())
        if self.serial.open(QIODevice.ReadWrite):
            self.serial.setBaudRate(int(self.comboboxBaudrate.currentText()))
            #self.serial.readyRead.connect(self.on_serial_read)  # line 152  buraya algoritma gelicek
            self.serial.readyRead.connect(self.portDataReceived) 
            self.sendButton.clicked.connect(self.portSendData)
            self.connectButton.setEnabled(False)
            self.disconnectButton.setEnabled(True)
            print("connected")

    def serial_close(self):
        self.serial.close()
        self.disconnectButton.setEnabled(False)
        self.connectButton.setEnabled(True)
        print("disconnect")
        
    def check_ports(self):
        ports = list_ports.comports()
        for port in ports:
            man = port.manufacturer if port.manufacturer else "None"
            #self.comboboxPort.addItem(port.usb_description())
            #port.serial_number = STLINK device serial number
            self.comboboxPort.addItem(f"{port.usb_description()}/{man}")
            print(ports)
#            self.cb_ports.addItem(f"{man}: {port.usb_description()}")


    def print_port(self):
        print(self.comboboxPort.currentText())
        serial_inst = serial.Serial()
        serial_inst.baudrate = int(self.comboboxBaudrate.currentText())
        print(int(self.comboboxBaudrate.currentText()))
        serial_inst.port = self.comboboxPort.currentText()
        serial_inst.open()

    def refresh(self):
        self.comboboxPort.clear()
        self.comboboxPort.addItem("Select")
        self.check_ports()
        print("refresh")

    def portDataReceived(self):
        self.readTextEdit.append(self.serial.readAll().data().decode())
        print(self.serial.readAll().data().decode())

    def portSendData(self):       
        self.serial.write(self.writeLineEdit.text().encode())



Application= QApplication([])
screen= mainClass()
screen.show() 
Application.exec_()
