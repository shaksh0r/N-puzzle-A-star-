class BoardNode:
    def __init__(self,boardSize,boardConfig,movesNeeded,id):
        self.id = id
        self.k = boardSize
        self.boardConfig = boardConfig
        self.movesNeeded = movesNeeded
        self.cost = 0

    def setCost(self,heuristic):
        self.cost = self.movesNeeded + heuristic 
