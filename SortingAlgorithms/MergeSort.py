#!/usr/bin/python3
import pygame


def merge(arr,left,right):
    
    l = 0
    r = 0
    k = 0
    
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            arr[k] = right[r]
            r += 1
        else:
            arr[k] = left[l]
            l += 1
        k += 1
    
    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
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


if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    mergeSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    mergeSort(arr2)
    print(arr2)