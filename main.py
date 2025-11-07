import pygame
from constants import *
from logger import log_state

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
