import pygame

class AnimationCreator(object):
    def __init__(self,gameWindow):
        '''
        Parameters:     gameWindow: pygame.surface.Surface
        Funktion:       Initialisierungs-Methode der animationCreator-Klasse
        Output:         None
        '''
        self.__font30 = pygame.font.Font("assets/fonts/pixelfont.ttf",30)
        self.__font20 = pygame.font.Font("assets/fonts/pixelfont.ttf",20)
        self.__gameWindow = gameWindow
        
    def animationDamage(self,animationCounter:int):
        '''
        Parameters:     animationCounter: int
        Funktion:       Erzeugt einen Grafischen Effekt auf dem Spielfenster, wenn die Funktion animationDamage durch das obstacleCreator-Objekt ausgelöst wurde.
                        Zeigt, dass der Spieler ein Leben verloren hat.
        Output:         None
        '''
        num = animationCounter//7+1
        text = "."*num + "hit!" + "."*num
        text1 = self.__font20.render("You were", False, "yellow")
        text2 = self.__font30.render(text, False, "yellow")
        text1Rect = text1.get_rect(center=(175,170))
        text2Rect = text2.get_rect(center=(170,200))
        self.__gameWindow.blit(text1,text1Rect)
        self.__gameWindow.blit(text2,text2Rect)
        
    def animationFule(self,animationCounter:int):
        '''
        Parameters:     animationCounter: int
        Funktion:       Erzeugt einen Grafischen Effekt auf dem Spielfenster, wenn die Funktion animationFule durch das obstacleCreator-Objekt ausgelöst wurde.
                        Zeigt, dass der Spieler einen Benzin-Kanister "aufgehoben" hat.
        Output:         None
        '''
        num = animationCounter//7+1
        text = "."*num + "was refilled!" + "."*num
        text1 = self.__font30.render("Fule", False, "yellow")
        text2 = self.__font20.render(text, False, "yellow")
        text1Rect = text1.get_rect(center=(175,170))
        text2Rect = text2.get_rect(center=(170,220))
        self.__gameWindow.blit(text1,text1Rect)
        self.__gameWindow.blit(text2,text2Rect)
        
    def animationWrench(self,animationCounter:int):
        '''
        Parameters:     animationCounter: int
        Funktion:       Erzeugt einen Grafischen Effekt auf dem Spielfenster, wenn die Funktion animationWrench durch das obstacleCreator-Objekt ausgelöst wurde.
                        Zeigt, dass der Spieler einen Schraubenschlüssel "aufgehoben" hat.
        Output:         None
        '''
        num = animationCounter//7+1
        text = "."*num + "was found" + "."*num
        text1 = self.__font30.render("Wrench", False, "yellow")
        text2 = self.__font20.render(text, False, "yellow")
        text1Rect = text1.get_rect(center=(175,170))
        text2Rect = text2.get_rect(center=(170,220))
        self.__gameWindow.blit(text1,text1Rect)
        self.__gameWindow.blit(text2,text2Rect)

    def animationMoney(self,animationCounter:int):
        '''
        Parameters:     animationCounter: int
        Funktion:       Erzeugt einen Grafischen Effekt auf dem Spielfenster, wenn die Funktion animationMoney durch das obstacleCreator-Objekt ausgelöst wurde.
                        Zeigt, dass der Spieler einen Geldschein "aufgehoben" hat.
        Output:         None
        '''
        num = animationCounter//7+1
        text = "."*num + "were found!" + "."*num
        text1 = self.__font30.render("250 M", False, "yellow")
        text2 = self.__font20.render(text, False, "yellow")
        text1Rect = text1.get_rect(center=(175,170))
        text2Rect = text2.get_rect(center=(170,220))
        self.__gameWindow.blit(text1,text1Rect)
        self.__gameWindow.blit(text2,text2Rect)