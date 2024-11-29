import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y1 = np.sin(x)          
y2 = np.exp(x / 3)     

fig, ax1 = plt.subplots()


ax1.plot(x, y1, 'b-', label='Sine Wave')
ax1.set_xlabel('X-axis (Common)')
ax1.set_ylabel('Y1: Sine Wave', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r--', label='Exponential Growth')
ax2.set_ylabel('Y2: Exponential', color='r')
ax2.tick_params(axis='y', labelcolor='r')


fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))


plt.title("Multiple Y-Axes Sharing a Common X-Axis")
plt.show()
