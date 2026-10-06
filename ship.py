import pygame

class Ship:
    def __init__(self , ai_game):
        #инициализация корабля и создание начальной его позиции
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # само изображение корабля загружаем и даем ему форму прямоугольника
        self.image = pygame.image.load('/home/okinnajinn/python/alien_invasion/images/sideship_03.png')
        self.rect = self.image.get_rect()

        # каждый новый корабль появляется снизу
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        # рисование корабля в текущей позиции
        self.screen.blit(self.image , self.rect)

class NextShip:
    def __init__(self , ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("/home/okinnajinn/python/alien_invasion/images/ship_000.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        

    def blitmenextship(self):
            # рисование корабля в текущей позиции
            self.screen.blit(self.image , self.rect )


        


   

    

