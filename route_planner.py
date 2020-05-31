import math
from helpers import Map, load_map, show_map

# calculates the shortest path between two points
def shortest_path(Map,start,goal):
    came_from = {}
    came_from[start] = 0
    
    cost_so_far = {}
    cost_so_far[start] = 0
    
    frontier = [(0, start)]
    
    return came_from
#     return best_route(came_from, start, goal)
#     return("shortest path called.")

# calculates the distance between two points
def distance(start, end):
    return (math.hypot(map_10.intersections[end][0] - map_10.intersections[start][0], map_10.intersections[end][1] - map_10.intersections[start][1]))

# traverse backwards to find the optimal path
def best_route(came_from, start, goal):
    if goal not in came_from:
        return(f"Goal destination {goal} not found on map.")
    
    node = goal
    path = []
    
    while node != start:
        path.append(node)
        node = came_from[node]
#     print(path)    
    path.append(start)
    path.reverse()
    return path
#     return("best route called.")

### TEST MAPS ###
map_10 = load_map("map-10.pickle")
# map_40 = load_map("map-40.pickle")


# print("map_10 intersections", map_10.intersections)
# print("map_40 intersections", map_40.intersections)

# # test 1
# shortest_path(map_40, 8, 24)
# # path: [8, 14, 16, 37, 12, 17, 10, 24]

# # test 2
# shortest_path(map_10, 2, 0)
# # path: [2, 3, 5, 0]


# # test 3
# shortest_path(map_10, 3, 9)
# # path: []

