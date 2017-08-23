import sys
import pygame

from gameObjects import Player, Background
from settings import SIZE, WHITE #импортируем файл глобальных настроек

pygame.init() #инициализируем
pygame.display.set_caption('Hello, world!') #название экрана

screen = pygame.display.set_mode(SIZE) #задает размер окна
clock = pygame.time.Clock() #параметр ограничивающй FPS

# Game objects
player = Player() # создаем обьект из модуля gameObjects
background = Background() # создаем обьект фона

while True:
    for event in pygame.event.get(): #вернет массив всех событий происходящих с окном
        if event.type == pygame.QUIT: #если бы выход
            sys.exit(0) #выходим

    screen.fill(WHITE) #заливаем цвет экрана в белый цвет
    player.update() # вызываем метод обновления движения
    background.update() # обновляем постоянно фон
    screen.blit(background.image, background.rect)  # отображение фона
    screen.blit(player.image, player.rect) #blit отвечает за отображение на экран
    pygame.display.flip()
    clock.tick(60)
