from controller import main_controller
from game_graphics import settings_menu_graphics
import pygame
import tkinter


def clicked_on_back(mouse):
    return False


def clicked_on_board_width(mouse):
    return False


def clicked_on_board_height(mouse):
    return False


def clicked_on_alfabeta(mouse):
    return False

def clicked_on_simple_moves(mouse):
    return False


def start():
    clock = pygame.time.Clock()
    settings_menu_graphics.draw_settings_menu()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Text menu")