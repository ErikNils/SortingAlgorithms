#!/usr/bin/python3

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

def heapify(arr, n, i, refill = None):
    largest = i
    left = 2 * i + 1
    right = left + 1

    if left < n and arr[largest] < arr[left]: largest = left
    if right < n and arr[largest] < arr[right]: largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        refill()
        heapify(arr, n, largest)


def buildMaxHeap(arr, refill = None):
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr, len(arr), i)



def heapSort(arr,array_color = None, refill = None):
    n = len(arr)
    buildMaxHeap(arr)
    heapSize = len(arr)
    for i in range(n-1, 0, -1):
        heapSize -= 1
        arr[heapSize], arr[0] = arr[0], arr[heapSize]
        heapify(arr, heapSize, 0)
        



if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    heapSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    heapSort(arr2)
    print(arr2)