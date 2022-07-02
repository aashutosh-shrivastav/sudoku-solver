from array import array
import numpy as np
from cell import Cell

class Board:
    __dimension:int = 9
    __cells:array = [];

    def __init__(self,cellValueArr:array = []) -> None:
        #adding cells to board
        for i in range(self.__dimension):
            x = []
            for j in range(self.__dimension):
                x.append(Cell())
            self.__cells.append(x)
        # initializing values to calls of board
        for cellValue in cellValueArr:
            self.__cells[cellValue[0]][cellValue[1]].value =  cellValue[2]

    @property
    def cells(self):
        return self.__cells
    
    @cells.setter
    def cells(self,arr:array):
        self.__cells = arr

    @property
    def dimension(self):
        return self.__dimension;

    @dimension.setter
    def dimension(self,val:int):
        self.__dimension = val

    def show(self) -> array:
        print("\n Board \n")
        showArr = np.zeros((self.__dimension,self.__dimension),dtype=int);
        for i,cellArr in enumerate(self.__cells):
            for j,cell in enumerate(cellArr):
                showArr[i][j] = cell.value
        return showArr
    
    def showCellDetails(self) :
        counter = 0
        for i,cellArr in enumerate(self.__cells):
            for j,cell in enumerate(cellArr):
                print(cell)
                if(cell.isCellSet()):
                    counter+=1
        print(f"no od set cells {counter}")
