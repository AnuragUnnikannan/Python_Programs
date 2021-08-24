import pandas as pd
from matplotlib import pyplot as plt
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("Test Plot")
plt.xlabel("X")
plt.ylabel("Y and Z")
plt.legend(["This is y", "This is z"])
plt.show()