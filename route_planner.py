from helpers import Map, load_map, show_map

def shortest_path(M,start,goal):
    return("shortest path called.")

shortest_path(1, 2, 3,)

### TEST MAPS ###
map_10 = load_map("map-10.pickle")
map_40 = load_map("map-40.pickle")

# # test 1
# shortest_path(map_40, 8, 24)
# # path: [8, 14, 16, 37, 12, 17, 10, 24]

# test 2
shortest_path(map_10, 2, 0)
# path: [2, 3, 5, 0]


# # test 3
# shortest_path(map_10, 3, 9)
# # path: []