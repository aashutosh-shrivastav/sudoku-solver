from array import array
from board import Board
import numpy as np

from cell import Cell
import solverUtil as solver


arr:array  = []
# numCells:int = int(input("enter no of cells to input : "))
# print("enter cordiantes with values","\n")
# for i in range(numCells):
#     arr.append(Cell())
#     print(numCells+i)

arr1  = [
    [1,2,6],
    [2,2,8],
    [0,3,4],
    [0,7,3],
    [1,4,2],
    [1,6,4],
    [2,5,5],
    [3,1,3],
    [3,7,7],
    [4,0,7],
    [4,4,4],
    [4,8,9],
    [5,1,9],
    [5,7,5],
    [6,3,2],
    [6,6,1],
    [7,2,1],
    [7,4,7],
    [7,6,6],
    [8,1,5],
    [8,5,3]
]

# for i in range(numCells):
#     x:int = int(input("insert at x :"))
#     y:int = int(input("insert at y :"))
#     z:int = int(input("insert value :"))
#     arr.append([x,y,z])
B:Board = Board(cellValueArr=arr1)

# print(B.show())

solver.solve(B);
print(B.show(),"\n")
B.showCellDetails()
