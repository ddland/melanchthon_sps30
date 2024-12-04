import numpy as np
import matplotlib.pyplot as plt
import os.path 
import glob

def per_dag(base_dir, col=1):
    """ Lees verscihllende datasets in, waarbij de meetdata uit de filenaam gehaald wordt
    
    argumenten:
       base_dir: directory waar files staan
        col: column nummer waar de data staat
    """
    alldata = []
    times = []
    for fh in sorted(glob.glob(os.path.join(base_dir, '*.csv'))):
        data = np.loadtxt(fh, delimiter=';', skiprows=1)
        alldata.append(data[:,col])
        # maand staat op positie 20:22 en dag op 22:24 van de filenaam + directory
        times.append(fh[20:22] +'-' + fh[22:24])
    return times, alldata


# maak tijd-as en datasets aan aan de hand van verschillende files in directory
mean_time, datasets = per_dag('melanchthon_001')

# creeer een figuur
fig, ax = plt.subplots(1)
ax.boxplot(datasets)

# teken een grid, label de assen
ax.grid()
ax.set_xlabel('tijd')
ax.set_ylabel('PM2.5 [ug/m]')
ax.set_xticklabels([x for x in mean_time], rotation=40)

plt.tight_layout()
# sla de data op
plt.savefig('figuur.pdf')
plt.show()

