import pygame
import math
import random
import player


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

# Helper function to generate a random color tuple
def random_color_tuple():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set up the balls
players = [
    player.Player(screen_width, screen_height, random_color_tuple()),
    player.Player(screen_width, screen_height, random_color_tuple()),
    player.Player(screen_width, screen_height, random_color_tuple()),
    player.Player(screen_width, screen_height, random_color_tuple()),
    player.Player(screen_width, screen_height, random_color_tuple()) 
]

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move and bounce the balls
    for player in players:
        player.move()
        player.bounce(screen_width, screen_height)
    
    # Draw the background image
    screen.blit(background_image, (0, 0))
    
    # Draw the balls
    for player in players:
        player.draw(screen)
    
    # Update the screen
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
