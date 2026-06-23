import pygame
from visualization.menu import MainMenu
from core.simulation import Simulation

WIDTH = 1000
HEIGHT = 700

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Swarm Simulation")
    clock = pygame.time.Clock()
    menu = MainMenu()
    current_screen = "MENU"
    simulation = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_screen == "MENU":
                result = menu.handle_event(event)
                if result:
                    if result == "Exit":
                        running = False
                    else:
                        print(f"Selected: {result}")

                        simulation = Simulation(result)
                        current_screen = "SIMULATION"
            elif current_screen == "SIMULATION":
                result = simulation.handle_event(event)
                if result == "MENU":
                    current_screen = "MENU"
                    simulation = None

        if current_screen == "MENU":
            menu.draw(screen)
        elif current_screen == "SIMULATION":
            simulation.update()
            simulation.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()