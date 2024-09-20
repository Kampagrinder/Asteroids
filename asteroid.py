from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
     
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
             return 
         random_angle = random.uniform(20, 50)
         vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
         vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         small_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
         small_asteroid1.velocity = vector1 * 1.2
         small_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
         small_asteroid2.velocity = vector2 * 1.2
        

       
