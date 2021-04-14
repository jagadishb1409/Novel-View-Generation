import numpy as np

K = np.load('K.npy')
print("K ",K)

ret = np.load('ret.npy')
print("\n",ret)
# K = np.load('./camera_params/K.npy')

dist = np.load('dist.npy')
print("\n",dist)