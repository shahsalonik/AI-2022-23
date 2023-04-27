import matplotlib.pyplot as plt
import random

plt.scatter([random.random() for x in range(100)], [random.random() for y in range(100)])
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.show()