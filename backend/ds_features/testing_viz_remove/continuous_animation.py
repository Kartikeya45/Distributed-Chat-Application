import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))

def update(frame):
    line.set_ydata(np.random.rand(10))
    return line,

ani = FuncAnimation(fig, update, interval=100, blit=True, repeat=True)
plt.show()
