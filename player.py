import random
import math
import pygame
import numpy as np


# Basket Class
class basket: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Define the Player class
class Player:
    def __init__(self, screen_width, screen_height, color):
        self.radius = 15
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.speed = 5
        self.angle = random.uniform(0, 2 * math.pi)
        self.color = color
    
    def assignPlayer(self, name):
        n = self.name
        ndata = np.gettext("data/nba2021_advanced.csv", delimiter=',', usecols=(0,))
        for i, name in enumerate(ndata, start=1):
            if (n == name):
                self.nbapos, self.age, self.tm, self.g, self.mp, self.per, self.ts, self.tsp, self.ftr= np.genfromtxt('data.csv', delimiter=',', skip_header=1, max_rows=1, usecols=(1,2,3,4,5,6,7,8,9), unpack=True)
                break;

    #
    def takeShot(self, basket_class):
        d = math.sqrt((self.x - basket.x)**2 + (self.y - basket.y)**2)
        #In pixels
        if (d < 40): return 0.6
        elif (d < 70): return 0.575
        elif (d < 104): return 0.525
        elif (d < 115): return 0.475
        elif (d < 130): return 0.425
        if (self.x < 125) or (self.x > 1440-125):
            if (d < 190):
                return 0.375
            elif (d < 270): return 0.425
            else: return 0.375
        else:
            if (d < 270):
                return 0.425
            elif (d < 400): return 0.375
            else: return 0.325

    
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
        


