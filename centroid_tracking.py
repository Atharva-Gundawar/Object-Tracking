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

    def __init__(self, with_history: bool = False, max_wait_frames: int = 5, dimensions : int = 2):
        """
        Initilizes the centroid tracker class

        Args:
            with_history (bool, optional): Refer file Docstirng. Defaults to False.
            max_wait_frames (int, optional): Num of frames to wait before deregistering a centroid. Defaults to 5.
            dimensions (int, optional): Dimentions of the detected centroid(2D,3D,etc). Defaults to 2.
        """
        self.with_history = with_history
        self.max_wait_frames = max_wait_frames
        self.last_frame = {}
        self.ids = []
        self.coordinates = []
        self.wait_frames = []
    

    def update(self,frame: List):
        """[summary]

        Args:
            frame (List): [description]
        """

       
        mini = 20000
        min_point = 0
        cf = [[],[]]
        counter = self.coordinates
        for last_coord in self.coordinates:
            for current_coord in frame:
                distance = math.dist(last_coord,j)
                if math.dist(last_coord,current_coord) < mini:
                    mini = distance
                    min_point = current_coord
               

            someindex = self.coordinates.index(last_coord)
            print(f'The closest point to {last_coord} is {min_point} at {mini} hence its id is {self.ids[someindex]}')

            cf[0].append(self.ids[someindex])
            cf[1].append(min_point)
            frame.pop(frame.index(min_point))
            if len(frame) == 0:
                break

            mini = 20000
            min_point = 0
            row = []

        for ele in frame:
            if ele not in cf[1]:
                cf[0].append(max(cf[0])+1)
                cf[1].append(ele)