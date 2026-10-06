import sys
import pygame
from settings import Settings
from ship import Ship
from ship import NextShip
class AlienInvasion: #класс для управления ресурсами и поведением игры

    def __init__(self):
        #инициализация игры и создание игровых ресурсов
        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))

        pygame.display.set_caption("инопланетяне атакуют!")

        self.ship = Ship(self)
        self.nextship = NextShip(self)

        

    def run_game(self):
        #основной цикл игры
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(180)

    def _check_events(self):
        # остслеживание клавы и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # при каждом проходе цикла перерисовываем экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.nextship.blitmenextship()

        # отображение ласт прорисовки экрана
        pygame.display.flip()
        


if __name__ == "__main__":
    # создание экземпляра и запуск 
    ai = AlienInvasion()
    ai.run_game()
