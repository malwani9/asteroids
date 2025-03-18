import pygame
from circleshape import CircleShape
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius , 2)
    
    def update(self, dt):
        self.position +=  self.velocity * dt
    
    def split(self):
        self.kill()
    
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           random_angle = random.uniform(20, 50)
           vector_1 =  pygame.math.Vector2(self.velocity).rotate(random_angle)
           vector_2 = pygame.math.Vector2(self.velocity).rotate(-random_angle)
           new_asteroid_1 = Asteroid(self.position.x,self.position.y,(self.radius - ASTEROID_MIN_RADIUS) )
           new_asteroid_2 = Asteroid(self.position.x, self.position.y,(self.radius - ASTEROID_MIN_RADIUS) )
           new_asteroid_1.velocity = vector_1 * 1.2
           new_asteroid_2.velocity = vector_2 * 1.2
           for group in self.groups():
               group.add(new_asteroid_1)
               group.add(new_asteroid_2)
        
