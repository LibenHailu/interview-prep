import heapq


def main(query):
    h = {}
    for i in range(int(query)):
        nextInput = input()
        operation = nextInput.split(" ")
        if operation[0] == '1':
            heapq.heappush(h, int(operation[1]))
        elif operation[0] == '3':
            print(h[0])
        elif operation[0] == '2':
            heapq.heappop(h)
        else:
            print("invalid command")
        # print(operation)


if name == "main":
    query = input()
    # print(query)
    main(query)
