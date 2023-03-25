import random
import math
import pygame

# Define the Ball class
class Ball:
    def __init__(self, screen_width, screen_height, color):
        self.radius = 15
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.speed = 5
        self.angle = random.uniform(0, 2 * math.pi)
        self.color = color
    
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
    
    def bounce(self, screen_width, screen_height):
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.angle = math.pi - self.angle
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.angle = -self.angle
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        


