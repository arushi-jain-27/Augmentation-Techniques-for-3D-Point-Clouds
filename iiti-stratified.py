import numpy as np
import array, os
import math
from operator import itemgetter
import random

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
    lower = np.min(pts, 0)
    upper = np.max(pts, 0)
    window = (upper - lower)/5
    return lower, window, pts

def sample(group):
    points = []
    for pts in group.values():
        select = int(len(pts)/3)
        index = random.sample(pts, select)
        points = points + index
    return points



path = os.path.dirname(os.path.realpath(__file__))
train_path = os.path.join(path, "faces")
subjectnames = sorted([d for d in os.listdir(train_path) if 'clt' not in d])
for l in range(0,len(subjectnames)):
    d_path = os.path.join(train_path, subjectnames[l])
    facenames = sorted([d for d in os.listdir(d_path) if '.asc' in d and 'aug' not in d])
    print(facenames)
    for i in range(0, len(facenames)):
        count = 1
        while  (count<= 30):
            
            s = os.path.join(d_path, facenames[i])
            lower, window, points = np.asarray(read_asc(s))
            group = {}
            for j in range (0, len(points)):
                diff = (points[j] - lower)
                index = [int (p/q) for p, q in zip(diff, window)]
                idx = tuple (index)
                if idx not in group:
                    group[idx] = []
                group[idx].append(points[j])
            select = sample (group)
            np.savetxt(os.path.join(path,"augmentation", "stratified", facenames[i].split(".")[0] + "aug" + str(count) + ".asc"), select, delimiter=' ', fmt = '%f')
            count = count + 1
        #break
        
    
