osterPageExtension = doc.find(string=" Roster ").parent['href']
        # rosterWebpage = requests.get(mainPageUrl+rosterPageExtension)
        # doc = BeautifulSoup(rosterWebpage.text,"html.parser")
        # playerPosition = doc.find(string=f" {playerName} ").parent.parent.parent.parent.find_all("td")[2].find("span").string