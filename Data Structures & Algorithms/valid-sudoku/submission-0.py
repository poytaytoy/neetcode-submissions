def validate(booga: List[str]) -> bool:
    checker = set()

    for stuff in booga: 
        if stuff == ".":
            continue
        else:   
            if stuff in checker: 
                return False
            else: 
                checker.add(stuff)

    return True 

class Solution:
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board: 
            if not validate(row):
                return False 

        for i in range(0, 9):
            if not (validate([row[i] for row in board])):
                return False 
            
            goob = i 
            row = goob // 3 
            column = goob % 3 

            box = [
                x
                for r in board[row*3:(row+1)*3]
                for x in r[column*3:(column+1)*3]
            ]
            if not (validate(box)):
                return False 




        return True        