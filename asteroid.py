import pygame, random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            split_1_vector = self.velocity.rotate(random_angle)
            split_2_vector = self.velocity.rotate(-random_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position.x, self.position.y, split_radius)
            split_2 = Asteroid(self.position.x, self.position.y, split_radius)
            split_1.velocity = split_1_vector * 1.2
            split_2.velocity = split_2_vector * 1.2

