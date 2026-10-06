import pygame

class Ship:
    def __init__(self , ai_game):
        #инициализация корабля и создание начальной его позиции
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        # само изображение корабля загружаем и даем ему форму прямоугольника
        self.image = pygame.image.load('/home/okinnajinn/python/alien_invasion/images/sideship_03.png')
        self.rect = self.image.get_rect()

        # каждый новый корабль появляется снизу
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # рисование корабля в текущей позиции
        self.screen.blit(self.image , self.rect)


    def update(self):
        # обновление позиции корабля с учетом флага
        if self.moving_right:
            self.rect.x += self.setting.speed_ship

        if self.moving_left:
            self.rect.x -= self.setting.speed_ship

        if self.moving_up:
            self.rect.y -= self.setting.speed_ship

        if self.moving_down:
            self.rect.y += self.setting.speed_ship

        self.rect.x = self.x
        self.rect.y = self.y



        


   

    

