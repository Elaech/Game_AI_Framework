import pygame
import json
import game_logic
import game_graphics

"""
Main Controller of the application
"""



if __name__ == '__main__':
    with open("../resources/settings.json","r") as settings_file:
        settings = json.load(settings_file)
    for el in settings:
        print(el, settings[el])
    print(settings["magic"]["number"])