import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self,pos,dim,filepath,bis=720):
        '''
        Parameters:     pos: tuple, dim: tuple, filepath: str, bis: int mit default 720
        Funktion:       Initialisierungs-Methode der item-Klasse
        Output:         None
        '''  
        pygame.sprite.Sprite.__init__(self)
        self.__bis = bis
        self.__image = pygame.image.load(filepath)
        self.rect = self.__image.get_rect(size=(dim[0],dim[1]),topleft=(pos[0],pos[1]))
        
    def getImage(self):
        '''
        Parameters:     None
        Funktion:       Gibt Sprite (Bild) des item-Objektes zurück.
        Output:         self.__image: pygame.surface.Surface
        '''
        return self.__image
    
    def getRect(self):
        '''
        Parameters:     None
        Funktion:       Gibt Viereck des item-Objektes zurück. Das Bild des items wird mithilfe des Vierecks auf das Spielefenster "gemalt".
        Output:         self.rect: pygame.rect.Rect
        '''    
        return self.rect
    
    def getPos(self):
        '''
        Parameters:     None
        Funktion:       Gibt Position des item Vierecks in einer Liste in [x,y] Koordinaten Form zurück.
        Output:         [self.rect.x: int,self.rect.y: int]
        '''
        return [self.rect.x,self.rect.y]
    
    def incPos(self):
        '''
        Parameters:     None
        Funktion:       Gibt True zurück und ändert die y-Position des Vierecks um die positive Geschwindigkeit ab. Wenn das Viereck sich schon unter der y-Position (self.__bis) befindet, ab der man 
                        das Gegner-Fahrzeug nichtmehr sehen soll wird der Sprite gelöscht und False zurückgegeben
        Output:         bool
        '''
        if self.rect.y < self.__bis:
            self.rect.y += 2
            return True
        else:
            self.kill()
            return False
        