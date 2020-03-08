"""
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guard post while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).
"""

import math
def solution(dimensions, your_position, guard_position, distance):
    #Your code here
    def check_distance(position,distance):
        x,y = position[0]-your_position[0],position[1]-your_position[1]
        if x**2+y**2 <= distance**2:
            return True
        return False
    def get_angle(position):
        return math.atan2((position[1]-your_position[1]),(position[0]-your_position[0]))
    def reflect_room(dimensions,distance):
        x_num_room = distance//dimensions[0]+1
        y_num_room = distance//dimensions[1]+1
        room_idx = []
        for i in range(x_num_room+1):
            for j in range(y_num_room+1):
                room_idx.extend([(i,j),(i,-j),(-i,j),(-i,-j)])
        return set(room_idx)
    def get_position(idx,position):
        room_pos_x = idx[0]*dimensions[0]
        room_pos_y = idx[1]*dimensions[1]
        mirr_pos_x = position[0]
        mirr_pos_y = position[1]
        if abs(idx[0])& 1:
            mirr_pos_x = dimensions[0]-position[0]
        if abs(idx[1])& 1:
            mirr_pos_y = dimensions[1]-position[1]
        return [mirr_pos_x+room_pos_x,mirr_pos_y+room_pos_y]

    rooms_idx = reflect_room(dimensions,distance)
    count = 0
    hit_you_angle = []
    #res = []
    for idx in rooms_idx:
        your_mirror_position = get_position(idx,your_position)
        if check_distance(your_mirror_position,distance) and your_mirror_position != your_position:
            your_angle = get_angle(your_mirror_position)
            hit_you_angle.append(your_angle)
        guard_mirror_position = get_position(idx,guard_position)
        if check_distance(guard_mirror_position,distance):
            guard_angle = get_angle(guard_mirror_position)
            if guard_angle not in hit_you_angle:
                count += 1
                #res.append(guard_mirror_position)
    return count

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
