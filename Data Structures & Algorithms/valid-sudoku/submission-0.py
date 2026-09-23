class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        total_hash_set = set([])

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                cell_value = [('row',i,val),('col',j,val), ('box',i//3,j//3,val)]

                if val != ".":      # Has a number inside
                    for cell in cell_value:
                        if cell in total_hash_set:
                            return False
                        else:
                            total_hash_set.add(cell)
                        

        return True

                    