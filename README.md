# Python Sudoku Solver

Input : An array with zero indexed cordinates and value of the cells of the sudoku board.

Output : A list of solutions for the sudoku puzzle given in input

Current logic to determine the cell's value 

Step 1 : Determine all posible values for each cell
Step 2:  For each cell check/eleminate feasibility of each possible value with respect to axial blocks(3 x 3)
Step 3 : If single posibility found mark it as value of the cell
Step 4 : Repeat Step 1 if single posibility found