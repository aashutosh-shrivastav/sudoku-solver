from math import floor
from numpy import array
from board import Board
import board
from cell import Cell

def removePossibleValueFromOtherCells(i:int,j:int,board:Board):
    print(f"Cleaning possible values :START")
    #remove from x axis
    counter  = 0
    print(f"Cleaning x axis values for ({i},{j}) = {board.cells[i][j].value} :START")
    for y in range(9):
        if y != j :
            counter+=1
            board.cells[i][y].removeValue(board.cells[i][j].value)
    print(f"Cleaned  {counter} x axis values for ({i},{j}) = {board.cells[i][j].value} :END")

    #remove from Y axis
    print(f"Cleaning y axis values for ({i},{j}) = {board.cells[i][j].value} :START")

    counter = 0
    for x in range(9):
        if x != i :
            counter+=1
            board.cells[x][j].removeValue(board.cells[i][j].value)
    print(f"Cleaned  {counter} y axis values for ({i},{j}) = {board.cells[i][j].value} :END")

    #remove from its block
    blockx = []
    a = floor(i/3)
    blockx.append(3*(a))
    blockx.append(3*(a)+1)
    blockx.append(3*(a)+2)

    blocky = []
    a= floor(j/3)
    blocky.append(3*(a))
    blocky.append(3*(a)+1)
    blocky.append(3*(a)+2)
    print(f"Cleaning block {3*floor(i/3)+floor(j/3)} values for ({i},{j}) = {board.cells[i][j].value} :START")

    for x in blockx:
        for y in blocky:
            if x != i and y!= j:
                board.cells[x][y].removeValue(board.cells[i][j].value)
    print(f"Cleaned block {3*floor(j/3)+floor(i/3)} values for ({i},{j}) = {board.cells[i][j].value} :END")

    print(f"Cleaning possible values :END")





def updatePossibleValues(board:Board) :
    print(f"Update :START")
    for i,row in enumerate(board.cells):
        for j, cell in enumerate(row):
            if cell.isCellSet() :
                removePossibleValueFromOtherCells(i,j,board)
    print(f"Update :END")
    
def computePossibleValues(board:Board) :
    updatePossibleValues(board)

def foundValuefromPossibleValues(board:Board) -> bool :
    print(f"foundValuefromPossibleValues :START")

    flag:bool = False
    counter = 0
    for row in board.cells:
        for cell in row:
            if  ( (cell.isCellSet() == False) and  cell.singlePosibility()) :
                counter+=1
                print(f"found {counter} single possible values")
                flag = True
                break
                # cell.value = cell.valueSet[0]
    print(f"foundValuefromPossibleValues :END")

    return flag

def appyValuesFromPossibleValues(board:Board) -> None:
    print(f"appyValuesFromPossibleValues :Start")
    counter = 0
    for row in board.cells:
        for cell in row:
            if  ( (cell.isCellSet() == False) and  cell.singlePosibility()) :
                counter+=1
                print(f"Applied {counter} single possible values")
                cell.value = cell.valueSet[0]
    print(f"appyValuesFromPossibleValues :END")


def eliminatePosibilityUsingValueAxisSurity(board:Board):
    counter = 0
    setA :set= {0,1,2}
    for i,row in board.cells:
        for j,cell in row:
            if(cell.isCellSet() == False):
                setRow = setA.difference({i})
                setCol = setA.difference({j})
                #for  all combination of x and y check confirm axial possibility and eleminate values


def solve(board:Board) -> Board:
    print(f"Solver :START ","\n",board.show(),"\n")
    updatePossibleValues(board)
    #eliminatePosibilityUsingValueAxisSurity(board)
    if (foundValuefromPossibleValues(board)):
        appyValuesFromPossibleValues(board)
        solve(board)
    print(f"Solver :END ","\n",board.show(),"\n")
    return board