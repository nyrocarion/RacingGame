import pygame
import sys

class MenuCreator(object):
    def __init__(self,gameWindow,main):
        '''
        Parameters:     gameWindow: pygame.surface.Surface, main:Main
        Funktion:       Initialisierungs-Methode der menuCreator-Klasse
        Output:         None
        '''  
        self.__gameWindow = gameWindow
        self.__main = main
        self.__currentPlayer = 0
        self.__currentCar = 0
        
        self.__fontTitle = pygame.font.Font("assets/fonts/bluescreen.ttf",90)
        self.__fontValues = pygame.font.Font("assets/fonts/bluescreen.ttf",55)
        self.__fontValuesNumbers = pygame.font.Font("assets/fonts/edundot.ttf",55)
        self.__fontButton = pygame.font.Font("assets/fonts/bluescreen.ttf",45)
        self.__fontMonospace = pygame.font.SysFont("consolas",40)
        self.__fontMonospaceSmall = pygame.font.SysFont("consolas",20)
        self.__fontSmall = pygame.font.Font("assets/fonts/bluescreen.ttf",25)
        
        self.__colorBgDark = (49,10,11)
        self.__colorBgMid = (224,163,135)
        self.__colorBgBright = (185,106,89)
        self.__colorFontMid = (116,58,54)
        self.__colorFontBright = (224,163,135)
        
    def getCurrentPlayer(self):
        '''
        Parameters:     None
        Funktion:       Gibt (aktuell ausgewählten) Spieler als int zurück. Bezieht sich auf den Index der spielerList, nicht auf die wirkliche Spieler Id.
        Output:         self.__aktuellerSpieler: int
        '''  
        return self.__currentPlayer
    
    def getCurrentCar(self):
        '''
        Parameters:     None
        Funktion:       Gibt (aktuell ausgewähltes) Fahrzeug als int zurück. Bezieht sich auf den Index der spielerList, nicht auf die wirkliche Spieler Id.
        Output:         self.__currentCar: int
        '''    
        return self.__currentCar
    
    def leaderboardMenu(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Menü-Screen für das Leaderboard aller xml-Spielstände. Liest "Knopfdrücke" aus und wechselt entsprechend Menüs.
        Output:         None
        '''  
        creditsBgRect = pygame.rect.Rect((0,50),(1000,100))
        creditsText = self.__fontTitle.render("LEADERBOARD",False,(116,58,54))
        creditsTextRect = creditsText.get_rect(center=(500,100))
        
        creditsBgRect = pygame.rect.Rect((50,175),(900,425))
        bottomBgRect = pygame.rect.Rect((0,650),(1000,100))
        
        backButton = pygame.rect.Rect((400,675),(200,50))
        backText = self.__fontButton.render("BACK", False, (224,163,135))
        backTextRect = backText.get_rect(center=(500,700))
        
        clicked = False
        
        while self.__main.menuManager.getLeaderboardMenu():
            self.__gameWindow.fill((49,10,11))
            
            cursorPos = pygame.mouse.get_pos()
            cursorOverBack = False   
            
            if backButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.menuManager.setLeaderboardMenu(False)
                    break
                else:
                    cursorOverBack = True
            # Draw BG
            pygame.draw.rect(self.__gameWindow,(185,106,89),creditsBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),bottomBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),creditsBgRect)

            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,(49,10,11),backButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),backButton)
            # Draw Text
            self.__gameWindow.blit(creditsText,creditsTextRect)    
            self.__gameWindow.blit(backText,backTextRect)
            
            for element in self.__main.xml.scoreboard():
                leaderboardText = self.__fontMonospace.render(element[0]+element[1],False, (224,163,135))
                leaderboardTextRect = leaderboardText.get_rect(topleft = (50,175+self.__main.xml.scoreboard().index(element)*40))
                self.__gameWindow.blit(leaderboardText,leaderboardTextRect)
            
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
            pygame.display.update()
            self.__main.clock.tick(30.0)
        
    def creditsMenu(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Menü-Screen für die Credits. Liest "Knopfdrücke" aus und wechselt entsprechend Menüs.
        Output:         None
        '''  
        creditsBgRect = pygame.rect.Rect((0,50),(1000,100))
        creditsText = self.__fontTitle.render("CREDITS",False,(116,58,54))
        creditsTextRect = creditsText.get_rect(center=(500,100))
        
        creditsLeftText1 = self.__fontButton.render("ALLGEMEIN",False,(224,163,135))
        creditsLeftText2 = self.__fontMonospaceSmall.render("Erstellt von Niklas in ca.45h",False,(224,163,135))
        creditsLeftText3 = self.__fontMonospaceSmall.render("im Rahmen eines Informatikprojekts",False,(224,163,135))
        creditsLeftText4 = self.__fontMonospaceSmall.render("Pixelart selbst erstellt mit",False,(224,163,135))
        creditsLeftText5 = self.__fontMonospaceSmall.render("www.piskelapp.com",False,(224,163,135))
        
        creditsRightText1 = self.__fontButton.render("FONTS",False,(224,163,135))
        creditsRightText2 = self.__fontMonospaceSmall.render("bluescreen.ttf",False,(224,163,135))
        creditsRightText3 = self.__fontMonospaceSmall.render("www.dafont.com/blue-screen.font",False,(224,163,135))
        creditsRightText4 = self.__fontMonospaceSmall.render("pixelfont.ttf",False,(224,163,135))
        creditsRightText5 = self.__fontMonospaceSmall.render("www.dafont.com/minecraft.font",False,(224,163,135))
        creditsRightText6 = self.__fontMonospaceSmall.render("edundot.ttf",False,(224,163,135))
        creditsRightText7 = self.__fontMonospaceSmall.render("www.dafont.com/edit-undo-dot.font",False,(224,163,135))   
        
        creditRLTexts = [creditsLeftText1,creditsLeftText2,creditsLeftText3,creditsLeftText4,creditsLeftText5,creditsRightText1,creditsRightText2,creditsRightText3,creditsRightText4,creditsRightText5,creditsRightText6,creditsRightText7]
        
        creditsLeftText1Rect = creditsLeftText1.get_rect(center=(250,200))
        creditsLeftText2Rect = creditsLeftText2.get_rect(center=(250,250))
        creditsLeftText3Rect = creditsLeftText3.get_rect(center=(250,280))
        creditsLeftText4Rect = creditsLeftText4.get_rect(center=(250,310))
        creditsLeftText5Rect = creditsLeftText5.get_rect(center=(250,340))
        
        
        creditsRightText1Rect = creditsRightText1.get_rect(center=(760,200))
        creditsRightText2Rect = creditsRightText2.get_rect(center=(750,250))
        creditsRightText3Rect = creditsRightText3.get_rect(center=(750,280))
        creditsRightText4Rect = creditsRightText4.get_rect(center=(750,310))
        creditsRightText5Rect = creditsRightText5.get_rect(center=(750,340))
        creditsRightText6Rect = creditsRightText6.get_rect(center=(750,370))
        creditsRightText7Rect = creditsRightText7.get_rect(center=(750,400))
        
        creditsBgRect1 = pygame.rect.Rect((50,175),(400,325))
        creditsBgRect2 = pygame.rect.Rect((550,175),(400,325)) 
        
        creditRLTextRects = [creditsLeftText1Rect,creditsLeftText2Rect,creditsLeftText3Rect,creditsLeftText4Rect,creditsLeftText5Rect,creditsRightText1Rect,creditsRightText2Rect,creditsRightText3Rect,creditsRightText4Rect,creditsRightText5Rect,creditsRightText6Rect,creditsRightText7Rect]
        
        bottomBgRect = pygame.rect.Rect((0,650),(1000,100))
        
        backButton = pygame.rect.Rect((400,675),(200,50))
        backText = self.__fontButton.render("BACK", False, (224,163,135))
        backTextRect = backText.get_rect(center=(500,700))
        
        clicked = False
        
        while self.__main.menuManager.getCreditsMenu():
            self.__gameWindow.fill((49,10,11))#
            
            cursorPos = pygame.mouse.get_pos()
            cursorOverBack = False  
            
            if backButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.menuManager.setCreditsMenu(False) 
                    break
                else:
                    cursorOverBack = True
            #Draw Bg
            pygame.draw.rect(self.__gameWindow,(185,106,89),creditsBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),bottomBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),creditsBgRect1)
            pygame.draw.rect(self.__gameWindow,(116,58,54),creditsBgRect2)
            
            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,(49,10,11),backButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),backButton)
            # Draw Text    
            self.__gameWindow.blit(creditsText,creditsTextRect)    
            self.__gameWindow.blit(backText,backTextRect)
            for text in creditRLTexts:
                self.__gameWindow.blit(text,creditRLTextRects[creditRLTexts.index(text)])
    
            
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
            pygame.display.update()
            self.__main.clock.tick(30.0)
        
    def endMenu(self): 
        '''
        Parameters:     None
        Funktion:       Erstellt eine Menü-Screen für den Review Screen am Ende eines Runs. Liest "Knopfdrücke" aus und wechselt entsprechend Menüs.
        Output:         None
        '''  
        # Create Text and Numbers
        gameoverText = self.__fontTitle.render("-GAME OVER-",False,(116,58,54))
        moneyAllText = self.__fontValues.render("ALL MONEY: ",False,(224,163,135))
        highscoreText = self.__fontValues.render("HIGHSCORE: ",False,(224,163,135))
        moneyText = self.__fontValues.render("MONEY: ",False,(224,163,135))
        scoreText = self.__fontValues.render("SCORE: ",False,(224,163,135))
        
        moneyAllNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,(224,163,135))
        highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,(224,163,135))
        moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getMoney(True)),False,(224,163,135))
        scoreNumber = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getScore()//50
        scoreNumberText = self.__fontValuesNumbers.render(str(scoreNumber),False,(224,163,135))
        # Create Rects
        gameoverBgRect = pygame.rect.Rect((0,50),(1000,100))
        moneyAllBgRect = pygame.rect.Rect((50,175),(400,75))
        highscoreBgRect = pygame.rect.Rect((550,175),(400,75))
        moneyBgRect = pygame.rect.Rect((50,300),(400,75))
        scoreBgRect = pygame.rect.Rect((550,300),(400,75))
        
        gameoverTextRect = gameoverText.get_rect(center=(500,100))
        highscoreTextRect = highscoreText.get_rect(topleft=(560,177))
        moneyAllTextRect = moneyAllText.get_rect(topleft=(60,177))
        moneyTextRect = moneyText.get_rect(topleft=(60,177+125))
        scoreTextRect = scoreText.get_rect(topleft=(560,177+125))
        
        moneyNumberRect = moneyNumberText.get_rect(topright=(440,183+125))
        scoreNumberRect = scoreNumberText.get_rect(topright=(940,183+125))
        highscoreNumberTextRect = highscoreNumberText.get_rect(topright=(940,183))
        moneyAllNumberRect = moneyAllNumberText.get_rect(topright=(440,183))
        
        bottomBgRect = pygame.rect.Rect((0,525),(1000,100))
        bottomBgRect2 = pygame.rect.Rect((0,650),(1000,100))
        
        backButton = pygame.rect.Rect((400,675),(200,50))
        backText = self.__fontButton.render("BACK", False, (224,163,135))
        backTextRect = backText.get_rect(center=(500,700))
        
        creditsButton = pygame.rect.Rect((400,550),(200,50))
        creditsText = self.__fontButton.render("CREDITS", False, (224,163,135))
        creditsTextRect = backText.get_rect(center=(470,575))
        
        clicked = False
        
        while self.__main.menuManager.getEndMenu():
            self.__gameWindow.fill((49,10,11))
            
            cursorPos = pygame.mouse.get_pos()
            cursorOverBack = False
            cursorOverLeaderboard = False
            values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())   
            self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3]) 
            
            if backButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.menuManager.setEndMenu(False)
                    self.__main.menuManager.setMainMenu(True)
                    break
                else:
                    cursorOverBack = True
                    
            if creditsButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.menuManager.setCreditsMenu(True)
                    self.creditsMenu()
                else:
                    cursorOverLeaderboard = True
            # Draw bg
            pygame.draw.rect(self.__gameWindow,(116,58,54),moneyAllBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),highscoreBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),gameoverBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),scoreBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),moneyBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),bottomBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),bottomBgRect2)
            
            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,(49,10,11),backButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),backButton)
                
            if cursorOverLeaderboard:
                pygame.draw.rect(self.__gameWindow,(49,10,11),creditsButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),creditsButton)
            # Draw Text
            self.__gameWindow.blit(highscoreText,highscoreTextRect)
            self.__gameWindow.blit(moneyAllText,moneyAllTextRect)
            self.__gameWindow.blit(moneyText,moneyTextRect)
            self.__gameWindow.blit(scoreText,scoreTextRect)
            self.__gameWindow.blit(gameoverText,gameoverTextRect)
            self.__gameWindow.blit(backText,backTextRect)
            self.__gameWindow.blit(creditsText,creditsTextRect)
            self.__gameWindow.blit(moneyAllNumberText,moneyAllNumberRect)
            self.__gameWindow.blit(highscoreNumberText,highscoreNumberTextRect)
            self.__gameWindow.blit(moneyNumberText,moneyNumberRect)
            self.__gameWindow.blit(scoreNumberText,scoreNumberRect)
            
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
            pygame.display.update()
            self.__main.clock.tick(30.0)
        
    def mainMenu(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Menü-Screen für das Main Menü. Liest "Knopfdrücke" aus und wechselt entsprechend Menüs.
        Output:         None
        '''
        
        values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())   
        self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3]) 
        self.__main.playerManager.getPlayerList()[self.__currentPlayer].setName(values[2])
        self.__main.playerManager.getPlayerList()[self.__currentPlayer].setCurrentCar(self.__currentCar)
        
        rightImage = pygame.image.load("assets/menuSymbols/right.png")
        leftImage = pygame.image.load("assets/menuSymbols//left.png")
        plusImage = pygame.image.load("assets/menuSymbols//plus.png")
        plus1Image = pygame.image.load("assets/menuSymbols//plus1.png")
        minusImage = pygame.image.load("assets/menuSymbols//minus.png")
        minus1Image = pygame.image.load("assets/menuSymbols//minus1.png")

        highscoreText = self.__fontValues.render("HIGHSCORE:",False,(224,163,135))
        highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,(224,163,135))
        moneyText = self.__fontValues.render("MONEY:",False,(224,163,135))
        moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,(224,163,135))
        titleText = self.__fontTitle.render("GAMETITLE",False,(116,58,54))
        startText = self.__fontButton.render("START", False, (224,163,135))
        leaderboardText = self.__fontButton.render("LEADERBOARD", False, (224,163,135))
        creditsText = self.__fontButton.render("CREDITS", False, (224,163,135))
        resetText = self.__fontButton.render("RESET", False, (224,163,135))
        info = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCurrentCarInfo(self.__currentCar)
        moneyValueCarTextCalc = "["+str(info[0])+"] "+info[1]+" - "+str(info[2])+"$"
        moneyValueCarText = self.__fontMonospaceSmall.render(moneyValueCarTextCalc,False,(49,10,11))
        
        titleBgRect = pygame.rect.Rect((0,50),(1000,100))
        moneyBgRect = pygame.rect.Rect((50,175),(400,75))
        highscoreBgRect = pygame.rect.Rect((550,175),(400,75))
        vehicleSelectionBgRect = pygame.rect.Rect((0,275),(1000,350))
        bottomBgRect = pygame.rect.Rect((0,650),(1000,100))
        
        startButton = pygame.rect.Rect((400,550),(200,50))
        leaderboardButton = pygame.rect.Rect((50,675),(250,50))
        creditsButton = pygame.rect.Rect((375,675),(250,50))
        resetButton = pygame.rect.Rect((700,675),(250,50))
        buyButton = pygame.rect.Rect((450,495),(100,25))
        
        playerNameBgRect = pygame.rect.Rect((350,300),(300,50))
        vehicleSelectionImageBgRect = pygame.rect.Rect((350,375),(300,160))
        moneyValueCarBgRect = pygame.rect.Rect((375,390),(250,25))
    
        leftRect1 = leftImage.get_rect(size=(50,50),topleft=(275,300))
        rightRect1 = rightImage.get_rect(size=(50,50),topleft=(675,300))
        leftRect2 = leftImage.get_rect(size=(50,50),topleft=(275,375+55))
        rightRect2 = rightImage.get_rect(size=(50,50),topleft=(675,375+55))
        
        plusRect = plusImage.get_rect(size=(50,50),topleft=(200,300))
        minusRect = minusImage.get_rect(size=(50,50),topleft=(750,300))
        
        highscoreTextRect = highscoreText.get_rect(topleft=(560,177))
        moneyTextRect = moneyText.get_rect(topleft=(60,177))
        highscoreNumberTextRect = highscoreNumberText.get_rect(topright=(940,183))
        moneyNumberTextRect = moneyNumberText.get_rect(topright=(440,183))
        titleTextRect = titleText.get_rect(center=(500,100))
        startTextRect = startText.get_rect(center=(500,575))
        leaderboardTextRect = leaderboardText.get_rect(center=(175,700))
        creditsTextRect = creditsText.get_rect(center=(500,700))
        resetTextRect = resetText.get_rect(center=(825,700))
        moneyValueCarTextRect = moneyValueCarText.get_rect(center=(500,403))
        
        textPlayerName = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getName()
        playerNameInputActive = False
        clicked = False
        
        while self.__main.menuManager.getMainMenu():
            # move Car Sprite to selection area
            self.__currentCar = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCurrentCar()
            dim = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getDimensions()
            self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
            
            info = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCurrentCarInfo(self.__currentCar)
            moneyValueCarTextCalc = "["+str(info[0])+"] "+info[1]+" - "+str(info[2])+"$"
            moneyValueCarText = self.__fontMonospaceSmall.render(moneyValueCarTextCalc,False,(49,10,11))
            if info[3]:
                buybuy = "BOUGHT"
            else:
                buybuy = "BUY"
            
            if not playerNameInputActive:
                textPlayerName = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getName()
            playerNameText = self.__fontButton.render(textPlayerName,False,(224,163,135))
            playerNameTextRect = playerNameText.get_rect(center=(500,325))
            moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,(224,163,135))
            moneyNumberTextRect = moneyNumberText.get_rect(topright=(440,183))
            highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,(224,163,135))
            highscoreNumberTextRect = highscoreNumberText.get_rect(topright=(940,183))
            self.__gameWindow.fill((49,10,11))
            
            cursorPos = pygame.mouse.get_pos()
            cursorOverStart = False
            cursorOverCredits = False
            cursorOverLeaderboard = False
            cursorOverReset = False
            cursorOverPlayerName = False
            cursorOverPlus = False
            cursorOverMinus = False
            cursorOverBuy = False
            
            
            if buyButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].buyCar(self.__currentCar)
                    self.__main.xml.toXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                else:
                    cursorOverBuy = True
            if plusRect.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.addNewPlayer()
                    self.__currentPlayer = -1
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3]) 
                else:
                    cursorOverPlus = True
            if minusRect.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked and len(self.__main.playerManager.getPlayerList())>1:
                    self.__main.xml.deleteSave(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList().remove(self.__main.playerManager.getPlayerList()[self.__currentPlayer])
                    if self.__currentPlayer < 0:
                        self.__currentPlayer = len(self.__main.playerManager.getPlayerList())-self.__currentPlayer-1
                    self.__currentPlayer -= 1
                else:
                    cursorOverMinus = True
            if playerNameBgRect.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    playerNameInputActive = True
                else:
                    cursorOverPlayerName = True
            else:
                playerNameInputActive = False
            if startButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked and self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getVehicleInfo()[3]:
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([162,650])
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].setCurrentCar(self.__currentCar)
                    self.__main.menuManager.setMainMenu(False)
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.laufen = True  
                    #print("mainloop gestarte mit",self.__main.playerManager.getPlayerList()[self.__currentPlayer].getName(),self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCurrentCar())
                    self.__main.mainloop()
                else:
                    cursorOverStart = True
            if leaderboardButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.menuManager.setLeaderboardMenu(True)
                    self.leaderboardMenu()
                else:
                    cursorOverLeaderboard = True
            if creditsButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked: 
                    self.__main.menuManager.setCreditsMenu(True)
                    self.creditsMenu()  
                else:
                    cursorOverCredits = True
            if resetButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.xml.resetXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3])   
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].resetAvailableCarList()
                else:
                    cursorOverReset = True
            if rightRect1.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__currentPlayer += 1
                    self.__currentPlayer = self.__currentPlayer % len(self.__main.playerManager.getPlayerList())
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3]) 
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
            if leftRect1.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__currentPlayer -= 1
                    self.__currentPlayer = self.__currentPlayer % len(self.__main.playerManager.getPlayerList())
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3]) 
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
            if leftRect2.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__currentCar -= 1
                    self.__currentCar = self.__currentCar % len(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].setCurrentCar(self.__currentCar)
                    dim = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getDimensions()
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
            if rightRect2.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__currentCar += 1
                    self.__currentCar = self.__currentCar % len(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].setCurrentCar(self.__currentCar)
                    dim = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getDimensions()
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].setPos([350+(300-dim[0])/2,375+(160-dim[1])/2])
            if textPlayerName != self.__main.playerManager.getPlayerList()[self.__currentPlayer].getName() and playerNameInputActive:
                self.__main.playerManager.getPlayerList()[self.__currentPlayer].setName(textPlayerName)
                self.__main.xml.toXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
            # Draw bg
            pygame.draw.rect(self.__gameWindow,(185,106,89),titleBgRect) 
            pygame.draw.rect(self.__gameWindow,(116,58,54),moneyBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),highscoreBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),vehicleSelectionBgRect)
            pygame.draw.rect(self.__gameWindow,(116,58,54),vehicleSelectionImageBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),moneyValueCarBgRect)
            pygame.draw.rect(self.__gameWindow,(185,106,89),bottomBgRect)

            if cursorOverBuy and not info[3]:
                pygame.draw.rect(self.__gameWindow,(49,10,11),buyButton)
            else:
                pygame.draw.rect(self.__gameWindow,(185,106,89),buyButton)
            if cursorOverPlayerName:
                pygame.draw.rect(self.__gameWindow,(49,10,11),playerNameBgRect)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),playerNameBgRect)
            if cursorOverStart:
                pygame.draw.rect(self.__gameWindow,(49,10,11),startButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),startButton)
            if cursorOverLeaderboard:
                pygame.draw.rect(self.__gameWindow,(49,10,11),leaderboardButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),leaderboardButton)
            if cursorOverCredits:
                pygame.draw.rect(self.__gameWindow,(49,10,11),creditsButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),creditsButton)
            if cursorOverReset:
                pygame.draw.rect(self.__gameWindow,(49,10,11),resetButton)
            else:
                pygame.draw.rect(self.__gameWindow,(116,58,54),resetButton)
            # Draw Text
            if cursorOverPlus:  
                self.__gameWindow.blit(plus1Image,plusRect)
            else:
                self.__gameWindow.blit(plusImage,plusRect)
            if cursorOverMinus:  
                self.__gameWindow.blit(minus1Image,minusRect)
            else:
                self.__gameWindow.blit(minusImage,minusRect)
            if cursorOverBuy and not info[3]:
                buyText = self.__fontSmall.render(buybuy,False,(185,106,89))
                buyTextRect = buyText.get_rect(center=(500,506))
                self.__gameWindow.blit(buyText,buyTextRect)
            else:
                buyText = self.__fontSmall.render(buybuy,False,(49,10,11))
                buyTextRect = buyText.get_rect(center=(500,506))
                self.__gameWindow.blit(buyText,buyTextRect)
            self.__gameWindow.blit(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getImage(),self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCarList()[self.__currentCar].getImageRect())
            self.__gameWindow.blit(titleText,titleTextRect)
            self.__gameWindow.blit(startText,startTextRect)
            self.__gameWindow.blit(leaderboardText,leaderboardTextRect)
            self.__gameWindow.blit(creditsText,creditsTextRect)
            self.__gameWindow.blit(resetText,resetTextRect)
            self.__gameWindow.blit(highscoreText,highscoreTextRect)
            self.__gameWindow.blit(moneyText,moneyTextRect)
            self.__gameWindow.blit(moneyNumberText,moneyNumberTextRect)
            self.__gameWindow.blit(highscoreNumberText,highscoreNumberTextRect)
            self.__gameWindow.blit(buyText,buyTextRect)
            self.__gameWindow.blit(moneyValueCarText,moneyValueCarTextRect)
            self.__gameWindow.blit(playerNameText,playerNameTextRect)
            self.__gameWindow.blit(leftImage,leftRect1)
            self.__gameWindow.blit(rightImage,rightRect1)
            self.__gameWindow.blit(leftImage,leftRect2)
            self.__gameWindow.blit(rightImage,rightRect2)
            
            
            clicked = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    #Ansatz der Spielernameeingabe: https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
                    if playerNameInputActive:
                        if event.key == pygame.K_BACKSPACE:
                            textPlayerName = textPlayerName[:-1]
                        else:
                            textPlayerName += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
            pygame.display.update()
            self.__main.clock.tick(30.0)
        