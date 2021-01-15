import pygame.freetype
import pygame
from game_graphics import main_graphics as mg

def draw_main_menu():
    mg.window.fill(mg.color_scheme["background_color"])
    mg.draw_button(mg.width*2/5, mg.height*2/10, mg.width/5, mg.height*2/10, "Play")
    pygame.display.update()
