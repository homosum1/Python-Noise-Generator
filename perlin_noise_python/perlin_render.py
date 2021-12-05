import pygame
import sys

from button import *
from noise import *

#inicjalizacja biblioteki python
pygame.init()

#utworzenie okna
w_width = 640
w_height = 550

pygame.display.set_caption('Perlin Noise v1.6')
my_window = pygame.display.set_mode((w_width, w_height))
font = pygame.font.SysFont("Sans", 25)
font_subtitles = pygame.font.SysFont("Sansa", 25)

#definicje przycisków
b_y = w_height-80
x = 130
b_x = 650-x
color = (82, 183, 57)
buttons_list = [Button(my_window, b_x, b_y, 110, 60, color, "EXIT"), Button(my_window, b_x-x, b_y, 110, 60, color, "CREATE"), Button(my_window, b_x-2*x, b_y, 110, 60, color, "SUBMIT")]

#definiowanie input-box'a
i_x = [b_x-3.91*x, b_x-3.91*x + 120]
i_y = b_y + 20
input_color_list = [(80,80,80), (80,80,80)]
input_box_list = [pygame.Rect(i_x[0], i_y, 110, 40), pygame.Rect(i_x[1], i_y, 110, 40)]


#definiowanie klasy do algorytmów szumu
my1DPerlin = Perlin_1D(10)
my1DPerlin.calculate_perlin(1, 2)
image = pygame.image.load('map.png')

def render():
    my_window.fill((128, 128, 128))
    #pygame.draw.rect(my_window, (80,80,80), (10, 10, 620, 440), 0)
    for button in buttons_list:
        button.create_button(my_window)
    
    for i in range(len(input_box_list)):
        pygame.draw.rect(my_window, input_color_list[i], input_box_list[i])
        pygame.draw.rect(my_window, (40,40,40), input_box_list[i],2)

        #obsługa wprowadzania seeda
        input_to_render = font.render(inputted_text_list[i], 1, (255, 255, 255))
        my_window.blit(input_to_render, (i_x[i] + 10, i_y + 10))

    #napisy
    octave = font_subtitles.render("OCTAVES " + str(function_data[0]), 1, (255, 255, 255))
    bias = font_subtitles.render("BIAS " + str(function_data[1]), 1, (255, 255, 255))
    my_window.blit(octave, (i_x[0], i_y - 20) )
    my_window.blit(bias, (i_x[1], i_y - 20) )
    
    #obsługa wypisywania grafu, wyników
    my_window.blit(image, (10, 10))

   
#główna pętla programu
image = pygame.image.load('map.png')
function_data = [1.0,2.0]


inputted_text_list = ["", ""]
RUN_PROGRAM = True

while RUN_PROGRAM:
    render()
    pygame.display.update()
    
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()

        # podświetlanie przycisków po najechaniu myszką
        if event.type == pygame.MOUSEMOTION:
            for button in buttons_list:
                if button.mouse_hover(mouse_position):
                    button.color = (68, 144, 49)
                else:
                    button.color = (0, 200, 10)

        # obsługa przycisków
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons_list[0].mouse_hover(mouse_position):
                RUN_PROGRAM = False
                
            if buttons_list[2].mouse_hover(mouse_position):
                for i in range(len(inputted_text_list)):
                    if len(inputted_text_list[i]) > 0:
                        function_data[i] = float(inputted_text_list[i])
                        inputted_text_list[i] = ""

                my1DPerlin.calculate_perlin(int(function_data[0]), function_data[1])
                image = pygame.image.load('map.png')

            if buttons_list[1].mouse_hover(mouse_position):
                my1DPerlin.initial_generation()
                my1DPerlin.calculate_perlin(int(function_data[0]), function_data[1])
                image = pygame.image.load('map.png')
                
            for i in range(len(input_color_list)):
                if input_box_list[i].collidepoint(event.pos):
                    input_color_list[i] = (50,50,50)
                else:
                    input_color_list[i] = (80, 80, 80)
                
        #obsługa wpisywania seeda
        if event.type == pygame.KEYDOWN:
            for i in range(len(input_color_list)):
                if input_color_list[i] == (50,50,50):
                    if event.key == pygame.K_BACKSPACE:
                        inputted_text_list[i] = inputted_text_list[i][:-1]
                    elif(len(inputted_text_list[i]) < 6 and ((event.unicode).isdigit() or event.unicode == ".") ):
                        inputted_text_list[i] += event.unicode

        #obsługa przycisku "zakończenia programu"
        if event.type == pygame.QUIT:
            RUN_PROGRAM = False
       

# zakończenie działania programu
pygame.display.quit()
pygame.quit()
sys.exit()


