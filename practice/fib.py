# the recursive approach

# def f(i):
#     if i < 2:
#         return i
# if is_computed[i]:
#     return f[i]

# f[i] = f(i-1) + f(i - 2)
# is_computed[i] = True
# return f[i]
# return f(i-1) + f(i - 2)


# Function for nth Fibonacci number
def Fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(9))

# with dp


def fib(n):

    f = [0] * n
    f[0] = 1
    f[1] = 1

    for i in range(2, n):
        f[i] = f[i-1] + f[i - 2]

    return f[n - 1]


print(fib(9))
# if n == 0:
#     return 0
# if n == 1:
#     return 1
