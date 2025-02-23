lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1= set({})
player2 = set({})
box = """
 _________________
|  1  |  2  |  3  |
|_____|_____|_____|
|  4  |  5  |  6  |
|_____|_____|_____|
|  7  |  8  |  9  |
|_____|_____|_____|
"""
def who_win(n):
    wins = [
        {1, 2, 3}, {4, 5, 6}, {7, 8, 9},
        {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
        {1, 5, 9}, {3, 5, 7}
    ]
    for i in wins:
        if i.issubset(n):
            return True
    return False

print(box)
for i in range(5):
    while True:
        print("Player1: ")
        try:
            x = int(input())
            if x in lst:
                box = box.replace(f'{x}','X')
                player1.add(x)
                lst.remove(x)
                break
            else:
                print("Enter a valid number")
        except ValueError:
            print("Enter a Number")
    print(box)
    if who_win(player1):
        print("player1 wins")
        break
    if i == 4:
        print("It's a draw")
        break
    else:
        while True:
            print("Player2: ")
            try:
                O = int(input())
                if O in lst:
                    box = box.replace(f'{O}','O')
                    player2.add(O)
                    lst.remove(O)
                    break
                else:
                    print("Enter a valid number")
            except ValueError:
                print("Enter a Number")
        print(box)
        if who_win(player2):
            print("player2 wins")
            break