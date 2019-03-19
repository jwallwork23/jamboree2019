import pandas as pd
import numpy as np
import statistics as stat
import matplotlib as mpl
import matplotlib.pyplot as plt

x_dat = pd.read_csv("velocity_x.csv")
y_dat = pd.read_csv("velocity_y.csv")

time_nr = len(x_dat)
xdat = np.zeros((time_nr,9,9))
ydat = np.zeros((time_nr,9,9))
for i in range(0,time_nr):
    xdat[i] = np.array( x_dat.iloc[i][1::] ).reshape(9,9)
    ydat[i] = np.array( y_dat.iloc[i][1::] ).reshape(9,9)

x_av = np.average( xdat, axis=0 )
y_av = np.average( ydat, axis=0 )

# x_var = np.var( xdat, axis=0 )
# y_var = np.var( ydat, axis=0 )

x_cov = np.cov( xdat.reshape(time_nr,81), rowvar=False )
y_cov = np.cov( ydat.reshape(time_nr/2,81), rowvar=False  )

x_est = x_av.reshape(81)
y_est = y_av.reshape(81)


### Plot covariance ###

# plt.contourf( x_cov )
# plt.colorbar()
# plt.savefig('plots/cov_x')
# plt.show()

# plt.contourf( y_cov )
# plt.colorbar()
# plt.savefig('plots/cov_y')
# plt.show()

# cbar_max = 0.1
# cbar_min = -0.1
# cbar_step = 0.01
# cbar_nr = int( cbar_max /cbar_step)
# cbar_tick = np.arange( cbar_min, cbar_max+cbar_step, cbar_step )
#
# plt.contourf(x_av, cbar_tick, cmap = plt.cm.get_cmap('viridis',cbar_nr), vmin=cbar_min, vmax=cbar_max)
# plt.title( 'Average in x direction' )
# plt.colorbar( ticks=cbar_tick )
# plt.savefig("plots/average_x2.png")
# plt.show()
#
# plt.contourf(y_av, cbar_tick, cmap = plt.cm.get_cmap('viridis',cbar_nr), vmin=cbar_min, vmax=cbar_max)
# plt.title( 'Average in y direction')
# plt.colorbar(ticks=cbar_tick )
# plt.savefig("plots/average_y2.png")
# plt.show()


### Plot variance in contours ###

# cbar_max = 0.002
# cbar_min = 0
# cbar_step = 0.00025
# cbar_nr = int( cbar_max /cbar_step)
# cbar_tick = np.arange( cbar_min, cbar_max+cbar_step, cbar_step )
#
# plt.contourf(x_var, cbar_tick, cmap = plt.cm.get_cmap('viridis',cbar_nr), vmin=cbar_min, vmax=cbar_max)
# plt.title( 'Variance in x direction' )
# plt.colorbar( ticks=cbar_tick )
# plt.savefig("plots/variance_x2.png")
# plt.show()
#
# plt.contourf(y_var, cbar_tick, cmap = plt.cm.get_cmap('viridis',cbar_nr), vmin=cbar_min, vmax=cbar_max)
# plt.title( 'Variance in y direction')
# plt.colorbar(ticks=cbar_tick )
# plt.savefig("plots/variance_y2.png")
# plt.show()
