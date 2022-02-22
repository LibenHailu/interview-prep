from genericpath import samefile
from operator import le


class MyHeapImplementation:
    # parent returns the parent of the child nodes
    def parent(self, i):
        return i - 1 // 2

    # left returns the left child node of the parent
    def left(self, i):
        return 2 * i + 1

    # right returns the right child node of the parent
    def right(self, i):
        return 2*i + 2

    def heapify(self, arr, n, i):

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

    def buildHeap(self, arr, n):
        for i in range(n//2, -1, -1):
            self.heapify(arr, n, i)

    def heapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        print(arr)

    def getMin(self, arr, n):
        self.heapSort(arr, n)
        return arr[0]

    def insert(self, arr, n, val):
        arr.append(val)
        self.buildHeap(arr, n+1)

    def remove(self, arr, n, i):
        arr[n-1], arr[i] = arr[i], arr[n-1]
        arr.pop()
        self.buildHeap(arr, n-1)

    def update(self, arr, n, i, val):
        arr[i] = val
        self.buildHeap(arr, n)
