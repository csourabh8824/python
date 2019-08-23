import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
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
      label = QLabel(self)
      label.setStyleSheet('background-image: url(a.jpg);')
      pixmap = QPixmap('a.jpg')  # type: QPixmap
      label.setPixmap(pixmap)

      self.resize(pixmap.width(),pixmap.height())
      
      
      self.UiCoffee()
      self.UiTea()
      self.UiGreenTea()
      self.UiMocktail()		
      self.show()
   
      

   def UiCoffee(self):
      button = QPushButton("COFFEE", self)
      button.move(250,58)
      button.resize(90,40)
      button.setStyleSheet("background-color:red");
      button.setStyleSheet("color: red");


   def UiTea(self):
      button = QPushButton("TEA", self)
      button.move(350,58)
      button.resize(90,40)
      button.setStyleSheet("background-color: red");
      button.setStyleSheet("color: brown");

   def UiGreenTea(self):
      button = QPushButton("GREEN TEA", self)
      button.move(450,58)
      button.resize(100,40)
      button.setStyleSheet("background-color: red");
      button.setStyleSheet("color: green");

   def UiMocktail(self):
      button = QPushButton("MOCKTAIL", self)
      button.move(560,58)
      button.resize(90,40)
      button.setStyleSheet("background-color: red");
      button.setStyleSheet("color: blue");
      
      

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())










