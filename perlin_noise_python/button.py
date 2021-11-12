import pygame
import sys


#klasa przycisku
class button():
    def __init__(self, my_window, x_pos, y_pos, width, height, color, text_included = ''):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.text_included = text_included

        self.font = pygame.font.SysFont("Sans", 23)


    def create_button(self, my_window):
        pygame.draw.rect(my_window, self.color, (self.x_pos, self.y_pos, self.width, self.height), 0)

        text_to_render = self.font.render(self.text_included, 1, (0,0,0))
        my_window.blit(text_to_render, (self.x_pos + ((self.width-text_to_render.get_width())/2), self.y_pos + ((self.height-text_to_render.get_height())/2) ))

    def mouse_hover(self, pos):
        if pos[0] > self.x_pos and pos[0] < self.x_pos + self.width:
            if pos[1] > self.y_pos and pos[1] < self.y_pos + self.height:
                return True

        return False
