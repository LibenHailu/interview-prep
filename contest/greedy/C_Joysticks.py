def joystics(players):
    player1 = players[0]
    player2 = players[1]
    count = 0
    while player1 > 0 and player2 > 0:
        if player1 == 1 and player2 == 1:
            break

        elif player2 >= player1:
            player1 += 1
            player2 -= 2
            count += 1

        else:
            player2 += 1
            player1 -= 2
            count += 1
        # print(player1, player2, count)
    print(count)


if __name__ == '__main__':
    joystics(list(map(int, input().rstrip().split())))
