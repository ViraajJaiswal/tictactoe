#WAP TO MAKE TIC TAC TOE 

arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
temp1 = 0
temp2 = 0

def check_win(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True 
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True 

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True 
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True 

    return False 

for j in range(9):
    for i in range(3):
        for k in range(3):
            print(arr[i][k], end = " ")
        print()

    turn = input("Enter the position in the format x,y : ")

    temp1 = (int(turn[0])-1)
    temp2 = (int(turn[2])-1)

    if(j%2 == 0):
        arr[temp1][temp2] = "X"
    else:
        arr[temp1][temp2] = "O"

    if check_win(arr):
        for i in range(3):
            for k in range(3):
                print(arr[i][k], end = " ")
            print()
        print(f"Player {'X' if j % 2 == 0 else 'O'} wins!")
        break

else:
    for i in range(3):
        for k in range(3):
            print(arr[i][k], end = " ")
        print()
    print("It's a draw")