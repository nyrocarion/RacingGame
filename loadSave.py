from xml.dom.minidom import *
import os

class LoadSave(object):
    def __init__(self,main):
        '''
        Parameters:     main: Main
        Funktion:       Initialisierungs-Methode der loadSave-Klasse
        Output:         None
        '''  
        self.__main = main
        
    def getStartList(self):
        '''
        Parameters:     None
        Funktion:       Dient dazu aus den xml Speicherdateien die Namen und Ids der Spieler auszulesen um die SpielerList zu füllen. Output ist eine Liste mit Elementen der 
                        Struktur [name,id]
        Output:         playerList: list of List
        '''   
        playerList = []
        for save in os.listdir("spielstaende"):
            xmlText = parse("spielstaende/"+save)
            playerTag =  xmlText.getElementsByTagName("spieler")[0]
            playerName = playerTag.getElementsByTagName("name")[0].childNodes[0].nodeValue
            playerId = playerTag.getElementsByTagName("id")[0].childNodes[0].nodeValue
            playerList.append([playerName,playerId])
        return playerList
    
    def getMaxId(self):
        '''
        Parameters:     None
        Funktion:       Gibt maximale vergeben id aus dem Speicherständen aus. Wenn kein Speicherstand vorhanden ist wird -1 zurückgegeben.
        Output:         int
        '''  
        if len(os.listdir("spielstaende")) == 0:
            return -1
        letzterSafe = os.listdir("spielstaende")[-1]
        xmlText = parse("spielstaende/"+letzterSafe)
        playerTag =  xmlText.getElementsByTagName("spieler")[0]
        playerId = playerTag.getElementsByTagName("id")[0].childNodes[0].nodeValue
        return int(playerId)
        
    def deleteSave(self,id):
        '''
        Parameters:     id: int
        Funktion:       Löscht den durch die id angegeben Spieler aus der Spielerliste und ebenfalls den dazugehörigen xml-Speicherstand
        Output:         None
        '''  
        for save in os.listdir("spielstaende"):
            xmlText = parse("spielstaende/"+save)
            playerTag = xmlText.getElementsByTagName("spieler")[0]
            idXML = playerTag.getElementsByTagName("id")[0].childNodes[0].nodeValue
            if str(id) == idXML:
                path = "spielstaende/"+save
                os.remove(path)
        
    def toXML(self,id):
        '''
        Parameters:     id: int
        Funktion:       Erstellt für den durch die id angegebenen Spieler einen Speicherstand im xml Format und speichert diesen.
        Output:         None
        '''  
        for player in self.__main.playerManager.getPlayerList():
            if player.getId() == id:
                text = "<spielstand>"
                text += "<spieler>"
                text += "<id>" + str(id) + "</id>"
                text += "<name>" + player.getName() + "</name>"
                text += "<geld>" + str(player.getTotalMoney()) + "</geld>"
                text += "<highscore>" + str(player.getHighscore()) + "</highscore>"
                text += "<cars>"
                for car in player.getAvailableCarList():
                    text += "<car>"
                    text += "<carid>" + str(car.getVehicleInfo()[0]) + "</carid>"
                    text += "</car>"
                text += "</cars>"
                text += "</spieler>"
                text += "</spielstand>"
                file = open("spielstaende/spielstand_"+str(id)+".xml","w")
                file.write(text)
                file.close
    
    def fromXML(self,id):
        '''
        Parameters:     id: int
        Funktion:       Liest für den durch die id angegebenen Spieler einen Speicherstand im xml Format aus und gibt eine List aus Werten des Spielers zurück.
        Output:         [highscore:str ,money:str ,playerName:str, carList: list of int]
        '''  
        for save in os.listdir("spielstaende"):
            xmlText = parse("spielstaende/"+save)
            player = xmlText.getElementsByTagName("spieler")[0]
            idXML = player.getElementsByTagName("id")[0].childNodes[0].nodeValue
            if str(id) == idXML:
                money = player.getElementsByTagName("geld")[0].childNodes[0].nodeValue
                highscore = player.getElementsByTagName("highscore")[0].childNodes[0].nodeValue
                playerName = player.getElementsByTagName("name")[0].childNodes[0].nodeValue
                carList = []
                for car in player.getElementsByTagName("carid"):
                    carList.append(car.childNodes[0].nodeValue)
                    
                return [highscore,money,playerName,carList]
    
    def resetXML(self,id):
        '''
        Parameters:     id: int
        Funktion:       Überschreibt für den durch die id angegebenen Spieler den Speicherstand im xml Format mit 0 für alle Werte und speichert diesen.
        Output:         None
        '''  
        for save in os.listdir("spielstaende"):
            xmlText = parse("spielstaende/"+save)
            playerTag = xmlText.getElementsByTagName("spieler")[0]
            idXML = playerTag.getElementsByTagName("id")[0].childNodes[0].nodeValue
            if str(id) == idXML:
                for player in self.__main.playerManager.getPlayerList():
                    if player.getId() == id:
                        text = "<spielstand>"
                        text += "<spieler>"
                        text += "<name>" + player.getName() + "</name>"
                        text += "<id>" + str(id) + "</id>"
                        text += "<geld>" + str(0) + "</geld>"
                        text += "<highscore>" + str(0) + "</highscore>"
                        text += "<cars>"
                        car = player.getAvailableCarList()[0]
                        text += "<car>"
                        text += "<carid>" + str(car.getVehicleInfo()[0]) + "</carid>"
                        text += "</car>"
                        text += "</cars>"
                        text += "</spieler>"
                        text += "</spielstand>"
                        file = open("spielstaende/spielstand_"+str(id)+".xml","w")
                        file.write(text)
                        file.close
        
    def __buildScoreboard(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Liste mit Elementen der Struktur [name,highscore] aus allen verfügbaren xml-Speicherständen. Liste ist aufsteigend nach Highscore geordnet.
        Output:         outputList: list of list
        '''  
        outputList = []
        for save in os.listdir("spielstaende"):
            element = []
            xmlText = parse("spielstaende/"+save)
            playerTag = xmlText.getElementsByTagName("spieler")[0]
            element.append(playerTag.getElementsByTagName("name")[0].childNodes[0].nodeValue)
            element.append(playerTag.getElementsByTagName("highscore")[0].childNodes[0].nodeValue)
            outputList.append(element)
        outputList = sorted(outputList, key = lambda x: int(x[1]))
        #outputList.reverse()
        return outputList
    
    def scoreboard(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Liste mit Text der als Zeile des Scoreboards im Leaderboard Screen grafisch angezeigt wird.
        Output:         text: list of str
        '''  
        scorelist = self.__buildScoreboard()
        start = len(str(scorelist[0][0]))
        index = 0
        for element in scorelist:
            if start < len(str(element[0])):
                start = len(str(element[0]))
                index = scorelist.index(element)
        fillUntilName = len(str(scorelist[index][0]))
        fillUntilNumber = len(str(scorelist[-1][1]))
        text = []
        for element in scorelist:
            name =  element[0]
            while len(name) < fillUntilName:
                name = name + " "
            number = str(element[1])
            while len(number) < fillUntilNumber:
                number = "0"+number
            text.append([name," "+number])
        return text