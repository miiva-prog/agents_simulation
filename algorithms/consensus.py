import math

class ConsensusAlgorithm:
    def __init__(self):
        self.neighbor_radius = 150
        self.consensus_weight = 0.03
        self.cohesion_weight = 0.003
        self.separation_radius = 25
        self.separation_weight = 0.08

    def update(
        self,
        agent,
        agents
    ):
        neighbors = []

        for other in agents:
            if other == agent:
                continue

            distance = agent.distance_to(
                other
            )

            if distance < self.neighbor_radius:
                neighbors.append(
                    other
                )

        if not neighbors:
            return

        avg_vx = 0
        avg_vy = 0
        center_x = 0
        center_y = 0
        separation_x = 0
        separation_y = 0

        for neighbor in neighbors:
            avg_vx += neighbor.vx
            avg_vy += neighbor.vy
            center_x += neighbor.x
            center_y += neighbor.y
            dx = agent.x - neighbor.x
            dy = agent.y - neighbor.y

            dist = math.sqrt(
                dx * dx +
                dy * dy
            )

            if (0 < dist < self.separation_radius):
                separation_x += dx / dist
                separation_y += dy / dist

        count = len(
            neighbors
        )

        avg_vx /= count
        avg_vy /= count
        center_x /= count
        center_y /= count

        agent.vx += (
            avg_vx -
            agent.vx
        ) * self.consensus_weight

        agent.vy += (
            avg_vy -
            agent.vy
        ) * self.consensus_weight

        agent.vx += (
            center_x -
            agent.x
        ) * self.cohesion_weight

        agent.vy += (
            center_y -
            agent.y
        ) * self.cohesion_weight

        agent.vx += (
            separation_x *
            self.separation_weight
        )

        agent.vy += (
            separation_y *
            self.separation_weight
        )