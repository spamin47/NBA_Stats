import sqlite3
import numpy
db_dict ={
    "dbName":"nba.db"
}

class Database:
    
    db_connection:sqlite3.Connection = None
    name = None
    
    #create a database object and connect to a sql database by name
    def __init__(self,name:str) -> None: #name: nba.db
        self.name = name.replace(" ", "_")
        self.db_connection = sqlite3.connect(name)
    
    def createTable(self, table_name: str):
        c = self.getCursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name.replace(" ","_")}(
                date DATE NOT NULL PRIMARY KEY, 
                position TEXT NOT NULL,
                team TEXT NOT NULL, 
                location TEXT NOT NULL,
                opponent TEXT NOT NULL, 
                scoreDifference INT NOT NULL, 
                duration DOUBLE NOT NULL, 
                FGM INT NOT NULL, 
                FGA INT NOT NULL,  
                FGPercentage DOUBLE NOT NULL, 
                ThreePM INT NOT NULL,
                ThreePA INT NOT NULL,
                ThreePPercentage DOUBLE NOT NULL,
                FTM INT NOT NULL,
                FTA INT NOT NULL,
                FTPercetange DOUBLE NOT NULL,
                OREB INT NOT NULL,
                DREB INT NOT NULL,
                REB INT NOT NULL,
                AST INT NOT NULL,
                STL INT NOT NULL,
                BLK INT NOT NULL,
                TOV INT NOT NULL,
                PF INT NOT NULL,
                PTS INT NOT NULL,
                impact INT NOT NULL
                );
                ''')
    def dropTable(self, table_name: str):
        c = self.getCursor()
        c.execute(f'''DROP TABLE IF EXISTS {table_name.replace(" ","_")};''')
        
    def insertIntoPlayerTable(self, table_name: str, inputs: list):
        c = self.getCursor()
        insertStmt = f'''INSERT OR IGNORE INTO {table_name.replace(" ","_")} VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        #datatype conversion
        inputs[0] = inputs[0][:-9] #dates
        inputs[5] = int(inputs[5]) #score difference
        if type(inputs[6]) ==type(None): #duration
            inputs[6] = 0
        inputs[6] = round(float(inputs[6]),2)
        inputs[7] = int(inputs[7]) #field goal made
        inputs[8] = int(inputs[8]) #field goal attempted
        if type(inputs[9]) ==type(None): #field goal percentage
            inputs[9] = 0
        inputs[9] = round(float(inputs[9]),2) 
        inputs[10] = int(inputs[10]) #Three pointers made
        inputs[11] = int(inputs[11]) #Three pointers attempted
        if type(inputs[12]) ==type(None): #Three pointers percentage
            inputs[12] = 0
        inputs[12] = round(float(inputs[12]),2)
        inputs[13] = int(inputs[13]) #free throws made
        inputs[14] = int(inputs[14]) #free throws attempted
        if type(inputs[15]) ==type(None): #free throws percentage
            inputs[15] = 0
        inputs[15] = round(float(inputs[15]),2) 
        inputs[16] = int(inputs[16]) #offensive rebounds
        inputs[17] = int(inputs[17]) #defensive rebounds
        inputs[18] = int(inputs[18]) #rebounds
        inputs[19] = int(inputs[19]) #assists
        inputs[20] = int(inputs[20]) #steals
        inputs[21] = int(inputs[21]) #blocks
        inputs[22] = int(inputs[22]) #turnovers
        inputs[23] = int(inputs[23]) #personal fouls
        inputs[24] = int(inputs[24]) #points
        inputs[25] = int(inputs[25]) #impact
        c.execute(insertStmt,tuple(inputs))
    
    def getCursor(self) -> sqlite3.Cursor:
        return  self.db_connection.cursor()
    def getConnection(self) -> sqlite3.Connection:
        return self.db_connection
    def commit(self):
        self.db_connection.commit()
        
    #Select and Query from table
    def selectALLfrom(self,table_name:str) -> numpy.ndarray:
        c = self.getCursor()
        c.execute(f'''SELECT * FROM {table_name.replace(" ","_")}''')
        results = c.fetchall()
        return numpy.asarray(results)
    
    def select(self, fromTable:str, select = "*", orderBy = "") -> numpy.ndarray:
        if orderBy.strip():
            orderBy = "ORDER BY " + orderBy
        else:
            orderBy = ""
        
        selectStatement = f'''SELECT {select} FROM {fromTable.replace(" ","_")} {orderBy}'''
        print("executing", selectStatement)
        c = self.getCursor()
        c.execute(selectStatement)
        
        results = c.fetchall()
        return numpy.asarray(results)
    
    # def select(self, selectStmt:str) -> numpy.ndarray:
    #     c = self.getCursor()
    #     c.execute(f'''{selectStmt}''')
    #     results = c.fetchall()
    #     return numpy.asarray(results)
    
# db = Database("nba.db")

# selectResult = db.select("Devin Booker", orderBy="date")
# print(selectResult.shape)