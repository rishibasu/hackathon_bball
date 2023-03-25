import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set the dimensions of the rectangle
RECT_WIDTH = 300
RECT_HEIGHT = 300

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Wavy Dot")

# Set up the clock
clock = pygame.time.Clock()

# Set up the dot
dot_radius = 10
dot_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # start at the center of the screen
dot_angle = random.uniform(0, math.pi * 2)  # random initial angle
dot_speed = 3  # constant speed
dot_direction = random.choice([-1, 1])  # start by turning either left or right
dot_wave_amplitude = 50  # amplitude of the wave
dot_wave_frequency = 0.01  # frequency of the wave
dot_wave_offset = random.uniform(0, math.pi * 2)  # random wave offset

# Set up a timer to change the dot's direction every 5-10 seconds
dot_direction_change_event = pygame.USEREVENT + 1
pygame.time.set_timer(dot_direction_change_event, random.randint(5000, 10000))

# Game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == dot_direction_change_event:
            # Change the dot's direction by a random amount
            dot_direction *= random.choice([-1, 1])
            pygame.time.set_timer(dot_direction_change_event, random.randint(5000, 100000))  # schedule the next direction change

    # Update the dot's position
    dot_pos[0] = SCREEN_WIDTH // 2 + int(RECT_WIDTH // 2 * math.cos(dot_angle))
    dot_pos[1] = SCREEN_HEIGHT // 2 + int(RECT_HEIGHT // 2 * math.sin(dot_angle))
    dot_angle += dot_direction * math.pi / 180  # rotate the angle by a small amount in the current direction

    # Update the wave offset
    dot_wave_offset += random.uniform(-0.01, 0.01)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH // 2 - RECT_WIDTH // 2, SCREEN_HEIGHT // 2 - RECT_HEIGHT // 2, RECT_WIDTH, RECT_HEIGHT], 2)

    # Draw the dot
    dot_x = dot_pos[0] + int(dot_wave_amplitude * math.sin(dot_wave_frequency * dot_pos[1] + dot_wave_offset))
    dot_y = dot_pos[1]
    pygame.draw.circle(screen, BLACK, [dot_x, dot_y], dot_radius)

    # Update the screen
    pygame.display.flip()

    # Wait for a short amount of time to control the frame rate
    clock.tick(30)

# Clean up
pygame.quit()
