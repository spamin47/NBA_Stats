import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QFrame
from PyQt6.QtWidgets import QSizePolicy, QLabel, QStackedWidget, QSpacerItem
from PyQt6.QtGui import QIcon
import pandas as pd
from PyQt6.QtCore import Qt
import dbManager



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window title")
        self.setWindowIcon(QIcon("maps.ico"))
        self.resize(400,500) #width, height
        
        self.layout = QVBoxLayout(self)
        self.stacked_widget = QStackedWidget(self)
 
        
        #Create frames and add onto the stack
        #main menu frame
        self.mainMenu_frame = QFrame()
        self.mainMenu_frame_layout = QVBoxLayout(self.mainMenu_frame)
        self.stacked_widget.addWidget(self.mainMenu_frame)
        
        #database frame
        self.database_frame = QFrame()
        self.database_frame_layout = QVBoxLayout(self.database_frame)
        self.stacked_widget.addWidget(self.database_frame)
        

        #buttons expand to fill the entire width,height of the frame
        
        
        self.layout.addWidget(self.stacked_widget)
        
        #initialize the main menu frame
        self.initMainMenuFrame()
        self.loadDatabase()
                
        # self.table = QTableWidget()
        # layout.addWidget(self.table)
        
        # self.button = QPushButton('&Load Data')
        
        # frame = QFrame()
        # frame.setMinimumSize(300,100)
        # frame_layout1 = QHBoxLayout()
        
        # frame.setLayout(frame_layout1)
        # layout.addWidget(frame)
        
        # self.button2 =  QPushButton('&Load Data')
        # frame_layout1.addWidget(self.button2)
        # frame_layout1.addWidget(self.button)
        
        # layout.addWidget(self.button)
        
    def initMainMenuFrame(self):
        #declare widgets
        mainMenu_nba_button = QPushButton("NBA")
        mainMenu_nfl_button = QPushButton("NFL")
        mainMenu_nhl_button = QPushButton("NHL")
        mainMenu_mlb_button = QPushButton("MLB")
        
        mainMenu_label = QLabel("Sport Data Basement")
        
        #modify widgets
        mainMenu_nba_button.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        mainMenu_nfl_button.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        mainMenu_nhl_button.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        mainMenu_mlb_button.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        
        #connect buttons
        mainMenu_nba_button.clicked.connect(lambda: self.switchToDatabase("NBA"))
        mainMenu_nfl_button.clicked.connect(lambda: self.switchToDatabase("NFL"))
        mainMenu_nhl_button.clicked.connect(lambda: self.switchToDatabase("NHL"))
        mainMenu_mlb_button.clicked.connect(lambda: self.switchToDatabase("MLB"))
        
        #add widgets
        self.mainMenu_frame_layout.addWidget(mainMenu_label)
        self.mainMenu_frame_layout.addWidget(mainMenu_nba_button)
        self.mainMenu_frame_layout.addWidget(mainMenu_nfl_button)
        self.mainMenu_frame_layout.addWidget(mainMenu_nhl_button)
        self.mainMenu_frame_layout.addWidget(mainMenu_mlb_button)
        
        
        
        
    def loadDatabase(self):        
        #declare widgets
        table = QTableWidget()
        load_button = QPushButton("Load")
        self.title = QLabel("Basement")
        topFrame = QFrame()
        topFrame_layout = QHBoxLayout(topFrame)
        mainMenu_button = QPushButton("Main Menu")
        spacer_item = QSpacerItem(100,10, QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Maximum) #space between the main menu button and title
        
        #modify widgets
        mainMenu_button.setFixedWidth(110)
        
        #connect buttons
        mainMenu_button.clicked.connect(lambda: self.switchToMainMenu())
        
        #add widgets
        topFrame_layout.addWidget(mainMenu_button)
        topFrame_layout.addSpacerItem(spacer_item) #space between the main menu button and title
        topFrame_layout.addWidget(self.title)
        self.database_frame_layout.addWidget(topFrame)
        self.database_frame_layout.addWidget(table)
        self.database_frame_layout.addWidget(load_button)
        
        
        
    def switchToMainMenu(self):
        self.stacked_widget.setCurrentIndex(0)
        
    def switchToDatabase(self,name):
        self.resize(700,500)
        self.title.setText(name + " Basement")
        
        #declare/set database
        self.db = dbManager.Database(name.lower()+".db")
        selectResult = self.db.select("Devin Booker", orderBy="date")
        print(selectResult.shape)
        
        #switch frame
        self.stacked_widget.setCurrentIndex(1)
        
        #set up table
        
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