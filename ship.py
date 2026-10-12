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

    


    def update(self):
        # обновление позиции корабля с учетом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.setting.speed_ship

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.setting.speed_ship

        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.setting.speed_ship

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.setting.speed_ship

       

    def blitme(self):
            # рисование корабля в текущей позиции
        self.screen.blit(self.image , self.rect)



        


   

    

