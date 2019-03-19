import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import data
x_dat = pd.read_csv("velocity_x.csv")
y_dat = pd.read_csv("velocity_y.csv")

# Plot initial data
init_x = np.array(x_dat.iloc[0][1:]).reshape((9, 9))
init_y = np.array(y_dat.iloc[0][1:]).reshape((9, 9))
plt.clf()
plt.quiver(init_x, init_y)
plt.savefig('plots/initial_quiver.png')

# Calculate average velocities
n = 9998
av_x = np.zeros((9,9))
av_y = np.zeros((9,9))
for i in range(n):
    av_x += np.array(x_dat.iloc[i][1:]).reshape((9, 9))
    av_y += np.array(y_dat.iloc[i][1:]).reshape((9, 9))
av_x /= 9998
av_y /= 9998

# Store averages
f = open('averages_alltime.txt', 'w+')
for i in range(9):
    for j in range(9):
        f.write('{:.4e}, {:.4e}\n'.format(av_x[i,j], av_y[i,j]))
f.close()

# Plot averages
plt.clf()
plt.contourf(av_x)
plt.title('Average x-velocity')
plt.colorbar()
plt.savefig('plots/average_x_alltime.png')
plt.clf()
plt.contourf(av_y)
plt.title('Average y-velocity')
plt.colorbar()
plt.savefig('plots/average_y_alltime.png')
plt.clf()
plt.quiver(av_x,av_y)
plt.title('Average velocity')
plt.savefig('plots/average_quiver_alltime.png')
