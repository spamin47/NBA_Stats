import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.setWindowIcon(QIcon("maps.ico"))
        self.resize(500,350) #width, height
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.inputField = QLineEdit()
        button = QPushButton('&Click Me',clicked = self.outputSmt)
        self.output = QTextEdit()
        
        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
    
    def outputSmt(self):
        inputText = self.inputField.text()
        self.output.setText("Hello {0}".format(inputText))


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