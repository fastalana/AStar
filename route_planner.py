import heapq
import math
from helpers import Map, load_map, show_map

# calculates the shortest path between two points
def shortest_path(Map,start,goal): # example inputs Map = map_10, start = 2, goal = 0
    came_from = {}
    came_from[start] = 0 # {2:0}
    
    cost_so_far = {}
    cost_so_far[start] = 0 # {2:0}
    
    frontier = [(0, start)] # [(0,20)]    
    
    while len(frontier) > 0:
        node = heapq.heappop(frontier)[1] # first iteration, node = 2
        
        if node == goal:
            break
            
        for neighbor in Map.roads[node]: # Map.roads[node] = Map.roads[2] = [4, 3, 1]
            path_cost = distance(Map.intersections[node], Map.intersections[neighbor]) # distance(2, 7) = 0.49619668801776967
            new_cost = cost_so_far[node] + path_cost # new_cost = cost_so_far[2] + 0.49619668801776967 = 0.49619668801776967
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                came_from[neighbor] = node  # {2: 0, 7: 2}
                cost_so_far[neighbor] = new_cost # {2: 0, 7: 0.49619668801776967}
                heapq.heappush(frontier, (new_cost, neighbor)) # frontier (once every neighbor has been visited) = [(0.128, 3), (0.212, 4), (0.134, 1)]
    

    return best_route(came_from, start, goal)

# calculates the distance between two points
def distance(start, end):
        return (math.hypot(end[0] - start[0], end[1] - start[1]))

# traverse backwards to find the optimal path
def best_route(came_from, start, goal):
    if goal not in came_from:
        return(f"Goal destination {goal} not found on map.")
    
    node = goal
    path = []
    
    while node != start:
        path.append(node)
        node = came_from[node] 
    path.append(start)
    path.reverse()
    return path

### TEST MAP ###
# map_10 = load_map("map-10.pickle")

# shortest_path(map_10, 2, 0)
# # path: [2, 3, 5, 0]