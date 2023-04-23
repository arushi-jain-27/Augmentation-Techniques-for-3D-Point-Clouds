# Augmentation-Techniques-for-3D-Clouds

Given a 3D point cloud, we use the following types of sampling techniques for data
augmentation:

### Random Sampling:
In random sampling, to create multiple subsamples from a single sample, we randomly select a fixed proportion of points from the original point cloud multiple times. This creates different unordered subsets containing a uniform number of points. In our experiment, we are selecting one-third of the original points for each sample.

### Systematic Sampling:
In this technique, we sort the point cloud of a sample by ordering the points in 6 possible arrangements - (x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x). For each arrangement, we choose a random starting point in [0, k-1] and choose the subsequent points after skipping k, 2k, 3k... points where k lies in [3,5] depending on how crowded or sparse we want our subsamples to be. Lower k results in a lower variance of points among different subsamples while higher k results in less repetition but sparser point clouds. However, we need to ensure that the chosen k isn't symmetric about the point cloud as this will result in the same subsampled point cloud irrespective of the ordering arrangement. In our experiment, we are using k = 3 so that the subsamples use one-third of the point cloud.

### Stratified Sampling:
In this technique, we divide the entire point cloud of a sample into cubical windows of fixed size and then select a proportionate number of points randomly from each window to create a single subsample. Hence, a higher number of points are selected from a dense region, and a lower number of points are chosen from a sparse region thus maintaining localization. In our experiment, we are using a window size of 5*5*5, and we are selecting one-third of the total points from each window. 



### Verification:

We use ICP and Central Limit Theorem to prove that the subsamples created from our original samples all carry the same information and that they have the same discriminative power as the original sample respectively.

Iterative Closest Point algorithm: The ICP algorithm finds the transformation matrix between two point clouds by minimizing the square errors between them. One of the point clouds (target) is fixed, and the other one (source) is transformed to best match the target. The algorithm is iterative and improves the transformation matrix to minimize the error. Finally, it returns the final error after the transformation and the transformation matrix. The error is essentially the registration error between the two point clouds. 

Central Limit Theorem: The central limit theorem says that for any kind of data with a high number of samples:
○ Sampling distribution’s mean should be equal to the population mean
○ Sampling distribution’s standard deviation should be equal to the population standard deviation divided by the square root of the total number of samples
