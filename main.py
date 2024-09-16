from constants import *
from player import Player
import pygame
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   
        updatable.update(dt)
        screen.fill(pygame.Color("black"))
        drawable.draw(screen)   
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        

if __name__ == "__main__":
    main()


#  git push origin main - git hub commit
#  source venv/bin/activate - virtual env