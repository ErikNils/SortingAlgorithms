#!/usr/bin/python3

from colors import RED, BLUE, GREEN

def heapify(arr, n, i, array_color = None, refill = None):
    largest = i
    left = 2 * i + 1
    right = left + 1

    if left < n and arr[largest] < arr[left]: largest = left
    if right < n and arr[largest] < arr[right]: largest = right
    if largest != i:
        if array_color is not None and refill is not None:
            array_color[i] = RED
            array_color[largest] = RED
            refill()
        arr[i], arr[largest] = arr[largest], arr[i]
        if array_color is not None and refill is not None:
            refill()
            array_color[i] = BLUE
            array_color[largest] = BLUE
        heapify(arr, n, largest, array_color, refill)


def buildMaxHeap(arr, array_color = None, refill = None):
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, len(arr), i, array_color, refill)



def heapSort(arr,array_color = None, refill = None):
    n = len(arr)
    buildMaxHeap(arr, array_color, refill)
    heapSize = len(arr)
    for i in range(n-1, 0, -1):
        heapSize -= 1
        if array_color is not None and refill is not None:
            array_color[0] = RED
            array_color[heapSize] = RED
            refill()
        arr[heapSize], arr[0] = arr[0], arr[heapSize]
        
        if array_color is not None and refill is not None:
            array_color[0] = BLUE
            array_color[heapSize] = GREEN
            refill()
            array_color[heapSize] = BLUE
        heapify(arr, heapSize, 0, array_color, refill)
        



if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    heapSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    heapSort(arr2)
    print(arr2)