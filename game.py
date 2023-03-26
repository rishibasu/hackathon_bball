import pygame
import random
import numpy as np
import math

# Initialize pygame
pygame.init()

# Set up the window
#WIDTH = 800
#HEIGHT = 600
#WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing Simulation")


# Load the background image
background_image = pygame.image.load("basketball-background.jpeg")
WIDTH, HEIGHT = background_image.get_size()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Define ball properties
BALL_RADIUS = 20
#BALL_SPEED = 5

# Basket Class
class basket: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Screen Class
class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

screen = Screen(WIDTH, HEIGHT)

# Ball Class
class ball():
    def __init__(self):
        self.x = 749
        self.y = 456
        self.color = ORANGE
        self.radius = BALL_RADIUS/2
        self.speed_x = 0
        self.speed_y = 0
        self.carried = False

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    # Check for collision with walls
        if self.x < self.radius * 4 or self.x > WIDTH - self.radius - 15:
            self.speed_x *= -1
        if self.y < self.radius * 4 or self.y > HEIGHT - self.radius - 15:
            self.speed_y *= -1
    


# Create class for the players
class player:
    def __init__(self, x, y, speed, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = BALL_RADIUS
        self.angle = random.uniform(0, math.pi)
        self.speed = speed
        self.orange_carried = False
        self.carrying = False

    def assignPlayer(self, name):
        n = self.name
        ndata = np.gettext("data/nba2021_advanced.csv", delimiter=',', usecols=(0,))
        for i, name in enumerate(ndata, start=1):
            if (n == name):
                self.nbapos, 
                self.age, 
                self.tm, 
                self.g, 
                self.mp, # market price
                self.per, # player efficiency rating
                self.ts, 
                self.tsp, 
                self.ftr = np.genfromtxt('data.csv', delimiter=',', skip_header=1, max_rows=1, usecols=(1,2,3,4,5,6,7,8,9), unpack=True)
                
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
            
    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)
    """
    def bounce(self, screen_width, screen_height):
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.angle = math.pi - self.angle
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.angle = -self.angle
    """
    def move(self):
        direction = random.uniform(-1, 1)
        wave_amplitude = 50
        wave_frequency = 0.01
        wave_offset = random.uniform(0, math.pi * 2)
        # self.x += self.speed * math.cos(self.angle)
        # self.y += self.speed * math.sin(self.angle)
        """
        # Check for collision with walls
        if self.x < self.radius*2 or self.x > WIDTH - self.radius - 5:
            self.speed_x *= -1
        if self.y < self.radius*2 or self.y > HEIGHT - self.radius - 5:
            self.speed_y *= -1
        """
        self.x = WIDTH // 2 + int(WIDTH // 2 * math.cos(self.angle))
        self.y = HEIGHT // 2 + int(HEIGHT // 2 * math.sin(self.angle))
        self.angle += direction * math.pi / 180
        self.x += int(wave_amplitude * math.sin(wave_frequency * self.x + wave_offset))
        self.y += int(wave_amplitude * math.sin(wave_frequency * self.y + wave_offset))
        
    player_direction_change_event = pygame.USEREVENT + 1
    pygame.time.set_timer(player_direction_change_event, random.randint(5000, 100000))

    def decide_turnover(self, player):
        if random.choice([1,2]) == 1:
            ball.carrier = self
        else:
            ball.carrier = player
           # carrying_ball(player, ball)
        ball.carried = True

    def carrying_ball(self, ball):
        dist = ((self.x - ball.x)**2 + (self.y - ball.y)**2)**0.5

        if dist <= self.radius + ball.radius:
            if ball.carried == False:
                ball.carried = True
                ball.carrier = self
                ball.speed_x = self.speed_x
                ball.speed_y = self.speed_y
                ball.x = self.x
                ball.y = self.y
            else:
                self.decide_turnover(ball.carrier)
             


            

# Create the balls
red_player = player(400, 400, 5, RED)
blue_player = player(400, 400, 3, BLUE)

#perhaps the ball should be different
orange_ball = ball()

# Set up game loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == player.player_direction_change_event:
            red_player.angle = random.uniform(0, math.pi)
            blue_player.angle = random.uniform(0, math.pi)

    # Move the balls
    red_player.move()
    blue_player.move()
    orange_ball.move()


    # Check for collisions between players and balls
    #red_ball.check_collision(blue_ball)
    #blue_ball.check_collision(red_ball)
    red_player.carrying_ball(orange_ball)
    blue_player.carrying_ball(orange_ball)

    # If the orange ball is being carried, move it with the carrying ball
    if hasattr(red_player, 'orange_carried') and red_player.orange_carried:
        orange_ball.x = red_player.x
        orange_ball.y = red_player.y
    elif hasattr(blue_player, 'orange_carried') and blue_player.orange_carried:
        orange_ball.x = blue_player.x
        orange_ball.y = blue_player.y

    # Draw the background and the balls
    #WIN.fill(background_image)
    WIN.blit(background_image, (0, 0))
    red_player.draw()
    blue_player.draw()
    orange_ball.draw()

    # Update the screen
    pygame.display.update()









"""
    def check_collision(self, other_ball):
        # Calculate distance between centers of balls
        dist = ((self.x - other_ball.x)**2 + (self.y - other_ball.y)**2)**0.5

        # Check if the balls are touching
        if dist < self.radius + other_ball.radius:
            # Calculate new velocities for the balls
            self.speed = ((self.speed_x**2 + self.speed_y**2)**0.5)
            other_ball.speed = ((other_ball.speed_x**2 + other_ball.speed_y**2)**0.5)
            self.direction = (self.x - other_ball.x, self.y - other_ball.y)
            other_ball.direction = (other_ball.x - self.x, other_ball.y - self.y)
            self.speed_new = other_ball.speed
            other_ball.speed_new = self.speed
            self.speed_new *= self.direction[0] / (self.direction[0] + other_ball.direction[0])
            other_ball.speed_new *= other_ball.direction[0] / (self.direction[0] + other_ball.direction[0])
            self.speed_x = self.speed_new * (self.direction[0] / abs(self.direction[0]))
            self.speed_y = self.speed_new * (self.direction[1] / abs(self.direction[1]))
            other_ball.speed_x = other_ball.speed_new * (other_ball.direction[0] / abs(other_ball.direction[0]))
            other_ball.speed_y = other_ball.speed_new * (other_ball.direction[1] / abs(other_ball.direction[1]))

            # If the orange ball is involved in the collision, carry it over to the other ball
            if self.color == ORANGE:
                other_ball.orange_carried = True
            elif other_ball.color == ORANGE:
                self.orange_carried = True
"""
