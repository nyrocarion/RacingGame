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
    
    def settingsMenu(self):
        settingsBgRect = pygame.rect.Rect((0,50),(1000,100))
        settingsText = self.__fontTitle.render("SETTINGS",False,self.__colorFontMid)
        settingsTextRect = settingsText.get_rect(center=(500,100))
        
        backButton = pygame.rect.Rect((400,675),(200,50))
        backText = self.__fontButton.render("BACK", False, self.__colorBgMid)
        backTextRect = backText.get_rect(center=(500,700))
        
        resetText = self.__fontButton.render("RESET", False, self.__colorBgMid)
        resetButton = pygame.rect.Rect((50,175),(350,50))
        resetTextRect = resetText.get_rect(center=(225,200))
        
        bottomBgRect = pygame.rect.Rect((0,650),(1000,100))
        
        clicked = False
        while self.__main.menuManager.getSettingsMenu():
            self.__gameWindow.fill(self.__colorBgDark)
            cursorPos = pygame.mouse.get_pos()
            cursorOverBack = False
            cursorOverReset = False
            
            if backButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.playerManager.setCurrentPlayer(self.__currentPlayer)
                    self.__main.menuManager.setLeaderboardMenu(False)
                    break
                else:
                    cursorOverBack = True
            if resetButton.collidepoint((cursorPos[0],cursorPos[1])):
                if clicked:
                    self.__main.xml.resetXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3])   
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].resetAvailableCarList()
                else:
                    cursorOverReset = True
            #Draw        
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,settingsBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect)
            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,backButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,backButton)
            if cursorOverReset:
                pygame.draw.rect(self.__gameWindow,self.__colorBgBright,resetButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,resetButton)
            self.__gameWindow.blit(settingsText,settingsTextRect)
            self.__gameWindow.blit(backText,backTextRect)
            self.__gameWindow.blit(resetText,resetTextRect)
            
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
    
    def leaderboardMenu(self):
        '''
        Parameters:     None
        Funktion:       Erstellt eine Menü-Screen für das Leaderboard aller xml-Spielstände. Liest "Knopfdrücke" aus und wechselt entsprechend Menüs.
        Output:         None
        '''  
        creditsBgRect = pygame.rect.Rect((0,50),(1000,100))
        creditsText = self.__fontTitle.render("LEADERBOARD",False,self.__colorFontMid)
        creditsTextRect = creditsText.get_rect(center=(500,100))
        
        creditsBgRect = pygame.rect.Rect((50,175),(900,425))
        bottomBgRect = pygame.rect.Rect((0,650),(1000,100))
        
        backButton = pygame.rect.Rect((400,675),(200,50))
        backText = self.__fontButton.render("BACK", False, self.__colorBgMid)
        backTextRect = backText.get_rect(center=(500,700))
        
        clicked = False
        
        while self.__main.menuManager.getLeaderboardMenu():
            self.__gameWindow.fill(self.__colorBgDark)
            
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
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,creditsBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,creditsBgRect)

            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,backButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,backButton)
            # Draw Text
            self.__gameWindow.blit(creditsText,creditsTextRect)    
            self.__gameWindow.blit(backText,backTextRect)
            
            for element in self.__main.xml.scoreboard():
                leaderboardText = self.__fontMonospace.render(element[0]+element[1],False, self.__colorBgMid)
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
        creditsText = self.__fontTitle.render("CREDITS",False,self.__colorFontMid)
        creditsTextRect = creditsText.get_rect(center=(500,100))
        
        creditsLeftText1 = self.__fontButton.render("ALLGEMEIN",False,self.__colorBgMid)
        creditsLeftText2 = self.__fontMonospaceSmall.render("Erstellt von Niklas in ca.45h",False,self.__colorBgMid)
        creditsLeftText3 = self.__fontMonospaceSmall.render("im Rahmen eines Informatikprojekts",False,self.__colorBgMid)
        creditsLeftText4 = self.__fontMonospaceSmall.render("Pixelart selbst erstellt mit",False,self.__colorBgMid)
        creditsLeftText5 = self.__fontMonospaceSmall.render("www.piskelapp.com",False,self.__colorBgMid)
        
        creditsRightText1 = self.__fontButton.render("FONTS",False,self.__colorBgMid)
        creditsRightText2 = self.__fontMonospaceSmall.render("bluescreen.ttf",False,self.__colorBgMid)
        creditsRightText3 = self.__fontMonospaceSmall.render("www.dafont.com/blue-screen.font",False,self.__colorBgMid)
        creditsRightText4 = self.__fontMonospaceSmall.render("pixelfont.ttf",False,self.__colorBgMid)
        creditsRightText5 = self.__fontMonospaceSmall.render("www.dafont.com/minecraft.font",False,self.__colorBgMid)
        creditsRightText6 = self.__fontMonospaceSmall.render("edundot.ttf",False,self.__colorBgMid)
        creditsRightText7 = self.__fontMonospaceSmall.render("www.dafont.com/edit-undo-dot.font",False,self.__colorBgMid)   
        
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
        backText = self.__fontButton.render("BACK", False, self.__colorBgMid)
        backTextRect = backText.get_rect(center=(500,700))
        
        clicked = False
        
        while self.__main.menuManager.getCreditsMenu():
            self.__gameWindow.fill(self.__colorBgDark)#
            
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
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,creditsBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,creditsBgRect1)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,creditsBgRect2)
            
            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,backButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,backButton)
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
        gameoverText = self.__fontTitle.render("-GAME OVER-",False,self.__colorFontMid)
        moneyAllText = self.__fontValues.render("ALL MONEY: ",False,self.__colorBgMid)
        highscoreText = self.__fontValues.render("HIGHSCORE: ",False,self.__colorBgMid)
        moneyText = self.__fontValues.render("MONEY: ",False,self.__colorBgMid)
        scoreText = self.__fontValues.render("SCORE: ",False,self.__colorBgMid)
        
        moneyAllNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,self.__colorBgMid)
        highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,self.__colorBgMid)
        moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getMoney(True)),False,self.__colorBgMid)
        scoreNumber = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getScore()//50
        scoreNumberText = self.__fontValuesNumbers.render(str(scoreNumber),False,self.__colorBgMid)
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
        backText = self.__fontButton.render("BACK", False, self.__colorBgMid)
        backTextRect = backText.get_rect(center=(500,700))
        
        creditsButton = pygame.rect.Rect((400,550),(200,50))
        creditsText = self.__fontButton.render("CREDITS", False, self.__colorBgMid)
        creditsTextRect = backText.get_rect(center=(470,575))
        
        clicked = False
        
        while self.__main.menuManager.getEndMenu():
            self.__gameWindow.fill(self.__colorBgDark)
            
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
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,moneyAllBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,highscoreBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,gameoverBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,scoreBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,moneyBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect2)
            
            if cursorOverBack:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,backButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,backButton)
                
            if cursorOverLeaderboard:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,creditsButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,creditsButton)
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

        highscoreText = self.__fontValues.render("HIGHSCORE:",False,self.__colorBgMid)
        highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,self.__colorBgMid)
        moneyText = self.__fontValues.render("MONEY:",False,self.__colorBgMid)
        moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,self.__colorBgMid)
        titleText = self.__fontTitle.render("GAMETITLE",False,self.__colorFontMid)
        startText = self.__fontButton.render("START", False, self.__colorBgMid)
        leaderboardText = self.__fontButton.render("LEADERBOARD", False, self.__colorBgMid)
        creditsText = self.__fontButton.render("CREDITS", False, self.__colorBgMid)
        resetText = self.__fontButton.render("SETTINGS", False, self.__colorBgMid)
        info = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getCurrentCarInfo(self.__currentCar)
        moneyValueCarTextCalc = "["+str(info[0])+"] "+info[1]+" - "+str(info[2])+"$"
        moneyValueCarText = self.__fontMonospaceSmall.render(moneyValueCarTextCalc,False,self.__colorBgDark)
        
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
            moneyValueCarText = self.__fontMonospaceSmall.render(moneyValueCarTextCalc,False,self.__colorBgDark)
            if info[3]:
                buybuy = "BOUGHT"
            else:
                buybuy = "BUY"
            
            if not playerNameInputActive:
                textPlayerName = self.__main.playerManager.getPlayerList()[self.__currentPlayer].getName()
            playerNameText = self.__fontButton.render(textPlayerName,False,self.__colorBgMid)
            playerNameTextRect = playerNameText.get_rect(center=(500,325))
            moneyNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getTotalMoney(True)),False,self.__colorBgMid)
            moneyNumberTextRect = moneyNumberText.get_rect(topright=(440,183))
            highscoreNumberText = self.__fontValuesNumbers.render(str(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getHighscore()),False,self.__colorBgMid)
            highscoreNumberTextRect = highscoreNumberText.get_rect(topright=(940,183))
            self.__gameWindow.fill(self.__colorBgDark)
            
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
                '''
                if clicked:
                    self.__main.xml.resetXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    values = self.__main.xml.fromXML(self.__main.playerManager.getPlayerList()[self.__currentPlayer].getId())
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].loadSave(values[0],values[1],values[3])   
                    self.__main.playerManager.getPlayerList()[self.__currentPlayer].resetAvailableCarList()
                '''
                if clicked:
                    self.__main.menuManager.setSettingsMenu(True)
                    self.settingsMenu()
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
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,titleBgRect) 
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,moneyBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,highscoreBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,vehicleSelectionBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorFontMid,vehicleSelectionImageBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,moneyValueCarBgRect)
            pygame.draw.rect(self.__gameWindow,self.__colorBgBright,bottomBgRect)

            if cursorOverBuy and not info[3]:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,buyButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorBgBright,buyButton)
            if cursorOverPlayerName:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,playerNameBgRect)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,playerNameBgRect)
            if cursorOverStart:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,startButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,startButton)
            if cursorOverLeaderboard:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,leaderboardButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,leaderboardButton)
            if cursorOverCredits:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,creditsButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,creditsButton)
            if cursorOverReset:
                pygame.draw.rect(self.__gameWindow,self.__colorBgDark,resetButton)
            else:
                pygame.draw.rect(self.__gameWindow,self.__colorFontMid,resetButton)
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
                buyText = self.__fontSmall.render(buybuy,False,self.__colorBgBright)
                buyTextRect = buyText.get_rect(center=(500,506))
                self.__gameWindow.blit(buyText,buyTextRect)
            else:
                buyText = self.__fontSmall.render(buybuy,False,self.__colorBgDark)
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
        