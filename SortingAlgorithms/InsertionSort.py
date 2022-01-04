#!/usr/bin/python3

def insertionSort(arr):
    for i in range(1,len(arr)-1):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
            
            
if __name__ == '__main__':
    arr1 = [5,3,7,1,7,4,2,8]
    insertionSort(arr1)
    print(arr1)
    arr2 = ['j','y','a','t','p']
    insertionSort(arr2)
    print(arr2)