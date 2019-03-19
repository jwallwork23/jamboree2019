import numpy as np

# Read averages from file
av_x = np.zeros((9, 9))
av_y = np.zeros((9, 9))
f = open('averages_alltime.txt', 'r')
for i in range(9):
    for j in range(9):
        av_x[i,j], av_y[i,j] = f.readline().split(',')
f.close()

# Forecasts for time level 19994, 19995 and 19996 ;)
forecast_19994_x = av_x
forecast_19995_x = av_x
forecast_19996_x = av_x
forecast_19994_y = av_y
forecast_19995_y = av_y
forecast_19996_y = av_y
