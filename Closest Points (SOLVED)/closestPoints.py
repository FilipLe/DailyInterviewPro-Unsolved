import math
#Program to find closest points to origin (0,0)
def closest_points(points, k):
    # Fill this in.
    #To find distance, you do √((x2-x1)^2+(y2-y1)^2)
    distance_arr = []
    count = 0
    #While loop to find distances
    while count < len(points):
        distance = math.sqrt(points[count][0]**2+points[count][1]**2)
        distance_arr.append(distance)
        count += 1
    
    amount = 0
    points_arr = []
    #while loop to find min k times
    while amount < k:
        counter = 0
        current_min = math.inf
        current_count = 0
        #while loop to find min
        while counter < len(points):
            if distance_arr[counter] < current_min:
                current_min=distance_arr[counter]
                current_count = counter
            counter += 1
        points_arr.append(points[current_count])#store closest point
        points.remove(points[current_count])#remove closest point and do the process again to find next closest point
        amount += 1
    return points_arr

print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
