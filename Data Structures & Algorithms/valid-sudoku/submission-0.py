class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row checker
        for row in board:
            seen = {"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0, ".": 0}
            for val in row:
                if seen[val] == 0 and val != ".":
                    seen[val] += 1
                elif seen[val] == 1:
                    return False
        #column checker
        for col in range(len(board)):
            seen = {"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0, ".": 0}
            for row in range(len(board)):
                if seen[board[row][col]] == 0 and board[row][col] != ".":
                    seen[board[row][col]] += 1
                elif seen[board[row][col]]== 1:
                    return False

        for box_row in range(3):
            for box_col in range(3):

                seen = {"1" : 0,"2" : 0,"3" : 0,"4" : 0,"5" : 0,"6" : 0,"7" : 0,"8" : 0,"9" : 0, ".": 0}

                for r in range(3):
                    for c in range(3):
                        val = board[box_row*3 +r][box_col*3 +c]
                        if seen[val] == 0 and val != ".":
                            seen[val] += 1
                        elif seen[val] == 1:
                            return False

        return True
        
       

            
                