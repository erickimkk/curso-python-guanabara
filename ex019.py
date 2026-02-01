import numpy as np

arrey = np.eye(5)

for i in range (arrey.shape[0]):
    for j in range (arrey.shape[1]):
        print(arrey[i,j])