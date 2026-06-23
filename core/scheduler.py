def update_neighbors(agents):
    for agent in agents:
        agent.neighbors = []

        for other in agents:
            if agent == other:
                continue

            distance = (
                agent.position.distance_to(
                    other.position
                )
            )

            if distance <= agent.radius:
                agent.neighbors.append(
                    other
                )