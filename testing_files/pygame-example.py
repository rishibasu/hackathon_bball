import pygame
import math
import random
import player

# Helper function to generate a random color tuple
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


# Set up the players
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
    
    # Move and bounce the players
    for player in players:
        player.move()
        player.bounce(screen_width, screen_height)
    
    # Draw the background image
    screen.blit(background_image, (0, 0))
    
    # Draw a rectangle
    rect_width = 0.0868 * screen_width
    rect_height = 0.758772 * screen_height
    rect_x = 0
    rect_y = 0.118 * screen_height
    rect_color = (0, 255, 0, 0)

    # Create the rectangle object
    rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

    # Draw the rectangle onto the screen
    pygame.draw.rect(screen, rect_color, rect)


    
    # Draw the players
    for player in players:
        player.draw(screen)
    
    # Update the screen
    pygame.display.flip()
    
    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
