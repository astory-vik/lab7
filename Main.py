from numpy import *
import matplotlib.pyplot as plt
x = [-2, -1, 0, 1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(i * math.sin(5 * i))

plt.plot(x, y)
plt.savefig('graph.png', dpi=200)