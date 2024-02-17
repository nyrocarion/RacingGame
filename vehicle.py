import pygame

class Vehicle(pygame.sprite.Sprite):
    def __init__(self,filepath:str,dimensions:tuple,position:list,id:int,price:int,name:str,type:str):
        '''
        Parameters:     filepath:str, dimensions:tuple, position:list, id:int, price:int, name:str
        Funktion:       Initialisierungs-Methode der vehicle-Klasse
        Output:         None
        '''   
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load(filepath)
        self.rect = self.__image.get_rect(size=dimensions,topleft=(position[0],position[1]))
        self.__vehicleName = name
        self.__vehicleId = id
        self.__vehiclePrice = price
        self.__bought = False
        self.__type = type
        
    def getType(self):
        '''
        Parameters:     None
        Funktion:       Gibt das type-Attribut zurück. 
        Output:         self.__type: str
        ''' 
        return self.__type
        
    def changeBought(self,value):
        '''
        Parameters:     value: bool
        Funktion:       Setzt das bought-Attribut auf den bool value Parameter. 
        Output:         None
        ''' 
        self.__bought = value
        
    def getBought(self):
        '''
        Parameters:     None
        Funktion:       Gibt das bought-Attribut zurück. 
        Output:         self.__bought: bool
        ''' 
        return self.__bought
        
    def getVehicleInfo(self):
        '''
        Parameters:     None
        Funktion:       Gibt Informationen über das Fahrzeug zurück.
        Output:         self.__vehicleId: int,self.__vehicleName:,self.__vehiclePrice,self.__bought
        ''' 
        return (self.__vehicleId,self.__vehicleName,self.__vehiclePrice,self.__bought,self.__type)
        
    def getDimensions(self):
        '''
        Parameters:     None
        Funktion:       Gibt Dimensionen des Fahrzeugs Vierecks in einem Tuple in (x,y) Koordinaten Form zurück.
        Output:         self.rect.size: tuple
        '''
        return (self.rect.size)
        
    def getImage(self):
        '''
        Parameters:     None
        Funktion:       Gibt Sprite (Bild) des Spieler-Fahrzeugs zurück.
        Output:         self.__image: pygame.surface.Surface
        '''
        return self.__image
    
    def getImageRect(self):
        '''
        Parameters:     None
        Funktion:       Gibt Viereck des Spieler-Fahrzeugs zurück. Das Bild des Spieler-Fahrzeugs wird mithilfe des Vierecks auf das Spielefenster "gemalt".
        Output:         self.rect: pygame.rect.Rect
        '''   
        return self.rect
    
    def setPos(self,position:list): 
        '''
        Parameters:     position: list
        Funktion:       Legt die Position des Fahrzeug Vierecks fest. Kontrolliert also die Grafische Darstellung des Spieler Fahrzeugs. Position ist die "obere linke Ecke" des Vierecks.
        Output:         None
        '''
        self.rect.x = position[0]
        self.rect.y = position[1]
        
