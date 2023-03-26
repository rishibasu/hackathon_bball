import numpy as np
import math
import random

# Basket Class
class Basket: 
    def __init__(self, x, y):
        self.x = x
        self.y = y


#create class for the ball
class Ball:
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
        if self.x < self.radius*4 or self.x > WIDTH - self.radius - 15:
            self.speed_x *= -1
        if self.y < self.radius*4 or self.y > HEIGHT - self.radius - 15:
            self.speed_y *= -1


#Player Class
class Player:
    def __init__(self, x, y, speed, team):
        self.x = x
        self.y = y
        self.team = team
        self.color = team.color
        self.radius = BALL_RADIUS
        #self.speed_x = random.randint(-BALL_SPEED, BALL_SPEED)
        #self.speed_y = random.randint(-BALL_SPEED, BALL_SPEED)
        self.speed_x = speed
        self.speed_y = speed
        self.angle = random.uniform(0, 2 * math.pi)
        self.orange_carried = False
        self.carrying = False
        self.in_tpz = False
        self.pts = 0

    def assignPlayer(self, name):
        n = self.name
        ndata = np.gettext("data/nba2021_advanced.csv", delimiter=',', usecols=(0,))
        for i, name in enumerate(ndata, start=1):
            if (n == name):
                self.nbapos, 
                self.age, 
                self.tm, 
                self.g, 
                self.mp, 
                self.per, 
                self.ts, 
                self.tsp, 
                self.ftr = np.genfromtxt('data.csv', delimiter=',', skip_header=i, max_rows=1, usecols=(1,2,3,4,5,6,7,8,9), unpack=True)
                
    def shotSuccess(self, team, basket):
        if (self.in_tps == True):
            self.pts += 3
            team.pts += 3

        else:
            self.pts += 2
            team.points += 2
            if ((math.sqrt((self.x - basket.x)**2 + (self.y - basket.y)**2)) < 100):
                team.close_pa += 1
            else:
                team.two_pa += 1

            
            
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
        self.x += self.speed_x * math.cos(self.angle)
        self.y += self.speed_y * math.sin(self.angle)

        # Check for collision with walls
        if self.x < self.radius*2 or self.x > WIDTH - self.radius - 5:
            self.speed_x *= -1
        if self.y < self.radius*2 or self.y > HEIGHT - self.radius - 5:
            self.speed_y *= -1

    def decide_turnover(self, player):
        if random.choice([1,2]) == 1:
            ball.carrier = self
        else:
            ball.carrier = player
           # carrying_ball(player, ball)
        ball.carried = True

    def carrying_ball(self, ball):
        dist = ((self.x - ball.x)**2 + (self.y - ball.y)**2)**0.5

        if dist < self.radius + ball.radius:
            if ball.carried == False or ball.carrier == self:
                ball.carried = True
                ball.carrier = self
                ball.speed_x = self.speed_x
                ball.speed_y = self.speed_y
                ball.x = self.x
                ball.y = self.y
            else:
                self.decide_turnover(ball.carrier)


#Team Class - 
#Attributes: total points, 3 point shots att (three_pa), 
# fs attempts (two_pa), close shot attempts (close_pa), player list, color
class Team:
    def __init__(self, players, color):
        self.points = 0
        self.players = players
        self.color = color
        self.three_pa = 0
        self.two_pa = 0
        self.close_pa = 0

class Game:
    def __init__(self, teams):
        self.team1 = teams[0] #team 1 scores on right hoop
        self.team2 = teams[1] #team 2 scores on left hoop
        self.time = 0
        self.shot_turnover = False
        self.steal_turnover = False
        self.possesion = 0 #0 means no team, 1 means team 1, 2 means team 2
    
    def incGametime(self):
        self.time += 1

def getDist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def takeShot(self, basket):
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
        

def shoot(p1, team2, basket1):
    if p1.carrying == True:
        shot_radius = 100
        for i, p2 in enumerate(team2.players):
            d = getDist(p1, p2)
            if (d <= shot_radius):
                shot_radius = d
        
        shot_offset = shot_radius / 100
        if (shot_offset**2 > 0.5):
            r = np.random.rand(1)
            total_chance = shot_offset * takeShot(p1, basket1)*0.7 * (p1.ts/5 + 1)
            if (r < total_chance):
                Player.shotSuccess(p1, p1.team, basket1)


