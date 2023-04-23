
import numpy as np
import array, os
import math

def read_asc(filename):
    num_select = 25000
    f = open(filename)
    All_points = []
    selected_points = []
    while True:
        new_line = f.readline()
        new_line = new_line.strip()
        x = new_line.split(' ')
        if len(x) == 3:
            A = np.array(x[0:3], dtype='float32')
            All_points.append(A)
        else:
            break
    # if the numbers of points are less than 2000, extent the point set
    if len(All_points) < (num_select):
        print('none detected')
        return None
    # take and shuffle points
    index = np.random.choice(len(All_points), int(len(All_points)/3), replace=False)
    for i in range(len(index)):
        selected_points.append(All_points[index[i]])
    return selected_points  # return N*3 array

path = os.path.dirname(os.path.realpath(__file__))
train_path = os.path.join(path, "faces")
subjectnames = sorted([d for d in os.listdir(train_path) if 'clt' not in d])

for l in range(0,len(subjectnames)):
	d_path = os.path.join(train_path, subjectnames[l])
	facenames = sorted([d for d in os.listdir(d_path) if '.asc' in d and 'aug' not in d])
	print(facenames)
	i = 0
	while i<len(facenames):
		samples = 0
		s = os.path.join(d_path, facenames[i])

		
		while samples < 30:
			points = read_asc(s)
			samples = samples + 1
			np.savetxt(os.path.join(path, "augmentation", "random", facenames[i].split(".")[0] + "aug" + str(samples) + ".asc"), points, delimiter=' ', fmt = '%f')
		#break
		i = i + 1
	#break


