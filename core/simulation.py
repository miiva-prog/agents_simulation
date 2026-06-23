import pygame
import random
import math
from agents.agent import Agent
from agents.obstacle_agent import ObstacleAgent
from environment.world import World
from algorithms.boids import BoidsAlgorithm
from algorithms.random_walk import RandomWalk
from algorithms.consensus import ConsensusAlgorithm
from algorithms.leader_follower import LeaderFollowerAlgorithm
from metrics.metrics import Metrics
from database import Database

class Simulation:
    WIDTH = 1000
    HEIGHT = 700
    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.world = World(
            self.WIDTH,
            self.HEIGHT
        )

        self.boids = BoidsAlgorithm()
        self.consensus = ConsensusAlgorithm()
        self.leader_follower = LeaderFollowerAlgorithm()
        self.leader = None
        self.metrics = Metrics()
        self.database = Database()
        self.show_metrics = False
        self.frame_counter = 0
        self.save_interval = 300
        self.agents = []
        self.obstacles = []
        AGENTS_COUNT = 80
        OBSTACLES_COUNT = 6

        for _ in range(OBSTACLES_COUNT):
            while True:
                x = random.randint(
                    150,
                    self.WIDTH - 150
                )

                y = random.randint(
                    150,
                    self.HEIGHT - 150
                )

                candidate = ObstacleAgent(
                    x,
                    y
                )

                candidate.radius = 70
                valid = True

                for obstacle in self.obstacles:
                    dx = obstacle.x - candidate.x
                    dy = obstacle.y - candidate.y
                    dist = math.sqrt(
                        dx * dx +
                        dy * dy
                    )

                    if dist < (obstacle.radius + candidate.radius + 80):
                        valid = False
                        break

                if valid:
                    self.obstacles.append(
                        candidate
                    )

                    break

        for _ in range(AGENTS_COUNT):
            while True:
                x = random.randint(
                    50,
                    self.WIDTH - 50
                )

                y = random.randint(
                    50,
                    self.HEIGHT - 50
                )

                valid = True
                for obstacle in self.obstacles:
                    dx = x - obstacle.x
                    dy = y - obstacle.y

                    dist = math.sqrt(
                        dx * dx +
                        dy * dy
                    )

                    if dist < obstacle.radius + 40:
                        valid = False
                        break

                if valid:
                    self.agents.append(
                        Agent(x, y)
                    )

                    break

        if self.algorithm_name == "Leader-Follower":
            self.leader = self.agents[0]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "MENU"
            if event.key == pygame.K_m:
                self.show_metrics = (
                    not self.show_metrics
                )

        return None

    def update(self):
        self.frame_counter += 1

        if (self.frame_counter % self.save_interval == 0):
            avg_speed = (
                self.metrics.calculate_average_speed(
                    self.agents
                )
            )

            avg_distance = (
                self.metrics.calculate_average_distance(
                    self.agents
                )
            )

            self.database.save_experiment(
                self.algorithm_name,
                avg_speed,
                avg_distance,
                len(self.agents),
                len(self.obstacles)
            )

        for obstacle in self.obstacles:
            obstacle.update(
                self.WIDTH,
                self.HEIGHT
            )

        for i in range(len(self.obstacles)):
            for j in range(
                i + 1,
                len(self.obstacles)
            ):

                a = self.obstacles[i]
                b = self.obstacles[j]
                dx = b.x - a.x
                dy = b.y - a.y

                dist = math.sqrt(
                    dx * dx +
                    dy * dy
                )

                min_dist = (
                    a.radius +
                    b.radius
                )

                if dist < min_dist:
                    if dist == 0:
                        dist = 0.1

                    nx = dx / dist
                    ny = dy / dist

                    overlap = (
                        min_dist - dist
                    )

                    a.x -= nx * overlap / 2
                    a.y -= ny * overlap / 2
                    b.x += nx * overlap / 2
                    b.y += ny * overlap / 2
                    a.vx *= -1
                    a.vy *= -1
                    b.vx *= -1
                    b.vy *= -1

        for agent in self.agents:
            if self.algorithm_name == "Boids":
                self.boids.update(
                    agent,
                    self.agents,
                    self.obstacles
                )
            elif self.algorithm_name == "Random Walk":
                RandomWalk.update(
                    agent
                )
            elif self.algorithm_name == "Consensus":
                self.consensus.update(
                    agent,
                    self.agents
                )
            elif self.algorithm_name == "Leader-Follower":
                if agent == self.leader:
                    RandomWalk.update(
                        agent
                    )
                else:
                    self.leader_follower.update(
                        agent,
                        self.leader,
                        self.agents
                    )

            agent.update()

            for other in self.agents:
                if other == agent:
                    continue

                dx = agent.x - other.x
                dy = agent.y - other.y

                dist = math.sqrt(
                    dx * dx +
                    dy * dy
                )

                min_dist = (
                    agent.radius +
                    other.radius
                )

                if (0 < dist < min_dist):
                    nx = dx / dist
                    ny = dy / dist

                    overlap = (
                        min_dist - dist
                    )

                    agent.x += (
                        nx *
                        overlap *
                        0.5
                    )

                    agent.y += (
                        ny *
                        overlap *
                        0.5
                    )

                    agent.vx += nx * 0.2
                    agent.vy += ny * 0.2

            for obstacle in self.obstacles:
                dx = agent.x - obstacle.x
                dy = agent.y - obstacle.y

                dist = math.sqrt(
                    dx * dx +
                    dy * dy
                )

                min_dist = (
                    agent.radius +
                    obstacle.radius
                )

                if dist < min_dist:
                    if dist == 0:
                        dist = 0.1

                    nx = dx / dist
                    ny = dy / dist

                    agent.x = (
                        obstacle.x +
                        nx * min_dist
                    )

                    agent.y = (
                        obstacle.y +
                        ny * min_dist
                    )

                    agent.vx += nx * 3
                    agent.vy += ny * 3

            self.world.handle_boundaries(
                agent
            )

    def draw(self, screen):
        screen.fill(
            (30, 30, 30)
        )

        for obstacle in self.obstacles:
            pygame.draw.circle(
                screen,
                (220, 50, 50),
                (
                    int(obstacle.x),
                    int(obstacle.y)
                ),
                obstacle.radius
            )

        for agent in self.agents:
            color = (0, 255, 0)

            if (self.algorithm_name == "Leader-Follower" and agent == self.leader):
                color = (
                    255,
                    255,
                    0
                )

            pygame.draw.circle(
                screen,
                color,
                (
                    int(agent.x),
                    int(agent.y)
                ),
                agent.radius
            )

        font = pygame.font.SysFont(
            None,
            32
        )

        screen.blit(
            font.render(
                f"Algorithm: {self.algorithm_name}",
                True,
                (255, 255, 255)
            ),
            (10, 10)
        )

        screen.blit(
            font.render(
                f"Agents: {len(self.agents)}",
                True,
                (255, 255, 255)
            ),
            (10, 45)
        )

        screen.blit(
            font.render(
                f"Obstacles: {len(self.obstacles)}",
                True,
                (255, 255, 255)
            ),
            (10, 80)
        )

        screen.blit(
            font.render(
                "M - Metrics",
                True,
                (255, 255, 255)
            ),
            (10, 115)
        )

        screen.blit(
            font.render(
                "ESC - Main Menu",
                True,
                (255, 255, 255)
            ),
            (10, 150)
        )

        if self.show_metrics:
            avg_speed = (
                self.metrics.calculate_average_speed(
                    self.agents
                )
            )

            avg_distance = (
                self.metrics.calculate_average_distance(
                    self.agents
                )
            )

            compactness = (
                self.metrics.calculate_compactness(
                    self.agents
                )
            )

            screen.blit(
                font.render(
                    f"Avg Speed: {avg_speed:.2f}",
                    True,
                    (255, 255, 0)
                ),
                (700, 10)
            )

            screen.blit(
                font.render(
                    f"Avg Distance: {avg_distance:.2f}",
                    True,
                    (255, 255, 0)
                ),
                (700, 45)
            )

            screen.blit(
                font.render(
                    f"Compactness: {compactness:.2f}",
                    True,
                    (255, 255, 0)
                ),
                (700, 80)
            )

            screen.blit(
                font.render(
                    f"Frame: {self.frame_counter}",
                    True,
                    (255, 255, 0)
                ),
                (700, 115)
            )