def bubble_sort(a):
    for i in range(len(a)-1):  # O(N)
        for j in range(len(a)-i-1):  # O(N)
            if a[j] > a[j+1]:  # O(1)
                a[j], a[j+1] = a[j+1], a[j]  # O(1)


bubble([1, 5, 3, 9, 4])
