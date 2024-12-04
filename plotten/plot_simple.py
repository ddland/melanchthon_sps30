import numpy as np
import matplotlib.pyplot as plt

# lees data
data = np.loadtxt('melanchthon_001/20241123.csv',
                  delimiter=';',
                  skiprows=1)

# creeer een tijds-as
t = np.asarray(data[:,0], dtype='datetime64[s]')

# plot de eerste column uitgezet tegen de tijd
plt.plot(t, data[:,1])

# teken grid, assen
plt.grid()
plt.xlabel('tijd')
plt.ylabel('PM2.5 [ug/m]')
plt.gcf().autofmt_xdate()

# sla het figuur op
plt.savefig('simple_fig.pdf')
plt.show()
