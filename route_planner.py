import heapq
import math
from helpers import Map, load_map, show_map

# calculates the shortest path between two nodes
def shortest_path(Map,start,goal): # example inputs Map = map_10, start = 2, goal = 0
    # tracks the nodes visited and what node you visited prior
    # at the end of this function node_path will look like {2: 0, 4: 2, 3: 2, 1: 2, 5: 3, 7: 5, 0: 5} with the inputs above
    node_path = {}
    node_path[start] = 0 # {2:0}
    
    current_cost = {}
    current_cost[start] = 0 # {2:0}
    
    # min heap that tracks the distances between a start and destination node
    frontier = [(0, start)] # [(0,20)]    
    
    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1] # first iteration, node = 2
        
        if node == goal:
            break
            
        for neighbor in Map.roads[node]: # Map.roads[node] = Map.roads[2] = [4, 3, 1]
            path_cost = distance(Map.intersections[node], Map.intersections[neighbor]) # distance(2, 7) = 0.49619668801776967
            new_cost = current_cost[node] + path_cost # new_cost = current_cost[2] + 0.49619668801776967 = 0.49619668801776967
            
            if neighbor not in current_cost or new_cost < current_cost[neighbor]:
                node_path[neighbor] = node  # {2: 0, 7: 2}
                current_cost[neighbor] = new_cost # {2: 0, 7: 0.49619668801776967}
                heapq.heappush(frontier, (new_cost, neighbor)) 

                # frontier (once every neighbor has been visited) = [(0.128, 3), (0.212, 4), (0.134, 1)], 
                # in the next iteration 3 will be the node and (0.128, 3) will be "popped" of the heap and the remaining list will be heapified 

    return best_route(node_path, start, goal)

# calculates the distance between two nodes
def distance(start, end):
        return (math.hypot(end[0] - start[0], end[1] - start[1]))

# traverse backwards to find the optimal path
def best_route(node_path, start, goal):
    if goal not in node_path:
        return(f"Goal destination {goal} not found on map.")
    
    node = goal
    path = []
    
    while node != start:
        path.append(node)
        node = node_path[node] 
    path.append(start)
    path.reverse()
    return path

### TEST MAP ###
# map_10 = load_map("map-10.pickle")

# shortest_path(map_10, 2, 0)
# # path: [2, 3, 5, 0]