class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        values = []
        for i in range(9):
            values = []
            for j in range(9):
                v = board[i][j]
                if v in values:
                    return False
                if v != ".":
                    values.append(v)
                
                
        for i in range(9):
            values = []
            for j in range(9):
                v = board[j][i]
                if v in values:
                    return False
                if v != ".":
                    values.append(v)
                
                
        for i in range(3):
            for j in range(3):
                values = []
                for k in range(3):
                    for l in range(3):
                        v = board[k+i*3][l+j*3]
                        if v in values:
                            return False
                        if v != ".":
                            values.append(v)
                        
        
        return True