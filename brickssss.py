import pygame
import sys
from grid import Grid

pygame.init()

dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid()  # Create an instance of the Grid class

game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(dark_blue)
    game_grid.draw(screen)  # Draw the grid on the screen

    pygame.display.flip()
    clock.tick(60)
