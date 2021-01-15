import main_controller
import pygame
"""
Main Menu controller that controls the interaction between the user and the application's main menu
"""


def check_if_callable(mouse):
    return false

def start():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check_if_callable(pygame.mouse.get_pos())

