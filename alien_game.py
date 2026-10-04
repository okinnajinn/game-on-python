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
            # остслеживание клавы и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # при каждом проходе цикла перерисовываем экран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # отображение ласт прорисовки экрана
            pygame.display.flip()
            self.clock.tick(180)


if __name__ == "__main__":
    # создание экземпляра и запуск 
    ai = AlienInvasion()
    ai.run_game()
