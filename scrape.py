from bs4 import BeautifulSoup
import requests
import dbManager
import sqlite3

mainPageUrl = "https://www.statmuse.com"

#Main Player Page
playerPageUrl = "https://www.statmuse.com/nba/player/devin-booker-9301"
PlayerWebpage = requests.get(playerPageUrl) #getting an HTTP GET request for the url
doc = BeautifulSoup(PlayerWebpage.text,"html.parser")

#get Players name
playerName = doc.find('h2').string[1:-1]
print("player: ",playerName, " size: ",len(playerName))
#find stats link
statsTag = doc.findAll(string = "Stats")[0].parent.parent
print(statsTag)
statsPageExtension = statsTag.find("a")['href']
print(statsPageExtension)

#connect to database
print(dbManager.db_dict.get("dbName"))
db = dbManager.Database(dbManager.db_dict.get("dbName"))
db.createTable(playerName)


#Career Stats Page
playerCareerStatsUrl = mainPageUrl +statsPageExtension
print(playerCareerStatsUrl)
playerCareerWebpage = requests.get(playerCareerStatsUrl) #request stats url link
doc = BeautifulSoup(playerCareerWebpage.text,"html.parser")
RegularSeason = doc.find(string = "Regular Season").parent.parent.parent
#traverse through each season
seasons = RegularSeason.findAll('a', {'title' : playerName})
playerPosition = None
for season in seasons:
    
    #Get player position 
    try:
        teamPageExtension = season.parent.parent.findAll("td")[1].find("a")['href']
        teamWebPage = requests.get(mainPageUrl + teamPageExtension)
        doc = BeautifulSoup(teamWebPage.text,"html.parser")
        rosterPageExtension = doc.find(string=" Roster ").parent['href']
        rosterWebpage = requests.get(mainPageUrl+rosterPageExtension)
        doc = BeautifulSoup(rosterWebpage.text,"html.parser")
        playerPosition = doc.find(string=f" {playerName} ").parent.parent.parent.parent.find_all("td")[2].find("span").string
    except:
        print("cannot access link")
    
    
    seasonYearPageExtension = season['href']
    #Season Stats Page
    seasonYearUrl =mainPageUrl+ seasonYearPageExtension 
    # print("\nseason: ",seasonYearUrl)
    seasonWebpage = requests.get(seasonYearUrl)
    doc = BeautifulSoup(seasonWebpage.text, "html.parser")

    tables = doc.findAll('table') #grab table. Each table should represent the month, conference semifinals, first round
    columnNames = tables[0].findAll('th')

    for table in tables:    
        rows = table.findAll("tr")[1:-1]#first and last are the label row and avg row
        for row in rows:
            rowOfData = []
            columns = row.findAll("td")
            for index, column in enumerate(columns):
                rowOfData.append(column.get('data-value'))
                if(index == 0):
                    rowOfData.append(playerPosition[1:-1])
            db.insertIntoPlayerTable(playerName,rowOfData)
            
db.commit()







