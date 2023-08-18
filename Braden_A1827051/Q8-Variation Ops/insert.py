import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
y = np.empty_like(x)

swap = np.array([3,7])

for i in range(swap[1]):
    y[i] = x[i]

y[swap[1]+1]=x[swap[2]]
j=1
for i in x - swap[1] - 1:
    if (x[i+swap[1]+1] == y[swap[1]+1]):
        i += 1
    y[j+swap[1]+1] = x[i+swap[1]+1]
    j += 1

for i in y:
    print(y[i])

