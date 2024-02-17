class MenuManager(object):
    def __init__(self):
        '''
        Parameters:     None
        Funktion:       Initialisierungs-Methode der MenuManager-Klasse
        Output:         None
        '''
        self.__mainMenu = True
        self.__endMenu = False
        self.__creditsMenu = False
        self.__leaderboardMenu = False
        
    def setMainMenu(self,bool):
        '''
        Parameters:     bool: bool
        Funktion:       Setzt das mainMenu-Attribut auf den angegeben bool-Wert.
        Output:         None
        '''
        self.__mainMenu = bool
        
    def setEndMenu(self,bool):
        '''
        Parameters:     bool: bool
        Funktion:       Setzt das endMenu-Attribut auf den angegeben bool-Wert.
        Output:         None
        '''
        self.__endMenu = bool
        
    def setCreditsMenu(self,bool):
        '''
        Parameters:     bool: bool
        Funktion:       Setzt das creditsMenu-Attribut auf den angegeben bool-Wert.
        Output:         None
        '''
        self.__creditsMenu = bool
        
    def setLeaderboardMenu(self,bool):
        '''
        Parameters:     bool: bool
        Funktion:       Setzt das leaderboardMenu-Attribut auf den angegeben bool-Wert.
        Output:         None
        '''
        self.__leaderboardMenu = bool
        
    def getMainMenu(self):
        '''
        Parameters:     None
        Funktion:       Gibt mainMenu-Attribut zurück. Attribut ist dafür zuständig um Menü anzuhalten
        Output:         self.__mainMenu: bool
        '''
        return self.__mainMenu 
        
    def getEndMenu(self):
        '''
        Parameters:     None
        Funktion:       Gibt endMenu-Attribut zurück. Attribut ist dafür zuständig um Menü anzuhalten
        Output:         self.__endMenu: bool
        '''
        return self.__endMenu
        
    def getCreditsMenu(self):
        '''
        Parameters:     None
        Funktion:       Gibt creditsMenu-Attribut zurück. Attribut ist dafür zuständig um Menü anzuhalten
        Output:         self.__creditsMenu: bool
        '''
        return self.__creditsMenu 
        
    def getLeaderboardMenu(self):
        '''
        Parameters:     None
        Funktion:       Gibt leaderboardMenu-Attribut zurück. Attribut ist dafür zuständig um Menü anzuhalten
        Output:         self.__leaderboardMenu: bool
        '''
        return self.__leaderboardMenu