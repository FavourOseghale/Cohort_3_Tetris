"""This code sets up a Tetris game using Pygame, initializing necessary modules, fonts, and display elements."""
import sys
import pygame
from Grid_Class import Grid

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Cohort 3 Tetris")

clock = pygame.time.Clock()

game_grid = Grid()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)