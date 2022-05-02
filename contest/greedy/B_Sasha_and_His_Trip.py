
def sasha(inp):
    price = 0
    gas_cap = 0
    for i in range(1, inp[0] + 1):
        if i == 1:
            gas_cap = inp[1]
            if gas_cap > inp[0] or gas_cap == inp[0]:
                price += inp[0]*i - 1
            else:
                price += gas_cap*i
        else:
            gas_cap -= 1
            if inp[0] - i > gas_cap:

                gas_cap += 1
                price += i
    print(price)


if __name__ == '__main__':
    sasha(list(map(int, input().rstrip().split())))
