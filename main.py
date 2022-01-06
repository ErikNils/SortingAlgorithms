# Python implementation for visualizing merge sort. 
import pygame
import random
from SortingAlgorithms.BubbleSort import bubbleSort
from SortingAlgorithms.HeapSort import heapSort
from SortingAlgorithms.InsertionSort import insertionSort
from SortingAlgorithms.MergeSort import mergeSort
from SortingAlgorithms.QuickSort import quickSort

pygame.font.init()

WIDTH = 1200
HEIGHT = 850

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Sorting Algorithm Visualizer")

run = True

BLUE = (0,0,255)
WHITE = (255,255,255)
GREY = (232,232,232)

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


def refill():
    screen.fill(WHITE)
    draw()
    pygame.display.update()
    pygame.time.delay(10)
 
  
# Draw the array values
def draw():
    bar_width =(WIDTH-len(array))//len(array)
    bar_space = WIDTH / len(array)
    bar_height = (HEIGHT-100) / (max(array)*1.05)
    pygame.draw.line(screen, (0, 0, 0), 
                    (0, 95), (WIDTH, 95), 6)
    # Draw the boundry
    for i in range(1, max(array)+1):
        pygame.draw.line(screen,
                        GREY,
                        (0, bar_height * i + 100),
                        (WIDTH, bar_height * i + 100), 1)
    
    # Drawing the array
    for i in range(1, len(array)):
        pygame.draw.line(screen, array_color[i], (bar_space * i, 100),
            (bar_space * i, array[i]*bar_height + 100), bar_width)
        
        


if __name__ == '__main__':
    # Needs to have generated an array before function calls to stop it from crashing
    generate_array(20)
    while run:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    generate_array(150) 
                if event.key == pygame.K_RETURN:
                    quickSort(array,array_color,refill)
        draw()
        pygame.display.update()

    pygame.quit()