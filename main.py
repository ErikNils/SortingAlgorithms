# Python implementation for visualizing merge sort. 
import pygame
import random
#from SortingAlgorithms.MergeSort import mergeSort

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
    pygame.time.delay(20)
 
  
# Draw the array values
def draw():
    
    element_width =(WIDTH-len(array))//len(array)
    boundry_arr = WIDTH / len(array)
    boundry_grp = 550 / (len(array))
    pygame.draw.line(screen, (0, 0, 0), 
                    (0, 95), (900, 95), 6)
    for i in range(1, 100):
        pygame.draw.line(screen, 
                        (224, 224, 224),
                        (0, boundry_grp * i + 100),
                        (900, boundry_grp * i + 100), 1)
      
    # Drawing the array values as lines
    for i in range(1, len(array)):
        pygame.draw.line(screen, array_color[i], (boundry_arr * i-3, 100),
            (boundry_arr * i-3, array[i]*boundry_grp + 100), element_width)
        
        
def merge(arr,left,right):
    
    l = 0
    r = 0
    k = 0
    pygame.event.pump()
    
    while l < len(left) and r < len(right):
        refill()
        pygame.event.pump()
        if left[l] > right[r]:
            arr[k] = right[r]
            r += 1
        else:
            arr[k] = left[l]
            l += 1
        k += 1
    
    while l < len(left):
        refill()
        pygame.event.pump()
        arr[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        refill()
        pygame.event.pump()
        arr[k] = right[r]
        r += 1
        k += 1



def mergeSort(arr):
    n = len(arr)
    if n==1: return arr
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left)
    mergeSort(right)

    merge(arr,left,right)
  
# Infinite loop to keep the window open
while run:
    # background
    screen.fill((255, 255, 255))
    # Event handler stores all event 
    for event in pygame.event.get():
        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_array(150) 
            if event.key == pygame.K_RETURN:
                mergeSort(array)     
    draw()
    pygame.display.update()
      
pygame.quit()