import numpy as np
import matplotlib.pyplot as plt

# lees data
data = np.loadtxt('data/03_buiten.csv',
                  delimiter=';',
                  skiprows=1)

# creeer een tijds-as
t = np.asarray(data[:,0], dtype='datetime64[s]')

# plot de eerste column uitgezet tegen de tijd
plt.plot(t, data[:,1], label='PM 1.0')
plt.plot(t, data[:,2], label='PM 2.5')
plt.plot(t, data[:,3], label='PM 4.0')
plt.plot(t, data[:,4], label='PM 10')

# teken grid, assen
plt.grid()
plt.xlabel('tijd')
plt.ylabel('fijnstof [ug/m]')
plt.legend(loc=0)
plt.gcf().autofmt_xdate()

# sla het figuur op
plt.savefig('simple_fig.pdf')
plt.show()
