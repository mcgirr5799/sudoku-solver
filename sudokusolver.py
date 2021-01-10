import numpy as np

sudokuboard = [
[4, 0, 0, 0, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 9, 8],
[3, 0, 0, 0, 8, 2, 4, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 8, 0],
[9, 0, 3, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 0, 6, 7, 0],
[0, 5, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 2, 0, 0, 9, 0, 7],
[6, 4, 0, 3, 0, 0, 0, 0, 0],
]

def possible(y,x,n):
    #this is a brute force method of solving the puzzle, the runtime is not insignificant

    #check if n is possible within the coordinates of x,y
    #default case is true

    global sudokuboard

    #checking in y row
    for i in range (0,9):
        if (sudokuboard[y][i] == n):
            return False
    
    #checking in x row
    for i in range (0,9):
        if (sudokuboard[i][x] == n):
            return False
    x_intial = (x//3)*3
    y_intial = (y//3)*3

    #checking in "local" grid
    for i in range(0,3):
        for j in range(0,3):
            if sudokuboard[y_intial + i][x_intial + j] == n:
                return False

    return True

def solve():
    #solving the puzzle via backtracking and recursion
    global sudokuboard

    for y in range(9):
        for x in range(9):
            if (sudokuboard[y][x] == 0):
                for n in range (1,10):
                    if (possible(y,x,n)):
                        sudokuboard[y][x] = n
                        solve()
                        sudokuboard[y][x] = 0
                return

    print(np.matrix(sudokuboard))

solve()

