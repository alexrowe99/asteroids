import pygame
from circleshape import CircleShape
from constants import ASTEROID_COLOUR, ASTEROID_LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, ASTEROID_LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt