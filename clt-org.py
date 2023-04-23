
import numpy as np
import array, os
import math

def modulus (list):
    print (math.sqrt (list[0]*list[0] + list[1]*list[1] + list[2]*list[2]))

def read_asc(filename):
    f = open(filename)
    All_points = []
    while True:
        new_line = f.readline()
        new_line = new_line.strip()
        x = new_line.split(' ')
        if len(x) == 3:
            A = [x[0], x[1], x[2]]
            All_points.append(A)
        else:
            break
    pts = np.array(All_points).astype(np.float)
    modulus (np.mean(pts, 0)) 
    modulus (np.std(pts,0)) 

path = os.path.dirname(os.path.realpath(__file__))
train_path = os.path.join(path, "faces")
facenames = sorted([d for d in os.listdir(train_path) if '.asc' in d])

for l in range(1,len(facenames)+1 ):
    s = os.path.join(train_path, facenames[l-1])
    print(s)
    print (read_asc(s))




