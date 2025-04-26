from Heuristic import Heuristic
from BoardNode import BoardNode
from queue import PriorityQueue


h = Heuristic([1,2,3,4,5,6,7,8,0])
pq = PriorityQueue()

closedList = []

def inClosedList(closedList,insertNode):
    for node in closedList:
        if node.id == insertNode.id:
            return True
    
    return False


id = 0
initial_node = BoardNode(3,[0,1,3,4,2,5,7,8,6],0,id)

initial_node.setCost(0)

pq.put((initial_node.cost,initial_node))

while True:
    cost, node = pq.get()
    closedList.append(node)
    if node.cost == 0:
        break

    i = 0
    k = node.k
    moves = node.movesNeeded
    grid = node.boardConfig
    row,column = 0,0
    while(i<k*k):
        if grid[i] == 0:
            row,column = h.boardPosition(i)
            break
    id+= 1
    if(column+1 < k):
        temp_grid = grid
        temp = grid[row*k + column+1]
        temp_grid[row*k + column+1] = temp_grid[row*k + column]
        temp_grid[row*k+column] = temp
        tempNode = BoardNode(k,temp_grid,moves+1,id)
        if (not inClosedList(closedList,tempNode)):

            heuristic = h.HammingDistance(tempNode)
            tempNode.setCost(heuristic)

            pq.put((tempNode.cost,tempNode))

    
    if(column-1 < k):
        temp_grid = grid
        temp = grid[row*k + column-1]
        temp_grid[row*k + column-1] = temp_grid[row*k + column]
        temp_grid[row*k+column] = temp
        tempNode = BoardNode(k,temp_grid,moves+1,id)

        if (not inClosedList(closedList,tempNode)):

            heuristic = h.HammingDistance(tempNode)
            tempNode.setCost(heuristic)
        
            pq.put((tempNode.cost,tempNode))
    if(row+1 < k):
        temp_grid = grid
        temp = grid[(row+1)*k+column]
        temp_grid[(row+1)*k+column] = temp_grid[row*k+column]
        temp_grid[row*k + column] = temp
        tempNode = BoardNode(k,temp_grid,moves+1,id)

        if (not inClosedList(closedList,tempNode)):

            heuristic = h.HammingDistance(tempNode)
            tempNode.setCost(heuristic)
        
            pq.put((tempNode.cost,tempNode))
    if(row-1 < k):
        temp_grid = grid
        temp = grid[(row-1)*k+column]
        temp_grid[(row-1)*k+column] = temp_grid[row*k+column]
        temp_grid[row*k + column] = temp
        tempNode = BoardNode(k,temp_grid,moves+1,id)


        if (not inClosedList(closedList,tempNode)):

            heuristic = h.HammingDistance(tempNode)
            tempNode.setCost(heuristic)
        
            pq.put((tempNode.cost,tempNode))
