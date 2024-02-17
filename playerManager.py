from player import Player

class PlayerManager(object):
    def __init__(self,main):
        '''
        Parameters:     main: Main
        Funktion:       Initialisierungs-Methode der PlayerManager-Klasse
        Output:         None
        '''  
        self.__main = main
        self.__playerList = []
        self.__currentPlayer = None
        self.__idCounter = self.__main.xml.getMaxId()
        
    def getPlayerList(self):
        '''
        Parameters:     None
        Funktion:       Gibt spielerListe zurück.
        Output:         self.__playerList: list of player
        '''
        return self.__playerList
    
    def getCurrentPlayer(self):
        '''
        Parameters:     None
        Funktion:       Gibt (aktuell ausgewählten) Spieler zurück
        Output:         self.__currentPlayer: player
        '''
        return self.__currentPlayer
    
    def setCurrentPlayer(self,index:int):
        '''
        Parameters:     index: int
        Funktion:       Setzt den aktuellen Spieler auf das Element der spielerListe das durch den index angegeben wird.
        Output:         None
        '''
        self.__currentPlayer = self.__playerList[index]
    
    def addPlayerToList(self,player):
        '''
        Parameters:     player: Player
        Funktion:       Fügt der Spielerliste ein Player-Objekt an.
        Output:         None
        '''
        self.__playerList.append(player)
        
    def addNewPlayer(self):
        '''
        Parameters:     None
        Funktion:       Fügt der SpielerList ein neues Spieler-Objekt hinzu. Ein xml-Speicherstand wird erstellt.
        Output:         None
        '''
        self.__idCounter += 1
        num = self.__idCounter%8
        self.__playerList.append(Player("Spieler"+"I"*num,self.__idCounter))
        self.__main.xml.toXML(self.__idCounter)
    
    