class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def handle_boundaries(self, agent):
        if agent.x < 0:
            agent.x = self.width

        if agent.x > self.width:
            agent.x = 0

        if agent.y < 0:
            agent.y = self.height

        if agent.y > self.height:
            agent.y = 0