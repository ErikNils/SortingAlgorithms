#!/usr/bin/python3
def bubbleSort(arr):
    n = len(arr)
        
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                


if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    bubbleSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    bubbleSort(arr2)
    print(arr2)