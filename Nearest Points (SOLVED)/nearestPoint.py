import math
#Program to find closest points
def closest_points(points, k, p):
    # Fill this in.
    #To find distance, you do √((x2-x1)^2+(y2-y1)^2)
    distance_arr = []
    count = 0
    #While loop to find distances
    while count < len(points):
        distance = math.sqrt((points[count][0]-p[0])**2+(points[count][1]-p[1])**2)
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

#List of points
points = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
]
print(closest_points(points, 2, (0,2)))
# [(1, 1), (2, 2)]
# or [(0, 0), (1, 1)]

#Distance from (0,2) to (2,2) is equal to the distance from (0,2) to (0,0)
