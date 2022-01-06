#!/usr/bin/python3

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

def merge(arr,left, mid, right, array_color = None, refill = None):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    l = 0
    r = 0
    
    # Using temporary array instead of just changing the given array
    # to make the visualization better.
    tmp = []
    
    while l < len(left_arr) and r < len(right_arr):
        if array_color is not None and refill is not None:
            array_color[l+left] = RED
            array_color[r+mid] = RED
            refill()
            array_color[l+left] = BLUE
            array_color[r+mid] = BLUE
        if left_arr[l] > right_arr[r]:
            tmp.append(right_arr[r])
            r += 1
        else:
            tmp.append(left_arr[l])
            l += 1
    
    while l < len(left_arr):
        if array_color is not None and refill is not None:
            array_color[l+left] = RED
            refill()
            array_color[l+left] = BLUE
        tmp.append(left_arr[l])
        l += 1

    while r < len(right_arr):
        if array_color is not None and refill is not None:
            array_color[r+mid] = RED
            refill()
            array_color[r+mid] = BLUE
        tmp.append(right_arr[r])
        r += 1

    # Using a temporary array makes the visualisation better, but the code a bit slower.
    j = 0
    for i in range(left, right+1):
        arr[i] = tmp[j]
        j += 1
        if array_color is not None and refill is not None:
            array_color[i] = GREEN
            refill()
            if right-left != len(arr)-2: array_color[i] = BLUE


def mergeSort(arr , array_color = None, refill = None, left = 0, right = None):
    if right == None: right = len(arr)-1
    
    if left < right:
        mid = (left+right)//2
        
        mergeSort(arr, array_color, refill, left, mid)
        mergeSort(arr, array_color, refill, mid+1, right)
    
        merge(arr, left, mid, right, array_color, refill)


if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    mergeSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    mergeSort(arr2)
    print(arr2)