from controller import main_controller
from game_graphics import settings_menu_graphics


def start():
    clock = pygame.time.Clock()
    settings_menu_graphics.draw_settings_menu()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                controller = get_callable(pygame.mouse.get_pos())
                if controller is not None:
                    return controller
