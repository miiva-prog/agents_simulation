import pygame

class MainMenu:
    def __init__(self):
        self.options = [
            "Boids",
            "Random Walk",
            "Consensus",
            "Leader-Follower",
            "Exit"
        ]

        self.selected = 0
        pygame.font.init()
        self.title_font = pygame.font.SysFont(None, 64)
        self.font = pygame.font.SysFont(None, 42)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]

        return None

    def draw(self, screen):
        screen.fill((20, 20, 30))
        title = self.title_font.render(
            "SWARM SIMULATION",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (250, 80))
        y = 220

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (220, 220, 220)

            text = self.font.render(
                option,
                True,
                color
            )

            screen.blit(text, (340, y))
            y += 60