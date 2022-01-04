#!/usr/bin/python3


def selectionSort(arr):
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]: minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]



if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    selectionSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    selectionSort(arr2)
    print(arr2)