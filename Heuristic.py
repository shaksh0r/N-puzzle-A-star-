class Heuristic:    
    def __init__(self,goal):
        self.goal = goal

    def boardPosition(self,position,k):
        row = position // k
        column = position - row*k

        return (row,column)
    def HammingDistance(self,board):
        cost = 0
        k = board.k
        config = board.boardConfig

        i = 0
        while(i < k*k-1):
            if self.goal[i] != config[i]:
                cost += 1
            i += 1
        
        return cost
    

    def ManhattanDistance(self,board):
        cost = 0
        k = board.k
        config = board.boardConfig

        i = 0
        while(i < k*k):
            if(config[i] == 0):
                i += 1
                continue

            currentRow,currentColumn = self.boardPosition(i,k)
            goalRow,goalColumn = self.boardPosition(config[i]-1,k)

            cost += abs(currentRow - goalRow) + abs(currentColumn - goalColumn)

            i += 1
        return cost
    def EuclideanDistance(self,board):
        cost = 0
        k = board.k
        config = board.boardConfig

        i = 0
        while(i < k*k):
            if(config[i] == 0):
                i += 1
                continue

            currentRow,currentColumn = self.boardPosition(i,k)
            goalRow,goalColumn = self.boardPosition(config[i]-1,k)

            cost += ((currentRow - goalRow)**2 + (currentColumn-goalColumn)**2)**0.5

            i += 1
        return cost

            

