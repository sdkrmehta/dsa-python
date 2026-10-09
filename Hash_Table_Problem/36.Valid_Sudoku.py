def isValidSudoku(board):
    sett = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            row = str(board[i][j]) + "_ROW_" + str(i)
            col = str(board[i][j]) + "_COL_" + str(j)
            box = str(board[i][j]) + "_BOX_" + str(i // 3) + "_" + str(j // 3)

            if row in sett or col in sett or box in sett:
                return False

            sett.add(row)
            sett.add(col)
            sett.add(box)

    return True

print(isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))