#!/usr/bin/python3

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

def bubbleSort(arr, array_color = None, refill = None):
    n = len(arr)
        
    for i in range(n-1):
        flag = True
        for j in range(n-i-1):
            if array_color is not None and refill is not None:
                array_color[j] = RED
                refill()
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = False
            if array_color is not None: array_color[j] = BLUE
        if flag: break
        if array_color is not None:
            array_color[n-i-1] = GREEN
            refill()
            array_color[n-i-1] = BLUE


if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    bubbleSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    bubbleSort(arr2)
    print(arr2)