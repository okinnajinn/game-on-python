import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion: #класс для управления ресурсами и поведением игры

    def __init__(self):
        #инициализация игры и создание игровых ресурсов
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))

        pygame.display.set_caption("инопланетяне атакуют!")

        self.ship = Ship(self)
        

        

    def run_game(self):
        #основной цикл игры
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(180)

    def _check_events(self):
        # остслеживание клавы и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # клавища нажата - тогда включаем флаг движения корабля
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                    
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            # клавиша отпущена - тогда выключаем флаг движения корабля
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False



                    

    def _update_screen(self):
        # при каждом проходе цикла перерисовываем экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
       

        # отображение ласт прорисовки экрана
        pygame.display.flip()
        


if __name__ == "__main__":
    # создание экземпляра и запуск 
    ai = AlienInvasion()
    ai.run_game()
