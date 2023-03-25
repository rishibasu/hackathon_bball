import pygame
import math
import random

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
        
    def random_color_tuple():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




# Initialize Pygame
pygame.init()

# Load the background image
background_image = pygame.image.load("basketball-background.jpeg")
screen_width, screen_height = background_image.get_size()

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the balls
balls = [
    Ball(screen_width, screen_height, Ball.random_color_tuple()),
    Ball(screen_width, screen_height, Ball.random_color_tuple()),
    Ball(screen_width, screen_height, Ball.random_color_tuple()),
    Ball(screen_width, screen_height, Ball.random_color_tuple()),
    Ball(screen_width, screen_height, Ball.random_color_tuple()) 
]

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move and bounce the balls
    for ball in balls:
        ball.move()
        ball.bounce(screen_width, screen_height)
    
    # Draw the background image
    screen.blit(background_image, (0, 0))
    
    # Draw the balls
    for ball in balls:
        ball.draw(screen)
    
    # Update the screen
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
