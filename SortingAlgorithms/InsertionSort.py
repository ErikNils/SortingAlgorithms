#!/usr/bin/python3

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

def insertionSort(arr, array_color = None, refill = None):
    for i in range(1,len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            if array_color is not None and refill is not None:
                array_color[j] = RED
                array_color[j-1] = RED
                refill()
            arr[j], arr[j-1] = arr[j-1], arr[j]
            if array_color is not None and refill is not None:
                array_color[j] = BLUE
                array_color[j-1] = BLUE
                refill()
            j -= 1
            
            
if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    insertionSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    insertionSort(arr2)
    print(arr2)