#!/usr/bin/python3

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
VIOLET = (132,112,255)

def selectionSort(arr, array_color = None, refill = None):
    for i in range(len(arr)-1):
        minimum = i
        
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                if array_color is not None and refill is not None:
                    array_color[minimum] = BLUE
                minimum = j
            if array_color is not None and refill is not None:
                array_color[j] = RED
                array_color[minimum] = GREEN
                array_color[i] = VIOLET
                refill()
                array_color[j] = BLUE
        
        arr[i], arr[minimum] = arr[minimum], arr[i]
        if array_color is not None and refill is not None:
            array_color[minimum] = BLUE
            array_color[i] = BLUE



if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    selectionSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    selectionSort(arr2)
    print(arr2)