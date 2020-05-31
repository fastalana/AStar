import math
from helpers import Map, load_map, show_map

# def shortest_path(Map,start,goal):
#     return("shortest path called.")

# calculates the distance between two points
def distance(start, end):
#     print("map_10 intersections", map_10.intersections)
#     a = map_10.intersections[end][0]
#     print(a)
    return math.hypot(map_10.intersections[end][0] - map_10.intersections[start][0], map_10.intersections[end][1] - map_10.intersections[start][1])
#     return("distance called.")



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

