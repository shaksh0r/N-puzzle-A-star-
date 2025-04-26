from BoardNode import BoardNode

def solvable(board):
    k = board.k
    grid = board.boardConfig
    i = 0
    inversions = 0
    while(i < k*k):
        if grid[i] == 0:
            i += 1
            continue
        j = i+1
        while(j < k*k):
            if ((grid[i] > grid [j]) and grid[j] != 0) :
                inversions += 1
            j += 1
        i += 1 
    

    if k%2 == 0:
        i = 0
        while(i<k):
            if grid[i] == 0:
               row = k-(i // k)
               if ((row % 2 == 0) and (inversions % 2 != 0)):
                   return True
               elif ((row % 2 != 0) and (inversions % 2 == 0)):
                   return True 
               else:
                   return False
            i+=1
    else:
        if inversions % 2 == 0:
            return True
        else:
            return False


boardConfig = [0,1,3,4,2,5,7,8,6]

board = BoardNode(3,boardConfig,0)

if (solvable(board)):
    print("Solvable")
else:
    print("Unsolvable")