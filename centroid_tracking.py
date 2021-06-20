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
    (should work for any dimension of input)

b)  mode of numbering :
    - with history (for every new object assign new id)
    - without history (if there are 5 centroids then there will be ids 1 to 5)

output : 
Dict : {id : (coordinates),id : (coordinates),id : (coordinates),}
"""