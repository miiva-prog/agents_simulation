import random
import math

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
        self.max_speed = 2.5
        self.radius = 5

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def limit_speed(self):
        speed = math.sqrt(self.vx**2 + self.vy**2)

        if speed > self.max_speed:
            self.vx = self.vx / speed * self.max_speed
            self.vy = self.vy / speed * self.max_speed

    def bounce(self):
        self.vx *= -1
        self.vy *= -1

    def update(self):
        self.limit_speed()
        self.move()

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(dx * dx + dy * dy)