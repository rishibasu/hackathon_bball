import random
import math
import pygame
import numpy as np

# Define the Player class
class Player:
    def __init__(self, screen_width, screen_height, color, name, ):
        self.radius = 15
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.speed = 5
        self.angle = random.uniform(0, 2 * math.pi)
        self.color = color
        self.name = name
    
    def assignValues(self):
        n = self.name
        ndata = np.gettext("data/nba2021_advanced.csv", delimiter=',', usecols=(0,))
        for i, name in enumerate(ndata, start=1):
            if (n == name):
                self.nbapos, self.age, self.tm, self.g, self.mp, self.per, self.ts, self.tsp, self.ftr= np.genfromtxt('data.csv', delimiter=',', skip_header=1, max_rows=1, usecols=(1,2,3,4,5,6,7,8,9), unpack=True)


    
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
        


