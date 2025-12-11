from collections import defaultdict
from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
    """
    Validates a Sudoku board by checking rows, columns, and 3x3 sub-boxes.
    
    Time Complexity: O(1) - Since the board is fixed at 9x9, we iterate 81 cells max.
    Space Complexity: O(1) - We store at most 81 numbers in sets.
    """
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # Key: (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            # Skip empty cells
            if board[r][c] == ".":
                continue
            
            val = board[r][c]
            
            # Check 3x3 square logic
            square_key = (r // 3, c // 3)
            
            # Validation Checks
            if (val in rows[r] or 
                val in cols[c] or 
                val in squares[square_key]):
                return False
            
            # Add to sets
            rows[r].add(val)
            cols[c].add(val)
            squares[square_key].add(val)
            
    return True