import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int):
        '''
        Parameters:     x: int, y: int
        Funktion:       Initialisierungs-Methode der enemy-Klasse
        Output:         None
        '''
        pygame.sprite.Sprite.__init__(self)
        self.__image = pygame.image.load("assets/cars/pickup_d.png")
        self.rect = self.__image.get_rect(size=(22,45),topleft=(x,y))
        self.__speed = 10
        
    def incPos(self):
        '''
        Parameters:     None
        Funktion:       Gibt True zurück und ändert die y-Position des Vierecks um die positive Geschwindigkeit ab. Wenn das Viereck sich schon unter der y-Position befindet, ab der man 
                        das Gegner-Fahrzeug nichtmehr sehen soll wird der Sprite gelöscht und False zurückgegeben
        Output:         bool
        '''
        if self.rect.y < 700:
            self.rect.y += self.__speed
            return True
        else:
            self.kill()
            return False
    
    def getSpeed(self):
        '''
        Parameters:     None
        Funktion:       Gibt Geschwindigkeit des Gegner-Fahrzeugs zurück.
        Output:         self.__speed: int
        '''
        return self.__speed
        
    def getImage(self):
        '''
        Parameters:     None
        Funktion:       Gibt Sprite (Bild) des Gegner-Fahrzeugs zurück.
        Output:         self.__image: pygame.surface.Surface
        '''
        return self.__image
    
    def getRect(self):
        '''
        Parameters:     None
        Funktion:       Gibt Viereck des Gegner-Fahrzeugs zurück. Das Bild des Gegner-Fahrzeugs wird mithilfe des Vierecks auf das Spielefenster "gemalt".
        Output:         self.rect: pygame.rect.Rect
        '''       
        return self.rect