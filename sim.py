import pygame
import random

# Initialize pygame
pygame.init()

# Set up the window
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing Simulation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Define ball properties
BALL_RADIUS = 20
BALL_SPEED = 5

# Create classes for the balls
class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = BALL_RADIUS
        self.speed_x = random.randint(-BALL_SPEED, BALL_SPEED)
        self.speed_y = random.randint(-BALL_SPEED, BALL_SPEED)
        self.orange_carried = False

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Check for collision with walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.speed_x *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.speed_y *= -1

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

# Create the balls
red_ball = Ball(100, 100, RED)
blue_ball = Ball(700, 500, BLUE)
orange_ball = Ball(400, 300, ORANGE)

# Set up game loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the balls
    red_ball.move()
    blue_ball.move()

    # Check for collisions between balls
    red_ball.check_collision(blue_ball)
    blue_ball.check_collision(red_ball)

    # If the orange ball is being carried, move it with the carrying ball
    if hasattr(red_ball, 'orange_carried') and red_ball.orange_carried:
        orange_ball.x = red_ball.x
        orange_ball.y = red_ball.y
    elif hasattr(blue_ball, 'orange_carried') and blue_ball.orange_carried:
        orange_ball.x = blue_ball.x
        orange_ball.y = blue_ball.y

    # Draw the background and the balls
    WIN.fill(WHITE)
    red_ball.draw()
    blue_ball.draw()
    orange_ball.draw()

    # Update the screen
    pygame.display.update()
