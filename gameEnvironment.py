import pygame

class GameEnvironment(object):
    def __init__(self,main):
        '''
        Parameters:     main: Main
        Funktion:       Initialisierungs-Methode der gameEnvironment-Klasse
        Output:         None
        '''  
        self.__gameWindow = pygame.display.set_mode(size=(1000,800))
        self.__lives = 3
        self.__wrench = 0
        self.__main = main
        
        self.__font = pygame.font.Font("assets/fonts/pixelfont.ttf",40)
        self.__font20 = pygame.font.Font("assets/fonts/pixelfont.ttf",20)
        
    def setGameWindowSize(self,x,y):
        # 350, 800 und 1000, 800
        del(self.__gameWindow)
        self.__gameWindow = pygame.display.set_mode(size=(x,y))

    def getGameWindow(self):
        '''
        Parameters:     None
        Funktion:       Gibt das __gameWindow-Attribut zurück.
        Output:         __gameWindow: pygame.display.Display
        '''
        return self.__gameWindow
    
    def createBackground(self):
        '''
        Parameters:     None
        Funktion:       Erstellt den Hintergrund für das Spiel in der mainloop
        Output:         None
        '''
        # Bilder laden
        self.__bg = pygame.image.load("assets/background/bg.png")
        self.__bg1 = pygame.image.load("assets/background/bg_start.png")
        self.__bgWhole = pygame.rect.Rect((0,0),(1000,800))
        self.__top = pygame.image.load("assets/top/top.png")
        self.__topbg = pygame.rect.Rect((0,0),(1000,150))
        # Rects erstellen
        self.__bgrect1 = self.__bg.get_rect(size=(250,150),topleft=(50,150))
        self.__bgrect2 = self.__bg.get_rect(size=(250,150),topleft=(50,300))
        self.__bgrect3 = self.__bg.get_rect(size=(250,150),topleft=(50,450))
        self.__bgrect4 = self.__bg1.get_rect(size=(250,150),topleft=(50,600))
        self.__topRect = self.__top.get_rect(size=(350,100),topleft=(0,0))
        # Zeichnen
        pygame.draw.rect(self.__gameWindow,"black",self.__bgWhole)
        self.__gameWindow.blit(self.__bg,self.__bgrect1)
        self.__gameWindow.blit(self.__bg,self.__bgrect2)
        self.__gameWindow.blit(self.__bg,self.__bgrect3)
        self.__gameWindow.blit(self.__bg1,self.__bgrect4)
        self.__gameWindow.blit(self.__top,self.__topRect)
        
    def createTop(self):
        '''
        Parameters:     None
        Funktion:       Erstellt den oberen Part mit den Anzeigen für das Spiel in der mainloop
        Output:         None
        '''
        # Bilder laden
        self.__fule0 = pygame.image.load("assets/top/sprit0.png")
        self.__fule1 = pygame.image.load("assets/top/sprit1.png")
        self.__fule2 = pygame.image.load("assets/top/sprit2.png")
        self.__fule3 = pygame.image.load("assets/top/sprit3.png")
        self.__fule4 = pygame.image.load("assets/top/sprit4.png")
        self.__tacho = pygame.image.load("assets/top/tacho.png")
        self.__money = pygame.image.load("assets/top/money1.png")
        # Rects erstellen
        lebenRect1 = pygame.rect.Rect((235,66),(10,4))
        lebenRect2 = pygame.rect.Rect((235,66-12),(10,12))
        lebenRect3 = pygame.rect.Rect((235,66-2*12),(10,12))
        lebenRect4 = pygame.rect.Rect((235,66-3*12),(10,12))
        self.lebenRectList = [lebenRect1,lebenRect2,lebenRect3,lebenRect4]
        self.__fule0Rect = self.__fule0.get_rect(size=(50,50),topleft=(70,25))
        self.__fule1Rect = self.__fule1.get_rect(size=(50,50),topleft=(70,25))
        self.__fule2Rect = self.__fule2.get_rect(size=(50,50),topleft=(70,25))
        self.__fule3Rect = self.__fule3.get_rect(size=(50,50),topleft=(70,25))
        self.__fule4Rect = self.__fule4.get_rect(size=(50,50),topleft=(70,25))
        self.__tachoRect = self.__tacho.get_rect(size=(90,90),topleft=(130,5))
        self.__moneyRect = self.__money.get_rect(size=(50,50),topleft=(10,25))
        wrenchRect1 = pygame.rect.Rect((265,66),(10,4))
        wrenchRect2 = pygame.rect.Rect((265,62),(10,4))
        wrenchRect3 = pygame.rect.Rect((265,58),(10,4))
        wrenchRect4 = pygame.rect.Rect((265,54),(10,4))
        wrenchRect5 = pygame.rect.Rect((265,50),(10,4))
        wrenchRect6 = pygame.rect.Rect((265,46),(10,4))
        wrenchRect7 = pygame.rect.Rect((265,42),(10,4))
        wrenchRect8 = pygame.rect.Rect((265,38),(10,4))
        wrenchRect9 = pygame.rect.Rect((265,34),(10,4))
        wrenchRect10 = pygame.rect.Rect((265,30),(10,4))
        self.__wrenchRectList = [wrenchRect1,wrenchRect2,wrenchRect3,wrenchRect4,wrenchRect5,wrenchRect6,wrenchRect7,wrenchRect8,wrenchRect9,wrenchRect10]
        # Zeichnen
        self.__gameWindow.blit(self.__money,self.__moneyRect)
        pygame.draw.rect(self.__gameWindow,(139,0,0),self.lebenRectList[0])
        for lebenRects in self.lebenRectList:
            if self.lebenRectList.index(lebenRects) > 0:
                pygame.draw.rect(self.__gameWindow,"red",lebenRects)
    
    def updateBackground(self):
        '''
        Parameters:     None
        Funktion:       Updatet den Hintergrund für das Spiel in der mainloop
        Output:         None
        '''
        pygame.draw.rect(self.__gameWindow,"black",self.__bgWhole)
        self.__gameWindow.blit(self.__bg,self.__bgrect1)
        self.__gameWindow.blit(self.__bg,self.__bgrect2)
        self.__gameWindow.blit(self.__bg,self.__bgrect3)
        self.__gameWindow.blit(self.__bg1,self.__bgrect4)
        
    def updateTop(self):
        '''
        Parameters:     None
        Funktion:       Updatet den oberen Part mit den Anzeigen für das Spiel in der mainloop
        Output:         None
        '''
        pygame.draw.rect(self.__gameWindow,"black",self.__topbg)
        self.__gameWindow.blit(self.__top,self.__topRect)
        self.__updateLives()
        self.__updateMoney()
        self.__updateWrench()
        self.__updateFule()
        self.__updateScore()
        
    def __updateLives(self):
        '''
        Parameters:     None
        Funktion:       Updatet die grafische Anzeige für die Leben des Spielers
        Output:         None
        '''
        lives = self.__main.playerManager.getCurrentPlayer().getLives()
        if self.__lives < lives:
            pygame.draw.rect(self.__gameWindow,"red",self.lebenRectList[lives])
            self.__lives = lives
        if self.__lives != lives and lives < 3:
            pygame.draw.rect(self.__gameWindow,(138,132,132),self.lebenRectList[1+lives])
            self.__lives = lives
        if self.__lives == lives:
            for counter in range(self.__lives+1):
                pygame.draw.rect(self.__gameWindow,"red",self.lebenRectList[counter])
            
    def __updateWrench(self):
        '''
        Parameters:     None
        Funktion:       Updatet die grafische Anzeige für die Schraubenschlüssel des Spielers
        Output:         None
        '''
        wrench = self.__main.playerManager.getCurrentPlayer().getWrench()
        if self.__wrench > wrench and wrench < 10:
            for s in range(1,11-wrench,1):
                pygame.draw.rect(self.__gameWindow,(138,132,132),self.__wrenchRectList[-s])
            self.__wrench = wrench
        if self.__wrench != wrench and wrench > 0:
            pygame.draw.rect(self.__gameWindow,(19,95,197),self.__wrenchRectList[wrench%10-1])
            self.__wrench = wrench
        if wrench == 0:
            self.__resetWrench()
        if self.__wrench == wrench:
            for counter in range(self.__wrench):
                pygame.draw.rect(self.__gameWindow,(19,95,197),self.__wrenchRectList[counter%10])
            
    def __resetWrench(self):
        '''
        Parameters:     None
        Funktion:       Färbt alle Vierecke in der wrenchRectList in der Hintergrundfarbe der Anzeige, sodass diese wieder bei Null steht.
        Output:         None
        '''
        for wrenchRect in self.__wrenchRectList:
            pygame.draw.rect(self.__gameWindow,(138,132,132),wrenchRect)
            
    def __updateFule(self):
        '''
        Parameters:     None
        Funktion:       Updatet die grafische Anzeige für den Sprit des Spielers
        Output:         None
        '''
        if self.__main.playerManager.getCurrentPlayer().getFule()>1200:
            self.__gameWindow.blit(self.__fule4,self.__fule4Rect)
        elif self.__main.playerManager.getCurrentPlayer().getFule()>900:
            self.__gameWindow.blit(self.__fule3,self.__fule3Rect)
        elif self.__main.playerManager.getCurrentPlayer().getFule()>600:
            self.__gameWindow.blit(self.__fule2,self.__fule2Rect)
        elif self.__main.playerManager.getCurrentPlayer().getFule()>300:
            self.__gameWindow.blit(self.__fule1,self.__fule1Rect)
        elif self.__main.playerManager.getCurrentPlayer().getFule()==0:
            self.__gameWindow.blit(self.__fule0,self.__fule0Rect)
        else:
            pass
        
    def __updateScore(self):
        '''
        Parameters:     None
        Funktion:       Updatet die grafische Anzeige für den Score des Spielers
        Output:         None
        '''
        score = self.__main.playerManager.getCurrentPlayer().getScore()
        scoreText= self.__font.render(str(score//50), False, "yellow")
        scoreTextRect = scoreText.get_rect(center=(178, 47))
        self.__gameWindow.blit(self.__tacho,self.__tachoRect)
        self.__gameWindow.blit(scoreText, scoreTextRect)
            
    def __updateMoney(self):
        '''
        Parameters:     None
        Funktion:       Updatet die grafische Anzeige für das Geld des Spielers
        Output:         None
        '''
        money = self.__main.playerManager.getCurrentPlayer().getMoney()
        if money >= 1000 and money < 9999:
            moneyTxt = str(money/1000)[0:3]+"K"
        elif money >= 9999 and money < 99999:
            moneyTxt = str(money//1000)+"K"
        elif money >= 99999:
            moneyTxt = str(money//10000)+"ZK"
        else:
            moneyTxt = str(money)
        moneyText= self.__font20.render(moneyTxt, False, "yellow")
        moneyTextRect = moneyText.get_rect(center=(35, 50))
        self.__gameWindow.blit(self.__money,self.__moneyRect)
        self.__gameWindow.blit(moneyText,moneyTextRect)
            
        