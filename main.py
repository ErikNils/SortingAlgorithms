#!/usr/bin/python3

import pygame
import pygame_widgets
import random
from SortingAlgorithms import alg_names, algorithms
from colors import BLUE, WHITE, GREY, GREEN, CYAN, VIOLET, RED
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.slider import Slider


pygame.font.init()

WIDTH = 1200
HEIGHT = 850

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Sorting Algorithm Visualizer")

run = True

delay = 20

array = []
array_color = []



# Generates an array of size n filled with random number bewteen 1 to n
def generate_array(n=150):
    global array, array_color
    arr = []
    arr_color = []
    for i in range(n):
        arr.append(random.randrange(1,n))
        arr_color.append(BLUE)
    array = arr
    array_color = arr_color
    



def refill():
    screen.fill(WHITE)
    draw()
    pygame.display.update()
    pygame.time.delay(delay)
 
  
# Draw the array values
def draw():
    n = len(array)+1
    bar_width =(WIDTH-n)//n
    bar_space = WIDTH/n
    bar_height = (HEIGHT-100)/(max(array)*1.05)
    pygame.draw.line(screen, (0, 0, 0), 
                    (0, 95), (WIDTH, 95), 6)
    # Draw the boundry
    for i in range(0, max(array)+1):
        pygame.draw.line(screen,
                        GREY,
                        (0, bar_height * i + 100),
                        (WIDTH, bar_height * i + 100), 1)
    
    # Draw the array
    for i in range(0, len(array)):
        pygame.draw.line(screen, array_color[i], (bar_space * i+bar_width, 100),
            (bar_space * i+bar_width, array[i]*bar_height + 100), bar_width)


alg_dropdown = Dropdown(
    screen, 200, 20, 130, 50, name='Select Algorithm',
    choices=alg_names,
    borderRadius=3, colour=VIOLET, values=algorithms, direction='down', textHAlign='left'
)
        

# Helper function for the sort_button to start the selected sorting algorithm
def pygame_sort():
    try:
        alg_dropdown.getSelected()(array,array_color,refill)
    except Exception:
        None
    


sort_button = Button(
    screen, 385, 20, 80, 50, text='Sort!', fontSize=30,
    margin=20, inactiveColour=RED, pressedColour=GREEN,
    radius=5, onClick=pygame_sort, font=pygame.font.SysFont('calibri', 15),
    textVAlign='bottom'
)


delay_slider = Slider(screen, 350, 75, 150, 10, min=5, max=200, step=2)

generate_slider = Slider(screen, 30, 75, 150, 10, min=5, max=200, step=1)


# Helper function for the gen_button to generate a new array of the chosen size
def pygame_generate():
    generate_array(generate_slider.getValue())

gen_button = Button(
    screen, 50, 20, 110, 50, text='Generate Array', fontSize=30,
    margin=20, inactiveColour=CYAN, pressedColour=GREEN,
    radius=5, onClick=pygame_generate, font=pygame.font.SysFont('calibri', 15),
    textVAlign='bottom'
)



if __name__ == '__main__':
    # Needs to have generated an array before function calls to stop it from crashing
    generate_array(20)
    while run:
        screen.fill(WHITE)
        delay = 205 - delay_slider.getValue()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            
        draw()
        pygame_widgets.update(events)
        pygame.display.update()

    pygame.quit()