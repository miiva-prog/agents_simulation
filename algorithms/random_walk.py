import random
import math

class RandomWalk:
    @staticmethod
    def update(agent):
        angle = random.uniform(0, 2 * math.pi)
        agent.vx += math.cos(angle) * 0.2
        agent.vy += math.sin(angle) * 0.2