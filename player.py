import pygame
from vehicle import Vehicle

class Player(pygame.sprite.Sprite):
    def __init__(self,name:str,id:int):
        '''
        Parameters:     name:str, id:int
        Funktion:       Initialisierungs-Methode der player-Klasse
        Output:         None
        '''  
        pygame.sprite.Sprite.__init__(self)
        self.__id = id
        self.__lane = "m"
        self.__lives = 3
        self.__fule = 1500
        self.__score = 0
        self.__wrench = 0
        self.__money = 0
        self.__highscore = 0
        self.__allMoney = 0
        self.__playerName = name
        self.__currentCar = 0
        self.__carList = [Vehicle("assets/cars//pickup_u.png",(22,50),[162,650],0,0,"Worktruck","combustion engine"),
                          Vehicle("assets/cars/944.png",(22,50),[162,650],1,2000,"944","combustion engine"),
                          Vehicle("assets/cars/500e.png",(22,50),[162,650],2,2500,"500e","electric engine"),
                          Vehicle("assets/cars/rwb1.png",(22,50),[162,650],3,5000,"RWB1","combustion engine"),
                          Vehicle("assets/cars/musclecar.png",(22,50),[162,650],4,8000,"Muscle","combustion engine"),
                          Vehicle("assets/cars/rwb2.png",(22,50),[162,650],5,10000,"RWB2","combustion engine")]
        self.__availableCarList = [self.__carList[0]]
        self.__carList[0].changeBought(True)
                
    def buyCar(self,carId):
        '''
        Parameters:     carId: int
        Funktion:       "Kauft" das angegeben Auto. Auto wid der Liste der verfügbaren Autos hinzugefügt und Geld wird abgezogen.
        Output:         None
        ''' 
        if not self.__carList[carId] in self.__availableCarList:
            price = self.__carList[carId].getVehicleInfo()[2]
            if self.__allMoney >= price:
                self.__allMoney -= price
                self.__availableCarList.append(self.__carList[carId])
                self.__carList[carId].changeBought(True)
             
    def getCurrentCarInfo(self,carId):
        '''
        Parameters:     carId: int
        Funktion:       Gibt Id, Name, Preis und eine Gekauft Variable von dem durch Id angegebenen Auto zurück.
        Output:         None
        ''' 
        return self.__carList[carId].getVehicleInfo()
    
    def resetAvailableCarList(self):
        '''
        Parameters:     None
        Funktion:       Setzt die gekauften Autos auf Anfang zurück. Ausgelöst durch den Reset Knopf im Main Menu.
        Output:         None
        ''' 
        self.__availableCarList =  [self.__carList[0]]
        for car in self.__carList:
            car.changeBought(False)
        self.__carList[0].changeBought(True)
    
    def getAvailableCarList(self):
        '''
        Parameters:     None
        Funktion:       Gibt Liste der verfügbaren Autos zurück
        Output:         self.__availableCarList: list of Vehicle
        ''' 
        return self.__availableCarList
        
    def loadSave(self,highscore:str,money:str,carList:list):
        '''
        Parameters:     highscore:str, money:str, carList: list of int
        Funktion:       Setzt die Werte für highscore- und money-Attribut des Spielers auf die Parameter. Benutzt wenn Daten aus xml-Speicherstand ausgelesen werden.
        Output:         None
        '''
        self.__highscore = int(highscore)
        self.__allMoney = int(money)
        for car in carList:
            if self.__carList[int(car)] not in self.__availableCarList:
                self.__availableCarList.append(self.__carList[int(car)])
                self.__carList[int(car)].changeBought(True)
        
    def setCurrentCar(self,car:int):
        '''
        Parameters:     car: int
        Funktion:       Setzt das currentCar-Attribut auf den Paramter Wert. Wird benutzt um im Spieler zu speichern, dass ein anderes Auto ausgewählt wurde.
        Output:         None
        '''
        self.__currentCar = car

    def setName(self,newName):
        '''
        Parameters:     newName: str
        Funktion:       Setzt das playerName-Attribut auf den Paramter-Wert.
        Output:         None
        '''
        self.__playerName = newName
     
    def getId(self):
        '''
        Parameters:     None
        Funktion:       Gibt id des Spielers zurück.
        Output:         self.__id: int
        '''
        return self.__id

    def getCurrentCar(self):
        '''
        Parameters:     None
        Funktion:       Gibt __currentCar-Attribut des Spielers zurückt. Gibt an, welches Fahrzeug als index aus der carList ausgewählt ist
        Output:         self.__currentCar: int
        '''
        return self.__currentCar
        
    def getCarList(self):
        '''
        Parameters:     None
        Funktion:       Gibt carList-Attribut des Spielers zurück. 
        Output:         self.__carList: list of Vehicle
        '''
        return self.__carList
        
    def getName(self):
        '''
        Parameters:     None
        Funktion:       Gibt name-Attribut des Spielers zurück. 
        Output:         self.__playerName: str
        '''
        return self.__playerName
    
    def getHighscore(self):
        '''
        Parameters:     None
        Funktion:       Gibt highscore-Attribut des Spielers zurück. 
        Output:         self.__highscore: int
        '''
        return self.__highscore
        
    def getWrench(self):
        '''
        Parameters:     None
        Funktion:       Gibt wrench-Attribut des Spielers zurück. Wrench gibt an, wieviele Schraubenschlüssel der Spieler gesammelt hat.
        Output:         self.__wrench: int
        '''
        return self.__wrench
    
    def getMoney(self,text=False):
        '''
        Parameters:     text: bool (default=False)
        Funktion:       Gibt Geld-Wert des Spielers zurück. Wenn Parameter text True ist dann wird ein String zurückgegeben der eine gekürzte Version des Geld-Wertes enthält.
        Output:         self.__money:int ODER moneyText:str
        '''
        if not text:
            return self.__money
        else:
            money = self.__money      
            if money >= 1000 and money < 9999:
                moneyTxt = str(money/1000)[0:3]+"K"
            elif money >= 9999 and money < 99999:
                moneyTxt = str(money//1000)+"K"
            elif money >= 99999:
                moneyTxt = str(money//10000)+"ZK"
            else:
                moneyTxt = str(money)
            return moneyTxt
    
    def getTotalMoney(self,text=False):
        '''
        Parameters:     text: bool (default=False)
        Funktion:       Gibt insgesamten Geld-Wert des Spielers zurück. Wenn Parameter text True ist dann wird ein String zurückgegeben der eine gekürzte Version des insgesamten Geld-Wertes enthält.
        Output:         self.__money:int ODER moneyText:str
        '''
        if not text:
            return self.__allMoney
        else:
            money = self.__allMoney      
            if money >= 1000 and money < 9999:
                moneyTxt = str(money/1000)[0:3]+"K"
            elif money >= 9999 and money < 99999:
                moneyTxt = str(money//1000)+"K"
            elif money >= 99999:
                moneyTxt = str(money//10000)+"ZK"
            else:
                moneyTxt = str(money)
            return moneyTxt
        
    def getLives(self):
        '''
        Parameters:     None
        Funktion:       Gibt leben-Attribut des Spielers zurück. 
        Output:         self.__lives:int
        '''
        return self.__lives
    
    def getScore(self):
        '''
        Parameters:     None
        Funktion:       Gibt score-Attribut des Spielers zurück. 
        Output:         self.__score:int
        '''
        return self.__score
    
    def getFule(self):
        '''
        Parameters:     None
        Funktion:       Gibt fule-Attribut des Spielers zurück. Fule gibt an wieviele Sprit das Spieler-Auto noch hat. Ist der Wert 0 ist der Run beendet.
        Output:         self.__fule:int
        '''
        return self.__fule
    
    def incFule(self):
        '''
        Parameters:     None
        Funktion:       Erhöht das fule-Attribut um 100. Ausgelöst wenn das Spieler-Fahrzeug einen Benzin Kanister "einsammelt".
        Output:         None
        '''
        self.__fule += 100
        
    def incWrench(self):
        '''
        Parameters:     None
        Funktion:       Erhöht das wrench-Attribut um 1. Ausgelöst wenn das Spieler-Fahrzeug einen Schraubenschlüssel "einsammelt".
        Output:         None
        '''
        self.__wrench += 1
  
    def incMoneyBy(self,increase):
        '''
        Parameters:     None
        Funktion:       Erhöht das fule-Attribut um Parameter increase. Ausgelöst wenn das Spieler-Fahrzeug einen Geldschein "einsammelt" oder sonst Geld "verdient".
        Output:         None
        '''
        self.__money += increase
        
    def schaden(self):
        '''
        Parameters:     None
        Funktion:       Verringert das leben-Attribut um 1. Ausgelöst wenn das Spieler-Fahrzeug schaden nimmt zB bei Kollision mit einem anderen Auto.
        Output:         None
        '''
        self.__lives -= 1
    
    def checkEnd(self):
        '''
        Parameters:     None
        Funktion:       Prüft, ob ein Run beendet ist. Ist das der Fall wird das highscore- und allMoney-Attribut aktualisiert. Ist der Run beendet wird True zurückgegeben, ansonsten False.
        Output:         bool
        '''
        if self.__fule <= 0 or self.__lives <= 0:
            if int(self.__highscore) < self.__score//50:
                self.__highscore = self.__score//50
            self.__allMoney += self.__money
            return True
        else:
            return False 
    
    def endRun(self):
        '''
        Parameters:     None
        Funktion:       Setzt Attribute des Spielers auf Anfangszustand zurück und legt die Positon wieder auf die im Main Menü geforderte fest.
        Output:         None
        '''
        self.__score = 0
        self.__money = 0
        self.__lives = 3
        self.__wrench = 0
        self.__fule = 1500
        self.__lane = "m"
        dim = self.__carList[self.__currentCar].getDimensions()
        self.__carList[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
        
    def update(self, oberflaeche):
        '''
        Parameters:     None
        Funktion:       Wird pro Durchgang der mainloop einmal ausgelöst und aktualisiert Werte des Spieler-Fahrzeugs und malt das Fahrzeug neu auf das Spielefenster. Wird außerdem 
                        benutzt um Schraubenschlüssel zu "benutzen" wenn 10 vorhanden sind um ein Leben zu "heilen".
        Output:         None
        '''
        oberflaeche.blit(self.__carList[self.__currentCar].getImage(),self.__carList[self.__currentCar].getImageRect())
        self.__fule -= 1
        self.__score += 1
        self.__money += 1
        if self.__wrench >= 10 and self.__lives !=3:
            self.__wrench -= 10
            self.__lives += 1
        
    def bewegung(self,bewegung):
        '''
        Parameters:     bewegung: str
        Funktion:       Verändert die Position und das lane-Attribut des Spielers in Abhängigkeit der Bewegungsrichtung
        Output:         None
        '''
        if bewegung == "links":
            if not self.__lane == "l":
                self.__carList[self.__currentCar].rect.x -= 80
                if self.__lane == "m":
                    self.__lane = "l"
                else: 
                    self.__lane = "m"
        if bewegung == "rechts":
            if not self.__lane == "r":
                self.__carList[self.__currentCar].rect.x += 80
                if self.__lane == "m":
                    self.__lane = "r"
                else: 
                    self.__lane = "m"

        
    