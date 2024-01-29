import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QFrame
from PyQt6.QtWidgets import QSizePolicy, QLabel, QStackedWidget, QSpacerItem, QCheckBox
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
        self.table = QTableWidget()
        load_button = QPushButton("Load")
        self.title = QLabel("Basement")
        
        #check buttons
        cbtn_date = QCheckBox("Date")
        cbtn_pos = QCheckBox("Pos")
        cbtn_team = QCheckBox("Team")
        cbtn_location = QCheckBox("Location")
        cbtn_opp = QCheckBox("OPP")
        cbtn_score = QCheckBox("Score")
        cbtn_duration = QCheckBox("Time")
        cbtn_FGM = QCheckBox("FGM")
        cbtn_FGA = QCheckBox("FGA")
        cbtn_FGP = QCheckBox("FGP")
        cbtn_3PM = QCheckBox("3PM")
        cbtn_3PA = QCheckBox("3PA")
        cbtn_3PP = QCheckBox("3PP")
        cbtn_FTM = QCheckBox("FTM")
        cbtn_FTA = QCheckBox("FTA")
        cbtn_FTP = QCheckBox("FTP")
        cbtn_OREB = QCheckBox("OREB")
        cbtn_DREB = QCheckBox("DREB")
        cbtn_REB = QCheckBox("REB")
        cbtn_AST = QCheckBox("AST")
        cbtn_STL = QCheckBox("STL")
        cbtn_BLK = QCheckBox("BLK")
        cbtn_TOV = QCheckBox("TOV")
        cbtn_PF = QCheckBox("PF")
        cbtn_PTS = QCheckBox("PTS")
        cbtn_impact = QCheckBox("+/-")
   
        
        self.check_btn_list = [cbtn_date,cbtn_pos,cbtn_team,cbtn_location,cbtn_opp,cbtn_score,
                               cbtn_duration,cbtn_FGM,cbtn_FGA,cbtn_FGP,cbtn_3PM,cbtn_3PA,
                               cbtn_3PP,cbtn_FTM,cbtn_FTA,cbtn_FTP,cbtn_OREB,cbtn_DREB,cbtn_REB,
                               cbtn_AST,cbtn_STL,cbtn_BLK,cbtn_TOV,cbtn_PF,cbtn_PTS,cbtn_impact]
        
        
        #frames
        mainFrame = QFrame()
        mainFrame_layout_H = QHBoxLayout(mainFrame)
        leftFrame = QFrame()
        leftFrame_layout_V = QVBoxLayout(leftFrame)
        rightFrame = QFrame()
        rightFrame_layout_V = QVBoxLayout(rightFrame)
        rightFrame2 = QFrame()
        rightFrame2_layout_V = QVBoxLayout(rightFrame2)
        topLeftFrame = QFrame()
        topLeftFrame_layout = QHBoxLayout(topLeftFrame)
        botLeftFrame = QFrame()
        botLeftFrame_layout = QVBoxLayout(botLeftFrame)
        
        
        mainMenu_button = QPushButton("Main Menu")
        spacer_item = QSpacerItem(100,10, QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Maximum) #space between the main menu button and title
        
        #modify widgets
        mainMenu_button.setFixedWidth(110)
        
        #connect buttons
        mainMenu_button.clicked.connect(lambda: self.switchToMainMenu())
        load_button.clicked.connect(lambda: self.loadTable())
        
        #add widgets
        #left Frame
        topLeftFrame_layout.addWidget(mainMenu_button)
        topLeftFrame_layout.addSpacerItem(spacer_item) #space between the main menu button and title
        topLeftFrame_layout.addWidget(self.title)
        botLeftFrame_layout.addWidget(load_button)
        self.database_frame_layout.addWidget(mainFrame)
        mainFrame_layout_H.addWidget(leftFrame)
        leftFrame_layout_V.addWidget(topLeftFrame)
        leftFrame_layout_V.addWidget(self.table)
        leftFrame_layout_V.addWidget(botLeftFrame)
        
        #right frame. Add check list buttons
        mainFrame_layout_H.addWidget(rightFrame)
        rightFrame_layout_V.addSpacerItem(QSpacerItem(10,40, QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Minimum))
        for indx in range(13):
            self.check_btn_list[indx].toggle()
            rightFrame_layout_V.addWidget(self.check_btn_list[indx])
        
        mainFrame_layout_H.addWidget(rightFrame2)
        rightFrame2_layout_V.addSpacerItem(QSpacerItem(10,40, QSizePolicy.Policy.Maximum,QSizePolicy.Policy.Minimum))
        for indx in range(13,26):
            self.check_btn_list[indx].toggle()
            rightFrame2_layout_V.addWidget(self.check_btn_list[indx])
        
        
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
        defaultHeaderLabels = ["Date", "Position","Team","vs/@","Opp","Score",
                               "Time", "FGM", "FGA", "FGP", "3PM", "3PA", "3PP",
                               "FTM", "FTA","FTP", "OREB","DREB","REB","AST", "STL", "BLK", "TOV",
                               "PF", "PTS", "+/-"]
        self.table.setRowCount(selectResult.shape[0])
        self.table.setColumnCount(selectResult.shape[1])
        self.table.setHorizontalHeaderLabels(defaultHeaderLabels)
        for r in range(selectResult.shape[0]):
            for c in range(selectResult.shape[1]):
                tableItem = QTableWidgetItem(str(selectResult[r,c]))
                self.table.setItem(r,c,tableItem)
    
    #load table based on setting
    def loadTable(self):
        sql_column_names = ["date", "position","team","location","opponent","scoreDifference",
                               "duration", "FGM", "FGA", "FGPercentage", "ThreePM", "ThreePA", "ThreePPercentage",
                               "FTM", "FTA","FTPercetange", "OREB","DREB","REB","AST", "STL", "BLK", "TOV",
                               "PF", "PTS", "impact"]
        headerLabels = []
        #check check buttons
        for i, btn in enumerate(self.check_btn_list):
            if btn.isChecked():
                sql_column_names.append(sql_column_names[i])
                headerLabels.append(str(btn.text()))
                
        
        #generate select statment
        selectResult = self.db.select("Devin Booker", select= ",".join(str(e) for e in sql_column_names[26:]), orderBy="date")
        print(selectResult)

        
        #set table
        self.setTable(headerLabels,selectResult)
                
        print(headerLabels)
    
    #Set table
    def setTable(self,headerLabels:list,matrix):
        self.table.clear()
        self.table.setColumnCount(len(headerLabels))
        self.table.setRowCount(matrix.shape[0])
        self.table.setHorizontalHeaderLabels(headerLabels)
        for r in range(matrix.shape[0]):
            for c in range(matrix.shape[1]):
                tableItem = QTableWidgetItem(str(matrix[r,c]))
                self.table.setItem(r,c,tableItem)
                        
        
        
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