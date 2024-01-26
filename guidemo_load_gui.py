import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6 import uic


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui\gui1.ui',self)
        self.setWindowTitle('My App')
        self.input.setText('Hello World')
        self.button.clicked.connect(self.sayHello)
    
        
    def sayHello(self):
        inputText = self.input.text()
        self.output.setText('Hello {0}'.format(inputText))
        


app = QApplication(sys.argv)
app.setStyleSheet('''
                  QWidget{
                      font-size:25px;
                  }
                  QPushButton {
                      font-size: 20px
                  }
                  ''')

window = MyApp()
window.show()

sys.exit(app.exec()) #terminate process upon closing the system