# Room areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, 
"bathroom", 9.50]
# b. Area of living room
print("Living room area:", areas[areas.index("living room") + 1])
# c. Kitchen and bedroom area
eat_sleep_area = areas[3] + areas[7]
print("Kitchen + Bedroom area:", eat_sleep_area)
# d. Downstairs and upstairs lists
downstairs = areas[:6]
upstairs = areas[6:]
print("Downstairs:", downstairs, "Upstairs:", upstairs)
# e. List of lists
house = [[areas[i], areas[i+1]] for i in range(0, len(areas), 2)]
print("House:", house)
# f. Update bathroom area and change living room
areas[9] = 10.50
areas[1] = "chill zone"
print("Updated areas:", areas)
# g. Add poolhouse
areas_1 = areas + ["poolhouse", 24.5]
print("Areas_1:", areas_1)
# h. Add garage
areas_2 = areas_1 + ["garage", 15.45]
print("Areas_2:", areas_2)
# i. Remove poolhouse
areas_2.remove("poolhouse")
areas_2.remove(24.5)
print("After removing poolhouse:", areas_2)
# j. Duplicate areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
area_copy = areas.copy()
area_copy[0] = 100
print("Original:", areas, "Copy:", area_copy)
# k. Explicit copy to prevent changes
area_copy = areas[:]
area_copy[0] = 200
print("After explicit copy - Original:", areas, "Copy:", area_copy)
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas.sort()
print(areas)
