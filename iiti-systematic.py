import numpy as np
import array, os
import math

def read_asc(filename):
    f = open(filename)
    All_points = []
    while True:
        new_line = f.readline()
        new_line = new_line.strip()
        x = new_line.split(' ')
        if len(x) == 3:
            A = np.array(x[0:3], dtype='float32')
            All_points.append(A)
        else:
            break
    return All_points

def sort_p(i,a):
    if(i==0):
        a = a[a[:,2].argsort()]
        a = a[a[:,1].argsort(kind='mergesort')]
        a = a[a[:,0].argsort(kind='mergesort')]
    elif(i==1):
        a = a[a[:,2].argsort()]
        a = a[a[:,0].argsort(kind='mergesort')]
        a = a[a[:,1].argsort(kind='mergesort')]
    elif(i==2):
        a = a[a[:,1].argsort()]
        a = a[a[:,2].argsort(kind='mergesort')]
        a = a[a[:,0].argsort(kind='mergesort')]
    elif(i==3):
        a = a[a[:,1].argsort()]
        a = a[a[:,0].argsort(kind='mergesort')]
        a = a[a[:,2].argsort(kind='mergesort')]
    elif(i==4):
        a = a[a[:,0].argsort()]
        a = a[a[:,1].argsort(kind='mergesort')]
        a = a[a[:,2].argsort(kind='mergesort')]
    elif(i==5):
        a = a[a[:,0].argsort()]
        a = a[a[:,2].argsort(kind='mergesort')]
        a = a[a[:,1].argsort(kind='mergesort')]
    return a

path = os.path.dirname(os.path.realpath(__file__))
train_path = os.path.join(path, "faces")
#train_path = "faces"
subjectnames = sorted([d for d in os.listdir(train_path) if 'clt' not in d])
for l in range(0,len(subjectnames)):
    d_path = os.path.join(train_path, subjectnames[l])
    facenames = sorted([d for d in os.listdir(d_path) if '.asc' in d and 'aug' not in d])
    print(facenames)
    for i in range(0, len(facenames)):
        count = 1
        s = os.path.join(d_path, facenames[i])
        points = np.asarray(read_asc(s))
        for j in range(0,6):
            point_s = sort_p(j,points)
            for k in range(0,3):
                #print("k",k)
                k = j
                for p in range(0,len(point_s)-k):
                    #print(p)
                    if (p%3==0 and p<3):
                        #print(p,k)
                        sample = [point_s[p+k]]
                        #print([point_s[p+k]])
                    elif(p%3==0):
                        sample = np.append(sample,[point_s[p+k]],axis=0)
                            
                np.savetxt(os.path.join(path,"augmentation", "systematic", facenames[i].split(".")[0] + "aug" + str(count) + ".asc"), sample, delimiter=' ', fmt = '%f')
                #print(k)
                count = count+1
        #break
        
