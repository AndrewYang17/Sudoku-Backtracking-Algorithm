# Sudoku-Backtracking-Algorithm
Backtracking is an algorithmic-technique for solving problems **recursively** by trying to build a solution incrementally, one piece at a time, 
removing those solutions that fail to satisfy the constraints of the problem at any point of time.
<br><br>
For example, consider the Sudoku solving problem, we try filling digits one by one. Whenever we find that current digit cannot lead to a solution, we remove it (backtrack) and try next digit. 
This is better than naive approach which generating all possible combinations of digits and then trying every combination one by one.
<br><br>

## Algorithm:
Starting with an incomplete board:

1. Find some empty space.
2. Attempt to place the digits 1-9 in that space.
3. Check if that digit is valid in the current position based on the current board.
4. If the digit is valid, recursively attempt to fill the board using steps 1-3.
5. If it is not valid, reset the square you just filled and go back to the previous step.
6. Once the board is full by the definition of this algorithm we have solved the Sudoku!

