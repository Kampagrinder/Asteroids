from constants import *
import pygame
fps = pygame.time.Clock()
dt = 0 

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color("black"))
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()


#  git push origin main -git hub commit
#  source venv/bin/activate - virtual env