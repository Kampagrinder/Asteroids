from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, angle):
     super().__init__(x, y, SHOT_RADIUS)
     direction = pygame.Vector2(0, 1).rotate(angle)
     self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self,screen):
         pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=0)

    def update(self, dt):
       self.position += self.velocity * dt