import math

class Metrics:
    def calculate_average_speed(self, agents):
        total_speed = 0

        for agent in agents:
            speed = math.sqrt(
                agent.vx ** 2 +
                agent.vy ** 2
            )

            total_speed += speed

        return total_speed / len(agents)

    def calculate_average_distance(self,agents):
        if len(agents) < 2:
            return 0

        total_distance = 0
        pairs = 0

        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                dx = (
                    agents[i].x -
                    agents[j].x
                )

                dy = (
                    agents[i].y -
                    agents[j].y
                )

                total_distance += math.sqrt(
                    dx * dx +
                    dy * dy
                )

                pairs += 1

        return total_distance / pairs

    def calculate_compactness(self, agents):
        if not agents:
            return 0

        center_x = 0
        center_y = 0

        for agent in agents:
            center_x += agent.x
            center_y += agent.y

        center_x /= len(agents)
        center_y /= len(agents)
        total_distance = 0

        for agent in agents:
            dx = agent.x - center_x
            dy = agent.y - center_y

            total_distance += math.sqrt(
                dx * dx +
                dy * dy
            )

        return total_distance / len(agents)