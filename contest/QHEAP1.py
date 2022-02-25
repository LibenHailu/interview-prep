import heapq


def main(query):
    h = []
    remove_dict = {}
    for i in range(int(query)):
        nextInput = input()
        operation = nextInput.split(" ")

        if operation[0] == '1':
            heapq.heappush(h, int(operation[1]))

        elif operation[0] == '3':
            while h[0] in remove_dict:
                if remove_dict[h[0]] == 1:
                    remove_dict.pop(h[0])
                else:
                    remove_dict[h[0]] -= 1

                heapq.heappop(h)

            print(h[0])

        elif operation[0] == '2':

            if operation[1] not in remove_dict:
                remove_dict[int(operation[1])] = 0

            remove_dict[int(operation[1])] += 1
        else:
            print("invalid command")


if __name__ == "__main__":
    query = input()
    main(query)
