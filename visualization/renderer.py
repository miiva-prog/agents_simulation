import pygame

class Renderer:
    @staticmethod
    def draw_agent(screen, agent):
        pygame.draw.circle(
            screen,
            (0, 255, 0),
            (int(agent.x), int(agent.y)),
            agent.radius
        )

    @staticmethod
    def draw_text(screen, text, x, y):
        font = pygame.font.SysFont(None, 24)
        img = font.render(text, True, (255, 255, 255))
        screen.blit(img, (x, y))