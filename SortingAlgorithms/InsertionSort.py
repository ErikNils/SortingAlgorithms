#!/usr/bin/python3

from colors import RED, BLUE, GREEN

def insertionSort(arr, array_color = None, refill = None):
    for i in range(1,len(arr)):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            if array_color is not None and refill is not None:
                array_color[j] = RED
                refill()
                array_color[j] = BLUE
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        if array_color is not None and refill is not None:
            array_color[j] = GREEN
            refill()
            array_color[j] = BLUE
            
            
if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    insertionSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    insertionSort(arr2)
    print(arr2)