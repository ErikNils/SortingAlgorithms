# Python implementation for visualizing merge sort. 
import pygame
import random
from SortingAlgorithms.BubbleSort import bubbleSort
from SortingAlgorithms.HeapSort import heapSort
from SortingAlgorithms.InsertionSort import insertionSort

pygame.font.init()

WIDTH = 900
HEIGHT = 650

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Sorting Algorithm Visualizer")

run = True

BLUE = (0,0,255)
WHITE = (255,255,255)

array = []
array_color = []




def generate_array(rng):
    global array, array_color
    arr = []
    arr_color = []
    for i in range(rng):
        arr.append(random.randrange(1,rng))
        arr_color.append(BLUE)
    array = arr
    array_color = arr_color
generate_array(20)

def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(100)
 
  
# Draw the array values
def draw():
    element_width =(WIDTH-len(array))//len(array)
    boundry_arr = WIDTH / len(array)
    boundry_grp = 550 / (max(array)*1.05)
    pygame.draw.line(screen, (0, 0, 0), 
                    (0, 95), (900, 95), 6)
    # Draw the boundry
    for i in range(1, max(array)+5):
        pygame.draw.line(screen, 
                        (224, 224, 224),
                        (0, boundry_grp * i + 100),
                        (900, boundry_grp * i + 100), 1)
      
    # Drawing the array
    for i in range(1, len(array)):
        pygame.draw.line(screen, array_color[i], (boundry_arr * i-3, 100),
            (boundry_arr * i-3, array[i]*boundry_grp + 100), element_width)
        
        



while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_array(20) 
            if event.key == pygame.K_RETURN:
                insertionSort(array,array_color,refill)
    draw()
    pygame.display.update()
      
pygame.quit()