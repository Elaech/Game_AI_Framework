import pygame.freetype


def draw_main_menu():
    main_graphics.window.fill(main_graphics.color_scheme["background_color"])
    main_graphics.draw_button(main_graphics.width*2/5, main_graphics.height*2/10,
                              main_graphics.width/5, main_graphics.height*2/10, "Play")
