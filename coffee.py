# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coffee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QLabel,QLineEdit,QPushButton,QInputDialog

from time import strftime
import MySQLdb as mdb
import mysql.connector
from mysql.connector import Error
a=10
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 659)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        Form.setFocusPolicy(QtCore.Qt.WheelFocus)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-family : sans-serif;\n"
"background:black;\n"
"}\n"
"")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 270, 241, 61))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton\n"
"{\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"font-style:decorative;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Desktop/cup-of-coffee-icon-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 270, 241, 61))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setToolTip("")
        self.pushButton_2.setStyleSheet("#pushButton_2\n"
"{\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cup5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 390, 241, 61))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3.setToolTip("")
        self.pushButton_3.setStyleSheet("#pushButton_3\n"
"{\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cup.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 390, 241, 61))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setToolTip("")
        self.pushButton_4.setStyleSheet("#pushButton_4\n"
"{\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("cup0.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(80, 530, 561, 71))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMouseTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setStyleSheet("#label\n"
"{\n"
"\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"font-size:35px;\n"
"}")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.clicked.connect(self.ref)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 340, 111, 41))
        self.pushButton_5.setToolTip("")
        self.pushButton_5.setStyleSheet("#pushButton_5\n"
"{\n"
"background:brown;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:30px;\n"
"font-style:decorative;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 40, 191, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("download.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def ref(self):
        dbs=db()
        dbs.exec_()
       # abc=Main()
        #abc.exec_()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "coffee vending machine"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p>Dispense Cappuccino</p></body></html>"))
        self.pushButton.setText(_translate("Form", "     CAPPUCCINO"))
        self.pushButton_2.setText(_translate("Form", "           LATTE"))
        self.pushButton_3.setText(_translate("Form", "            COFFEE"))
        self.pushButton_4.setText(_translate("Form", "      ESPRESSO"))
        self.label.setText(_translate("Form", "COFFEE    VENDING    MACHINE"))
        self.pushButton_5.setText(_translate("Form", "RE-FILL"))

#---------Window settings --------------------------------
         
        #self.setGeometry(300,300,250,100)
        #self.setWindowTitle("Clock")

"""class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(1000)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.display(strftime("%H"+":"+"%M"))
 
        self.setCentralWidget(self.lcd)
 
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,250,100)
        self.setWindowTitle("Clock")
 
#-------- Slots ------------------------------------------
 
    def Time(self):
        self.lcd.display(strftime("%H"+":"+"%M"))
       """  
#import test2_rc
class db(QDialog):
    def __init__(self):
        super().__init__()
 
        self.title = "PyQt5 Database Connection"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()
 
 
    def InitWindow(self):
       
        self.DBConnection()
 
        
        self.show()
 
 
    def DBConnection(self):
        try:
            db = mdb.connect('localhost', 'root', 'root', 'sourabh')
            QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
            login=LoginDlg()
            sys.exit(login.exec_())
 
        except mdb.Error as e:
            QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            


class LoginDlg(QDialog):

   def __init__(self):
      super().__init__()
      self.title = 'COFFEE VENDING MACHINE'
      self.left = 10
      self.top = 10
      self.width = 640
      self.height = 480
      self.initUI()
   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
      self.Uiadmin()

   def Uiadmin(self):
         label1=QLabel(self)
         label1.setText('Username')
         label1.move(150,150)
         self.text1 =QLineEdit(self)
         self.text1.move(300,150)
         label2 = QLabel(self)
         label2.setText('Password')
         label2.move(150,180)
         self.text2 = QLineEdit(self)
         self.text2.move(300, 180)
         button=QPushButton(self)
         button.setText('Continue')
         button.move(225,210)
         button.clicked.connect(self.login)

   def login(self):
         db = mdb.connect('localhost', 'root', 'root', 'sourabh')
         query="select * from admin where a_name= %s and a_password= %s;"
         cursor = db.cursor()
         cursor.execute(query,self.text1.text(),self.text2.text())
         row=cursor.fetchone()
         print(row)
         """
         if :
             
                print("Welcome!")
                r = refill()
                if r.exec_():
                     a_name=self.text1.text()

                else:
                     QMessageBox.about(self, 'Connection', 'That is the wrong Password!')
         else:
           QMessageBox.about(self, 'Connection', 'That is the wrong Username!')
class refill(QDialog):

   def __init__(self):
      super().__init__()
      self.title = 'ADMIN PAGE'
      self.left = 10
      self.top = 10
      self.width = 640
      self.height = 480
      self.initUI()
      self.capacity()
   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
   def capacity(self):
      i, okPressed = QInputDialog.getInt(self, "Get integer","Capacity:", 1, 0, 100, 1)
      if okPressed:
        print(i)
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

