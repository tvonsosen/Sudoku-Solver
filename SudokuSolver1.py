# Input a Sudoku and then it will output the time and solved sudoku

import time
sudoku = [[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]


#creates global variable to use in inputsudoku function

def inputsudoku():
    """Function to get the sudoku rows"""
    rows = []
    for rownum in range(1,10):
        newrow = input("Input row " + str(rownum) +": ")
        for i in range(9):
            rows.append(int(newrow[i]))
    return rows
  

def createboard(rows1,sudoku1):
    """Function to create the board on the empty board from the inputed rows"""
    row = 0
    col = 0
    for i in range(81):
        sudoku1[row][col] = rows1[i]
        #Updates the empty sudoku to be equal to the corresponding numbers in rows
        col = col + 1
        if col==9:
            col = 0
            row = row + 1
        

def valid(x,y,a,sudoku1):
    """Function to check all possible solutions of a missing number"""
    for i in range(9):
        if sudoku1[x][i] == a:
            return False
        #Checks if whole column is equal to a and if it is it returns false to not use a
        #Does same for row in next loop
    for i in range(9):
        if sudoku1[i][y] == a:
            return False
    #Finds the top x point of each square and y point of each square
    squarex = (x//3)*3
    squarey = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku1[squarex+i][squarey+j] == a:
                return False
    #Checks if each coordinate in the individual squares are equal to a and if they are it returns false to not use a
    #a is a number from 1-9 in the next function to plug in for missing numbers(0s)
    return True
    #if all requirements pass and that number is not found in the square, row, or column it returns True to use a


def solver(sudoku1):
    """Recursive function used to solve sudoku"""
    for x in range(9):
        for y in range(9):
            #finds missing numbers by checking all numbers in grid
            if sudoku1[x][y] == 0:
                #if missing number it goes into loop where missing numbers are plugged with possible numbers using valid function
                for a in range(1,10):
                    if valid(x,y,a,sudoku1):
                        #if requirements pass, missing number is replaced with a and then function is then called on itself with new number in grid
                        sudoku1[x][y] = a
                        done = solver(sudoku1)
                        if done:
                            return True
                        #Exits function if all spaces are filled up with no zeros
                        sudoku1[x][y] = 0
                        #no more possible answers for a missing number are found, use backtracking, set last number to 0, return to find next possible solution                        
                return False
                #backtracks(sets last number to 0 and tests next possible number(a)) when run into a wall where no possible answers are availabe for zeros
    return True
    #Exits function when all numbers are filled and sudoku is done

start = time.perf_counter()
rowsInput = inputsudoku()
createboard(rowsInput,sudoku)
start = time.perf_counter()
foundSolution = solver(sudoku)
end = time.perf_counter()
print(sudoku)
print("Time:", str(end-start))
#takes processing time of solving the sudoku
