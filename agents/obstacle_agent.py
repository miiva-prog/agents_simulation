import random
import math

class ObstacleAgent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        angle = random.uniform(
            0,
            2 * math.pi
        )

        self.vx = math.cos(angle) * 0.4
        self.vy = math.sin(angle) * 0.4
        self.radius = 80

    def update(
        self,
        width,
        height
    ):
        self.x += self.vx
        self.y += self.vy

        if self.x < self.radius:
            self.x = self.radius
            self.vx *= -1

        if self.x > width - self.radius:
            self.x = width - self.radius
            self.vx *= -1

        if self.y < self.radius:
            self.y = self.radius
            self.vy *= -1

        if self.y > height - self.radius:
            self.y = height - self.radius
            self.vy *= -1

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(
            dx * dx +
            dy * dy
        )