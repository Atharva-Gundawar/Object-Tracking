import numpy as np
import math

"""
Step 1 : get all centroids of current frame
step 2 : get centroids last frame
step 3 : record centroids of n frames to draw lines
step 4 : calculate closest distance between current centroids and previous centroids
step 5 : calculate best choice of centroids for ids

other things to do :
1> if an id is not in frame wait for 5 frames before deregistering
2> get dynamic new id for new centroid

inputs : 
a)  List of centroids eg : [(x,y),(x,y),(x,y)] or [(x,y,z),(x,y,z),(x,y,z)]
    (should work for multi dimension of input)

b)  mode of numbering :
    - with history (for every new object assign new id)
    - without history (if there are x centroids in a frame then there will be ids 1 to x)

output : 
Dict : {id : (coordinates),id : (coordinates),id : (coordinates),}
"""


class Centroid_tracker():

    def __init__(self, with_history: bool = False, wait_frames: int = 5, dimensions : int = 2):
        self.with_history = with_history
        self.wait_frames = wait_frames
        self.last_frame = {}
    
    def get_ids(self, coordinates : list):
        poc = [2, 3]
        last_frame = [[1, 2, 3, 4], [(2, 3), (10, 12), (20, 21), (30,40)]]
        current_frame =             [(2, 4), (10, 13), (20, 22), (23, 32), (30,41)]

        """ 
        # Handeles same or more in current
        for every poitn in current_frame
            if previous frame ids is not None:
                find the best match from previous frames and transfer id
            else : 
                assign new id 

        # to handle less in current or deregistration:
        for left over points in previous frame :
            copy and send them as 

        """
        for point in current_frame:
            if last_frame[0]:
                min_distance = 1000000
                last_points = last_frame[1]
                for i in last_points:
                    distance = math.dist(point,i)
                    # print(point, " ", i, " ", distance)
                    if distance < min_distance:
                        min_distance = distance
                        choosen_point = i
                # print(f"min distance : between {point} and {choosen_point} is {min_distance}")

        matrix = []
        row = []

        for i in last_frame[1]:
            for j in current_frame:
                row.append(math.dist(i,j))
            matrix.append(row)
            row = []

        list_as_array = np.array(matrix)

        print(np.transpose(list_as_array).argmin(axis=1)+1)