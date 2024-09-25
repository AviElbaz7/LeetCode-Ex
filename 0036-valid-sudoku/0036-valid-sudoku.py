class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(board: List[List[str]]) -> bool:
            for i in range(9):
                hashmap = {}
                for j in range(9):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in hashmap:
                        return False
                    else:
                        hashmap[board[i][j]] = 0
            return True
        
        def checkCols(board: List[List[str]]) -> bool:
            for i in range(9):
                hashmap = {}
                for j in range(9):
                    if board[j][i] == '.':
                        continue
                    if board[j][i] in hashmap:
                        return False
                    else:
                        hashmap[board[j][i]] = 0
            return True
        
        def checkSubgrids(board: List[List[str]]) -> bool:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    hashmap = {}
                    # Check each 3x3 subgrid
                    for row in range(i, i + 3):
                        for col in range(j, j + 3):
                            if board[row][col] == '.':
                                continue
                            if board[row][col] in hashmap:
                                return False
                            else:
                                hashmap[board[row][col]] = 0
            return True
        
        # Check rows, columns, and subgrids
        return checkRows(board) and checkCols(board) and checkSubgrids(board)