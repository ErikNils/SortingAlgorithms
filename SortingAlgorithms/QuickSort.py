#!/usr/bin/python3


def pick_pivot(L, start, end):
    mid = (start+end-1)//2
    a = L[start]
    b = L[mid]
    c = L[end-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, end-1
    if b <= c <= a:
        return c, end-1
    return a, start



def partition(arr, start, end):
    pivot, pivotIndex = pick_pivot(arr, start, end)
    arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
    
    index = start

    for i in range(start,end):
        if arr[i] < pivot:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    
    arr[index], arr[end] = arr[end], arr[index]
    
    return index


def quickSort(arr, start = None, end = None):
    if start is None: start = 0
    if end is None: end = len(arr)-1
    
    if start < end:
        pivotIndex = partition(arr,start,end)
        quickSort(arr,start,pivotIndex-1)
        quickSort(arr,pivotIndex+1,end)
        
        
        
if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    quickSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    quickSort(arr2)
    print(arr2)