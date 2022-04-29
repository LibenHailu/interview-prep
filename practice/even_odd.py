def even_odd(A):
    next_even, next_odd = 0, len(A) - 1

    while (0 <= next_even < len(A) and 0 <= next_odd < len(A) and next_even < next_odd):
        # print(A)
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A


print(even_odd([2, 7, 5, 2, 6, 3, 8, 4]))
