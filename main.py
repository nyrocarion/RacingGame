import pygame
import sys

from player import Player
from gameEnvironment import GameEnvironment
from obstacleCreator import ObstacleCreator
from loadSave import LoadSave
from menuCreator import MenuCreator
from playerManager import PlayerManager
from menuManager import MenuManager

class Main(object):
    def __init__(self):
        '''
        Parameters:     None
        Funktion:       Initialisierungs-Methode der main-Klasse
        Output:         None
        '''  
        pygame.init()
        self.clock = pygame.time.Clock()
        self.xml = LoadSave(self)
        self.playerManager = PlayerManager(self)
        for playerFromList in self.xml.getStartList():
            self.playerManager.addPlayerToList(Player(playerFromList[0],playerFromList[1]))
        if len(self.playerManager.getPlayerList()) == 0:
            self.playerManager.addNewPlayer()
        self.gameEnvironment = GameEnvironment(self)
        self.gameWindow = self.gameEnvironment.getGameWindow()
        self.obstacleCreator = ObstacleCreator(self.gameWindow,self)
        self.menuCreator = MenuCreator(self.gameWindow,self)
        self.menuManager = MenuManager()
        self.laufen = True
                   
    def mainloop(self):
        '''
        Parameters:     None
        Funktion:       Startet die mainloop des Spieles. Tasteneingaben werden abgearbeitet und das Spielefenster und seine Bestandteile geupdatet. Überprüft auch, ob der Run beendet ist und führt
                        dann Schritt aus um die Spielumgebung sowohl grafisch als auch im Modell so zurückzusetzen, dass ein erneuter Run möglich ist.
        Output:         None
        '''
        self.gameEnvironment.setGameWindowSize(350,800)
        self.gameWindow == self.gameEnvironment.getGameWindow()
        self.gameEnvironment.createBackground()
        self.gameEnvironment.createTop()
        while self.laufen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    bewegung = "unknown" 
                    # Esc zum schließen anstatt Alt+F4
                    if event.key == pygame.K_ESCAPE:
                        self.laufen = False
                    # Bewegung
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        bewegung = "links"
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        bewegung = "rechts"
                    '''
                    if event.key == pygame.K_r:
                        self.playerManager.getCurrentPlayer().schaden()
                        self.playerManager.getCurrentPlayer().schaden()
                        self.playerManager.getCurrentPlayer().schaden()
                    if event.key == pygame.K_t:
                        self.playerManager.getCurrentPlayer().incWrench()
                    '''
                    self.playerManager.getCurrentPlayer().bewegung(bewegung)
            self.gameEnvironment.updateBackground()
            self.gameEnvironment.updateTop()
            self.obstacleCreator.collisiondetect()
            self.obstacleCreator.update()
            self.gameEnvironment.updateTop()
            self.playerManager.getCurrentPlayer().update(self.gameWindow) 
                
            pygame.display.update()
            self.clock.tick(30.0)
            
            if self.playerManager.getCurrentPlayer().checkEnd():
                self.gameEnvironment.setGameWindowSize(1000,800)
                self.gameWindow == self.gameEnvironment.getGameWindow()
                self.menuManager.setEndMenu(True)
                self.xml.toXML(self.playerManager.getCurrentPlayer().getId())
                values = self.xml.fromXML(self.playerManager.getCurrentPlayer().getId())   
                self.playerManager.getCurrentPlayer().loadSave(values[0],values[1],values[3]) 
                self.menuCreator.endMenu()
                self.playerManager.setCurrentPlayer(self.menuCreator.getCurrentPlayer())
                self.playerManager.getCurrentPlayer().endRun()
                self.obstacleCreator.reset()
                self.laufen = False
                
                        
m = Main()
m.menuCreator.mainMenu()

                        