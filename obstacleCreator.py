import pygame
from random import randint, seed, choice

from enemy import Enemy
from animationCreator import AnimationCreator
from item import Item

seed()
 
class ObstacleCreator(object):
    def __init__(self,gameWindow,main):
        '''
        Parameters:     gameWindow: pygame.surface.Surface
        Funktion:       Initialisierungs-Methode der obstacleCreator-Klasse
        Output:         None
        '''  
        self.__gameWindow = gameWindow
        self.__main = main
        
        self.__spriteGroupFule = pygame.sprite.Group()
        self.__spriteGroupVehicle = pygame.sprite.Group()
        self.__spriteGroupWrench = pygame.sprite.Group()
        self.__spriteGroupMoney = pygame.sprite.Group()
        self.__spriteGruppeBattery = pygame.sprite.Group()
        
        self.__counter = 0
        
        self.__animationCreator = AnimationCreator(self.__gameWindow)
        self.__animationCounter = 0
        self.__animationType = ""
        
    def reset(self):
        '''
        Parameters:     None
        Funktion:       Setzt alle Listen mit Hindernissen und Zähler-Attribute für Effekte zurück. Wird ausgelöst, wenn ein Durchgang des Spiels beendet ist.
        Output:         None
        '''  
        self.__counter = 0
        self.__animationCounter = 0
        self.__animationType = ""
        self.__spriteGroupVehicle.empty()
        self.__spriteGroupFule.empty()
        self.__spriteGroupMoney.empty()
        self.__spriteGroupWrench.empty()
        self.__spriteGruppeBattery.empty()
        
    def getCounter(self):
        '''
        Parameters:     None
        Funktion:       Gibt counter-Attribut zurück.
        Output:         self.__counter: id
        '''  
        return self.__counter 
    
    def __newObstacles(self):
        '''
        Parameters:     None
        Funktion:       Erstellt in Abhängigkeit von dem counter-Attribut neue Hindernisse und fügt diese ihrer Sprite-Gruppe hinzu. Danach wird das Hinderniss auf das Spielefenster "gemalt".
        Output:         None
        '''  
        numbers = [0,1,2]
        number = randint(0,2)
        del numbers[number]
        coord = (82+number*80,150)
        if self.__counter % 200 == 0:
            coord2 = (82+choice(numbers)*80,150)
        if self.__counter % 30 == 0:
            self.__spriteGroupVehicle.add(Enemy(coord[0],coord[1]))
            self.__vehicleSpawn()
        if self.__counter % 100 == 0:
            id = self.__main.playerManager.getCurrentPlayer().getCurrentCar()
            if self.__main.playerManager.getCurrentPlayer().getCurrentCarInfo(id)[4]=="combustion engine":
                self.__spriteGroupFule.add(Item((coord[0],coord[1]),(30,30),"assets/items/fule.png"))
                self.__fuleSpawn()
            if self.__main.playerManager.getCurrentPlayer().getCurrentCarInfo(id)[4]=="electric engine":
                self.__spriteGroupFule.add(Item((coord[0],coord[1]),(30,30),"assets/items/battery.png"))
                self.__batterySpawn()
        if self.__counter % 200 == 0:
            self.__spriteGroupWrench.add(Item((coord2[0],coord2[1]),(30,30),"assets/items/wrench.png"))
            self.__wrenchSpawn()
        if self.__counter % 950 == 0:
            self.__spriteGroupMoney.add(Item((coord[0],coord[1]),(30,14),"assets/items/money2.png",736))
            self.__moneySpawn()
            
    def __batterySpawn(self):
        for battery in self.__spriteGruppeBattery:
            self.__gameWindow.blit(battery.getImage(),battery.getRect())
        
    def __fuleSpawn(self):
        '''
        Parameters:     None
        Funktion:       "Malt" alle Sprites aus self.__spriteGroupFule auf das Spielefenster.
        Output:         None
        '''  
        for fule in self.__spriteGroupFule:
            self.__gameWindow.blit(fule.getImage(),fule.getRect())
            
    def __vehicleSpawn(self):
        '''
        Parameters:     None
        Funktion:       "Malt" alle Sprites aus self.__spriteGroupVehicle auf das Spielefenster.
        Output:         None
        '''  
        for vehicle in self.__spriteGroupVehicle:
            self.__gameWindow.blit(vehicle.getImage(),vehicle.getRect())
            
    def __wrenchSpawn(self):
        '''
        Parameters:     None
        Funktion:       "Malt" alle Sprites aus self.__spriteGroupWrench auf das Spielefenster.
        Output:         None
        '''  
        for wrench in self.__spriteGroupWrench:
            self.__gameWindow.blit(wrench.getImage(),wrench.getRect())
            
    def __moneySpawn(self):
        '''
        Parameters:     None
        Funktion:       "Malt" alle Sprites aus self.__spriteGroupMoney auf das Spielefenster.
        Output:         None
        '''  
        for money in self.__spriteGroupMoney:
            self.__gameWindow.blit(money.getImage(),money.getRect())
        
    def update(self):
        '''
        Parameters:     None
        Funktion:       "Malt" die Sprites aller Sprite-Gruppen auf das Spielefenster, solange sie sich über einer y-Koordinatengrenze befinden (bestimmt durch inc.Pos).
        Output:         None
        '''  
        for fule in self.__spriteGroupFule:
            if fule.incPos():
                self.__gameWindow.blit(fule.getImage(),fule.getRect())
        for wrench in self.__spriteGroupWrench:
            if wrench.incPos():
                self.__gameWindow.blit(wrench.getImage(),wrench.getRect())
        for money in self.__spriteGroupMoney:
            if money.incPos():
                self.__gameWindow.blit(money.getImage(),money.getRect())
        for vehicle in self.__spriteGroupVehicle:
            if vehicle.incPos():
                self.__gameWindow.blit(vehicle.getImage(),vehicle.getRect())
                
        self.__counter += 1
        self.__newObstacles()
            
    def collisiondetect(self):
        '''
        Parameters:     None
        Funktion:       Prüft, ob der Spieler-Fahrzeug-Sprite und Sprite-Gruppen der obstacleCreator Klasse überlappen und löst anhand daran grafische Animationen und Veränderungen von 
                        Spieler-Werten aus. Überlappte Sprites werden gelöscht.
        Output:         None
        '''  
        if self.__animationCounter >= 20:
            self.__animationCounter = 0
            self.__animationType = ""
        else:
            if self.__animationType == "damage":
                self.__animationCreator.animationDamage(self.__animationCounter)
            if self.__animationType == "fule":
                self.__animationCreator.animationFule(self.__animationCounter)
            if self.__animationType == "wrench":
                self.__animationCreator.animationWrench(self.__animationCounter) 
            if self.__animationType == "money":
                self.__animationCreator.animationMoney(self.__animationCounter)
        self.__animationCounter += 1         
        player = self.__main.playerManager.getCurrentPlayer()
        if pygame.sprite.spritecollide(player.getCarList()[player.getCurrentCar()],self.__spriteGroupFule,True):
            self.__main.playerManager.getCurrentPlayer().incFule()
            self.__main.playerManager.getCurrentPlayer().incMoneyBy(50)
            self.__animationCreator.animationFule(self.__animationCounter)
            self.__animationCounter = 1    
            self.__animationType = "fule"
        if pygame.sprite.spritecollide(player.getCarList()[player.getCurrentCar()],self.__spriteGroupWrench,True):
            self.__main.playerManager.getCurrentPlayer().incWrench()
            self.__main.playerManager.getCurrentPlayer().incMoneyBy(100)
            self.__animationCreator.animationWrench(self.__animationCounter)
            self.__animationCounter = 1            
            self.__animationType = "wrench"
        if pygame.sprite.spritecollide(player.getCarList()[player.getCurrentCar()],self.__spriteGroupVehicle,True):
            self.__main.playerManager.getCurrentPlayer().schaden()
            self.__animationCreator.animationDamage(self.__animationCounter)
            self.__animationCounter = 1            
            self.__animationType = "damage"
        if pygame.sprite.spritecollide(player.getCarList()[player.getCurrentCar()],self.__spriteGroupMoney,True):
            self.__main.playerManager.getCurrentPlayer().incMoneyBy(250)
            self.__animationCreator.animationMoney(self.__animationCounter)
            self.__animationCounter = 1          
            self.__animationType = "money"
