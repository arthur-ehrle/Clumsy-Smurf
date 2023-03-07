# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

#####################################################################################
#************************* IMPORTS **************************************************
#####################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QWidget, QLabel, QMainWindow, QGridLayout ,QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
import os
import re
import threading
import subprocess
import time

#####################################################################################
#************************* FORME ****************************************************
#####################################################################################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(881, 584)
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png')) 
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 2)
        self.line_ip_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ip_1.setObjectName("line_ip_1")
        self.line_ip_1.textChanged.connect(self.ping)
        self.gridLayout.addWidget(self.line_ip_1, 3, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.line_ip_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ip_2.setObjectName("line_ip_2")
        self.line_ip_2.textChanged.connect(self.ping)
        self.gridLayout.addWidget(self.line_ip_2, 4, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.dhcp)
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.static)
        self.checkBox_2.hide()
        self.gridLayout.addWidget(self.checkBox_2, 6, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 2)
        self.combo_nic = QtWidgets.QComboBox(self.centralwidget)
        self.combo_nic.setObjectName("combo_nic")
        self.combo_nic.addItem("Ethernet")
        self.combo_nic.addItem("Wi-Fi")
        self.combo_nic.addItem("Ethernet 2")
        self.combo_nic.addItem("Ethernet 3")
        self.combo_nic.addItem("Ethernet 4")
        self.combo_nic.currentIndexChanged.connect(self.val_nic)
        
        self.gridLayout.addWidget(self.combo_nic, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 2)
        self.ip_state_1 = QtWidgets.QLabel(self.centralwidget)
        self.ip_state_1.setObjectName("ip_state_1")
        self.ip_state_1.setStyleSheet("color: red;")
        self.gridLayout.addWidget(self.ip_state_1, 3, 3, 1, 1)
        self.ip_state_2 = QtWidgets.QLabel(self.centralwidget)
        self.ip_state_2.setObjectName("ip_state_2")
        self.ip_state_2.setStyleSheet("color: red;")
        self.gridLayout.addWidget(self.ip_state_2, 4, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 4, 1, 3, QtCore.Qt.AlignHCenter)
        
        self.val_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.val_ip.setObjectName("val_ip")
        self.gridLayout.addWidget(self.val_ip, 7, 2, 1, 2)
        self.val_dns2 = QtWidgets.QLineEdit(self.centralwidget)
        self.val_dns2.setObjectName("val_dns2")
        self.gridLayout.addWidget(self.val_dns2, 11, 2, 1, 2)
        self.val_mask = QtWidgets.QLineEdit(self.centralwidget)
        self.val_mask.setObjectName("val_mask")
        self.gridLayout.addWidget(self.val_mask, 8, 2, 1, 2)
        self.val_dns1 = QtWidgets.QLineEdit(self.centralwidget)
        self.val_dns1.setObjectName("val_dns1")
        self.gridLayout.addWidget(self.val_dns1, 10, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ipconfig)
        self.ip_state_2.setStyleSheet("color: red;")
        self.gridLayout.addWidget(self.pushButton, 12, 2, 1, 2)
        self.val_gateway = QtWidgets.QLineEdit(self.centralwidget)
        self.val_gateway.setObjectName("val_gateway")
        self.gridLayout.addWidget(self.val_gateway, 9, 2, 1, 2)
        self.list_events = QtWidgets.QListWidget(self.centralwidget)
        self.list_events.setObjectName("list_events")
        self.gridLayout.addWidget(self.list_events, 9, 6, 4, 2)
        self.list_routing = QtWidgets.QListWidget(self.centralwidget)
        self.list_routing.setObjectName("list_routing")
        self.gridLayout.addWidget(self.list_routing, 2, 7, 1, 1)
        self.list_arp = QtWidgets.QListWidget(self.centralwidget)
        self.list_arp.setObjectName("list_arp")
        self.gridLayout.addWidget(self.list_arp, 2, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 7, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 881, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aide réseau"))
        self.label_4.setText(_translate("MainWindow", "Gateway"))
        self.label_8.setText(_translate("MainWindow", "IP n°1 :"))
        self.label_7.setText(_translate("MainWindow", "Ping :"))
        self.label_5.setText(_translate("MainWindow", "DNS1"))
        self.label_2.setText(_translate("MainWindow", "IP"))
        self.checkBox.setText(_translate("MainWindow", "DHCP"))
        self.checkBox_2.setText(_translate("MainWindow", "Manual"))
        self.label_13.setText(_translate("MainWindow", "Events :"))
        self.label_10.setText(_translate("MainWindow", "Carte réseau :"))
        self.label_6.setText(_translate("MainWindow", "DNS2"))
        self.label_3.setText(_translate("MainWindow", "Mask"))
        self.ip_state_1.setText(_translate("MainWindow", "NO"))
        self.ip_state_2.setText(_translate("MainWindow", "NO"))
        self.label_9.setText(_translate("MainWindow", "IP n°2 :"))
        self.label.setText(_translate("MainWindow", "Informations - réseau"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_11.setText(_translate("MainWindow", "Routing table :"))
        self.label_12.setText(_translate("MainWindow", "ARP table :"))


        t = threading.Thread(name='timer-func', target=self.timer, daemon=True)
                            #nom du thread          fonction visée                      'thread continu' 
        t.start()

#####################################################################################
#************************* FONCTIONS ************************************************
#####################################################################################
    def arp(self):
        self.list_arp.clear()
        with os.popen('arp -a') as f:
            data = f.read()

        for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
            self.list_arp.addItem(str(line))

    def static(self):
        self.arp()

    def ipconfig(self):
        ## VALEURS ##
        dns1=self.val_dns1.text()
        dns2=self.val_dns2.text()
        gateway=self.val_gateway.text()
        ip=self.val_ip.text()
        mask=self.val_mask.text()

        ## COMMANDE ##
        if ip != '' and mask != '':
            os.popen("""netsh interface ip set address name="{}" static {} {} {} """.format(nic_name,ip,mask,gateway))
            if dns1 != '':
                os.popen("""netsh interface ip set dns name="{}" static {} """.format(nic_name,dns1))
                os.popen("""netsh interface ip add dns name="{}" {} 2 """.format(nic_name,dns2))

            self.list_events.addItem("NIC '{}' configurée".format(nic_name))
        else:
            self.list_events.addItem("Mauvais masque / ip")
   
    def dhcp(self):
        a=self.checkBox.checkState()
        if a == 2:    
            self.val_dns1.hide()
            self.val_dns2.hide()
            self.val_gateway.hide()
            self.val_ip.hide()
            self.val_mask.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.hide()
            self.pushButton.hide()
            os.system("""netsh interface ip set address name="{}" source ="dhcp"  """.format(nic_name))
            self.list_events.addItem("NIC '"+nic_name+"' configurée en dhcp")
        if a ==0:
            self.val_dns1.show()
            self.val_dns2.show()
            self.val_gateway.show()
            self.val_ip.show()
            self.val_mask.show()
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.pushButton.show()

    def ping(self):
        ip1 = self.line_ip_1.text()
        ip2 = self.line_ip_2.text()
        if ip1 != '' and len(ip1) >= 7:
            reponse= subprocess.call('ping -w 2 -n 1 '+ip1+'')
            if reponse ==0:
                self.ip_state_1.setText("OK")
                self.ip_state_1.setStyleSheet("color: green;")
            else:
                self.ip_state_1.setText("Not OK")
                self.ip_state_1.setStyleSheet("color: red;")
        else:
                self.ip_state_1.setText("Not OK")
                self.ip_state_1.setStyleSheet("color: red;")
        if ip2 != '' and len(ip2) >= 7:
            reponse=subprocess.call('ping -w 2 -n 1 '+ip2+'') 
            if reponse ==0:
                self.ip_state_2.setText("OK")
                self.ip_state_2.setStyleSheet("color: green;")
            else:
                self.ip_state_2.setText("Not OK")
                self.ip_state_2.setStyleSheet("color: red;")
        else:
                self.ip_state_2.setText("Not OK")
                self.ip_state_2.setStyleSheet("color: red;")

    def routing_table(self):
        self.list_routing.clear()
        render = os.popen("netstat -r").read()
        for ligne in render.split('\n'):
            self.list_routing.addItem(ligne)

    def timer(self):
        time.sleep(5)
        self.ping()
        self.arp()
        self.routing_table()
        t = threading.Thread(name='timer-func', target=self.timer, daemon=True)
                            #nom du thread          fonction visée                      'thread continu' 
        t.start()

    def val_nic(self):
        global nic_name     
        index=self.combo_nic.currentIndex()
        nic_name=self.combo_nic.itemText(index)
        

#############################################################################
#************************* INITIALISATION VARIABLES *************************
#############################################################################
global nic_name
nic_name = "Ethernet"


#####################################################################################
#************************* EXECUTION ************************************************
#####################################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w) 
    w.show()
    sys.exit(app.exec_())
    