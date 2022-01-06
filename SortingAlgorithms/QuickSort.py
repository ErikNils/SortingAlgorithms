#!/usr/bin/python3

from random import sample
from colors import ORANGE, VIOLET, RED, BLUE, GREEN


def pick_pivot(arr, a, b, c):
    
    if arr[a] <= arr[b] <= arr[c]:
        return b
    if arr[c] <= arr[b] <= arr[a]:
        return b
    if arr[a] <= arr[c] <= arr[b]:
        return c
    if arr[b] <= arr[c] <= arr[a]:
        return c
    return a



def partition(arr, array_color, refill, start, end):
    # If there are atleast 3 elements in the array we pick median of three
    if end-start > 1:
        a, b, c = sample(range(start, end+1), 3)
        pivotIndex = pick_pivot(arr, a, b, c)
    else: 
        pivotIndex = start
    
    
    if array_color is not None and refill is not None:
        array_color[pivotIndex] = ORANGE
        array_color[end] = ORANGE
        refill()
        array_color[end] = VIOLET #
        array_color[pivotIndex] = BLUE
    
    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
    
    index = start

    for i in range(start,end):
        if array_color is not None and refill is not None:
            array_color[i] = GREEN
            array_color[index] = GREEN
            refill()
            array_color[i] = BLUE
            array_color[index] = BLUE
        if arr[i] < arr[end]:
            if array_color is not None and refill is not None:
                array_color[index] = RED
                array_color[i] = RED
                refill()
                array_color[index] = BLUE
                array_color[i] = BLUE
                array_color[end] = VIOLET #
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    

    arr[index], arr[end] = arr[end], arr[index]
    if array_color is not None and refill is not None:
        array_color[index] = RED
        array_color[end] = RED
        refill()
        array_color[end] = BLUE
        array_color[index] = BLUE
    
    return index


def quickSort(arr, array_color = None, refill = None, start = None, end = None):
    if start is None: start = 0
    if end is None: end = len(arr)-1
    
    if start < end:
        pivotIndex = partition(arr, array_color, refill, start, end)
        quickSort(arr, array_color, refill, start,pivotIndex-1)
        quickSort(arr, array_color, refill, pivotIndex+1,end)
        
        
        
if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    quickSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    quickSort(arr2)
    print(arr2)