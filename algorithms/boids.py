import math

class BoidsAlgorithm:
    def __init__(self):
        self.neighbor_radius = 120
        self.cohesion_weight = 0.02
        self.alignment_weight = 0.22
        self.separation_weight = 8
        self.obstacle_weight = 0.4
        self.obstacle_radius = 80

    def update(
        self,
        agent,
        agents,
        obstacles
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

        cohesion_x = 0
        cohesion_y = 0
        alignment_x = 0
        alignment_y = 0
        separation_x = 0
        separation_y = 0

        if neighbors:
            center_x = 0
            center_y = 0
            avg_vx = 0
            avg_vy = 0

            for n in neighbors:
                center_x += n.x
                center_y += n.y
                avg_vx += n.vx
                avg_vy += n.vy
                dx = agent.x - n.x
                dy = agent.y - n.y
                dist = math.sqrt(
                    dx * dx +
                    dy * dy
                )

                if 0 < dist < 18:
                    separation_x += (
                        dx /
                        (dist * dist)
                    )

                    separation_y += (
                        dy /
                        (dist * dist)
                    )

            count = len(neighbors)
            center_x /= count
            center_y /= count
            avg_vx /= count
            avg_vy /= count
            cohesion_x = (
                center_x -
                agent.x
            )

            cohesion_y = (
                center_y -
                agent.y
            )

            alignment_x = (
                avg_vx -
                agent.vx
            )

            alignment_y = (
                avg_vy -
                agent.vy
            )

        obstacle_x = 0
        obstacle_y = 0

        for obstacle in obstacles:
            dx = (
                agent.x -
                obstacle.x
            )

            dy = (
                agent.y -
                obstacle.y
            )

            dist = math.sqrt(
                dx * dx +
                dy * dy
            )

            safe_distance = (
                obstacle.radius +
                20
            )

            if 0 < dist < safe_distance:
                obstacle_x += (
                    dx /
                    (dist * dist)
                )

                obstacle_y += (
                    dy /
                    (dist * dist)
                )

        agent.vx += (
            0.02 * cohesion_x +
            8 * separation_x +
            0.22 * alignment_x +
            0.4 * obstacle_x
        )

        agent.vy += (
            0.02 * cohesion_y +
            8 * separation_y +
            0.22 * alignment_y +
            0.4 * obstacle_y
        )