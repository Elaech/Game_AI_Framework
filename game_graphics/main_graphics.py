import pygame.freetype
import json

window = None
color_scheme = None
settings = None
button_text_size = None
font = None
width = None
height = None


def init_graphics(screen, options):
    global window
    global settings
    global font
    global button_text_size
    global width
    global height
    settings = options
    height = settings["screen_height"]
    width = settings["screen_width"]
    button_text_size = 16
    font = pygame.freetype.SysFont("Arial", 16)
    window = screen
    init_colors()


def init_colors():
    global color_scheme
    with open("../resources/color_settings.json") as settings_file:
        color_scheme = json.load(settings_file)


def draw_button(x, y, button_width, button_height, button_text):
    window.fill(color_scheme["button_border"], (x, y, button_width, button_height))
    window.fill(color_scheme["button_color"], (x + 5, y + 5, button_width - 10, button_height - 10))
    font.render_to(window, (x, y), button_text, color_scheme["text_color"])
