import math


class LeaderFollowerAlgorithm:
    def __init__(self):
        self.follow_distance = 50
        self.follow_weight = 0.012
        self.separation_radius = 30
        self.separation_weight = 0.15

    def update(
        self,
        agent,
        leader,
        agents
    ):
        if leader is None:
            return

        if agent == leader:
            return

        speed = math.sqrt(
            leader.vx * leader.vx +
            leader.vy * leader.vy
        )

        if speed < 0.1:
            speed = 0.1

        dir_x = leader.vx / speed
        dir_y = leader.vy / speed

        target_x = (
            leader.x -
            dir_x *
            self.follow_distance
        )

        target_y = (
            leader.y -
            dir_y *
            self.follow_distance
        )

        dx = target_x - agent.x
        dy = target_y - agent.y

        agent.vx += (
            dx *
            self.follow_weight
        )

        agent.vy += (
            dy *
            self.follow_weight
        )

        separation_x = 0
        separation_y = 0

        for other in agents:
            if other == agent:
                continue

            dx = agent.x - other.x
            dy = agent.y - other.y

            dist = math.sqrt(
                dx * dx +
                dy * dy
            )

            if (
                0 <
                dist <
                self.separation_radius
            ):
                separation_x += (
                    dx / dist
                )

                separation_y += (
                    dy / dist
                )

        agent.vx += (
            separation_x *
            self.separation_weight
        )

        agent.vy += (
            separation_y *
            self.separation_weight
        )