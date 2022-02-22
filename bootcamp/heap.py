# User function Template for python3

import sys
import io
import atexit


class Solution:
    # parent returns the parent of the child nodes
    def parent(self, i):
        return i + 1 // 2

    # left returns the left child node of the parent
    def left(self, i):
        return 2 * i + 1

    # right returns the right child node of the parent
    def right(self, i):
        return 2*i + 2

    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left < n and arr[largest] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, n, largest)

        print(i)
    # Function to build a Heap from array.

    def buildHeap(self, arr, n):
        # code here
        for i in range(n//2, -1, -1):
            self.heapify(arr, n, i)
    # Function to sort an array using Heap Sort.

    def HeapSort(self, arr, n):
        # code here
        self.buildHeap(arr, n)
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
