from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
     
    def update(self, dt):
        self.position += self.velocity * dt
       


# self.x = x
# self.y = y
# self.radius = radius
#self.x += self.velocity.x * dt
#self.y += self.velocity.y * dt
