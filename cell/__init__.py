from typing import Set


class Cell:
    #vlaue of cell
    __value:int 
    # possible value set
    __valueSet:set 

    __dimension = 9
    
    def __init__(self):
        self.__value = 0
        self.__valueSet:set = set()
        # adding possible values of cells on initialization
        for i in range(self.__dimension):
            self.__valueSet.add(i+1)

    @property
    def value(self) ->int:
        return self.__value

    @property
    def valueSet(self):
        return self.__valueSet

    @value.setter
    def value(self,val:int) -> None:
        #if value is set thats the only possible value
        print(" ---------------------------------- set called",val)
        self.__valueSet.clear()
        self.__valueSet.add(val)
        self.__value = val

    def addValue(self,val:int) ->None:
        self.__valueSet.add(val)

    def removeValue(self,val:int) ->None:
        if self.__valueSet.__contains__(val) :
            self.__valueSet.remove(val)

    def isSetEmpty(self) ->bool:
        return self.__valueSet.__len__() == 0

    def singlePosibility(self) ->bool:
        return self.__valueSet.__len__() == 1
    
    def isCellSet(self) ->bool:
        return self.__value != 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__value},{self.__valueSet})"


