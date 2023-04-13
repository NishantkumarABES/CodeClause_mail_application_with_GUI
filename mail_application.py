from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 547)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 0, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 80, 201, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 200, 341, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 240, 341, 121))
        self.textEdit.setObjectName("textEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.send)

        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 410, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reset)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 480, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 480, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 505, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "E-MAIL APPLICATION"))
        self.label_2.setText(_translate("MainWindow", "E-Mail ID:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "To:"))
        self.label_5.setText(_translate("MainWindow", "Subject:"))
        self.label_6.setText(_translate("MainWindow", "Body: "))
        self.pushButton.setText(_translate("MainWindow", "Send "))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label_7.setText(_translate("MainWindow", "status:"))

        
    def isEmptyFeild(self):
        s_email=self.lineEdit.text()
        s_pass=self.lineEdit_2.text()
        r_email=self.lineEdit_3.text()
        if s_email=="" or s_pass=="" or r_email=="":
            return 1
        else:
            return 0
    
    def reset(self):
        s_email=self.lineEdit.clear()
        s_pass=self.lineEdit_2.setText("")
        r_email=self.lineEdit_3.setText("")
        subject=self.lineEdit_4.setText("")
        body=self.textEdit.setText("")
        self.label_8.setText("")
    
    def send(self):
        try:
            if not(self.isEmptyFeild()):
                server = smtplib.SMTP("smtp.gmail.com",587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                sender_email=self.lineEdit.text()
                sender_password=self.lineEdit_2.text()
                server.login(sender_email,sender_password)
                receiver_email=self.lineEdit_3.text()
                subject=self.lineEdit_4.text()
                body=self.textEdit.toPlainText()
                
                
                message="Subject: {}\n\n{}".format(subject,body)
                server.sendmail(sender_email,receiver_email,message)
                self.label_8.setText("mail sent successfull!")
                self.label_8.setStyleSheet("color: green")
                
            else:
                self.label_8.setText("Required field is empty.(click Reset)")
                self.label_8.setStyleSheet("color: red")
                
                
                
                
        except Exception as e:
            print(e)
            self.label_8.setText("Unsuccessfull!(click Reset)")
            self.label_8.setStyleSheet("color: red")
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#njseccwfokqiixrr
