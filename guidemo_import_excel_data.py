import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout
from PyQt6.QtGui import QIcon
import pandas as pd
from PyQt6.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.setWindowIcon(QIcon("maps.ico"))
        self.resize(700,500) #width, height
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.table = QTableWidget()
        layout.addWidget(self.table)
        
        self.button = QPushButton('&Load Data')
        layout.addWidget(self.button)
        
    def loadExcelData(self,excel_file_dir, worksheet_name):
        df = pd.read_excel(excel_file_dir,worksheet_name)
        
        

if __name__ == '__main__':
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

    try:
        sys.exit(app.exec()) #terminate process upon closing the system
    except SystemExit:
        print('Closing Window...')