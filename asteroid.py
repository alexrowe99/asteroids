import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_COLOUR, ASTEROID_LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, ASTEROID_LINE_WIDTH)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		new_velocity1 = self.velocity.rotate(angle)
		new_velocity2 = self.velocity.rotate(-angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
		asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
		asteroid1.velocity = new_velocity1 * 1.2
		asteroid2.velocity = new_velocity2 * 1.2