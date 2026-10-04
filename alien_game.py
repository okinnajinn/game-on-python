import sys
import pygame

class AlienInvasion(): #класс для управления ресурсами и поведением игры

    def __init__(self):
        #инициализация игры и создание игровых ресурсов
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1980,1080))
        pygame.display.set_caption("инопланетяне атакуют!")

        # задание цвета фона
        self.bg_color = (255,230,230)

    def run_game(self):
        #основной цикл игры
        while True:
            # остслеживание клавы и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # при каждом проходе цикла перерисовываем экран
            self.screen.fill(self.bg_color)
            
            # отображение ласт прорисовки экрана
            pygame.display.flip()
            self.clock.tick(180)


if __name__ == "__main__":
    # создание экземпляра и запуск 
    ai = AlienInvasion()
    ai.run_game()
