import numpy as np
import matplotlib.pyplot as plt
import os.path 
import glob

def per_file(base_dir, col=1):
    """ Lees verscihllende datasets in, waarbij de meetdata uit de filenaam gehaald wordt
    De eerste column is een tijdstamp, daarna zijn er colummen met data.
    
    argumenten:
       base_dir: directory waar files staan
       col: column nummer waar de data staat
    """
    alldata = []
    times = []
    for fh in sorted(glob.glob(os.path.join(base_dir, '*.csv'))):
        data = np.loadtxt(fh, delimiter=';', skiprows=1)
        alldata.append(data[:,col])
        times.append(np.mean(data[:,0])) # timestamps in col 0
    times = np.array(times).astype('datetime64[s]')
    return times, alldata


# maak tijd-as en datasets aan aan de hand van verschillende files in directory
mean_time, datasets = per_file('data', col=2)

# creeer een figuur
fig, ax = plt.subplots(1)
ax.boxplot(datasets, tick_labels=mean_time)

# teken een grid, label de assen
ax.grid()
ax.set_xlabel('activiteit')
ax.set_ylabel('PM2.5 [ug/m]')

# labels met een gemiddelde tijd
#ax.set_xticklabels([x.item().strftime('%m-%d')  # maand-dag
#                    for x in mean_time], rotation=40)
# labels met tekst passend bij files
ax.set_xticklabels(['achtergrond binnen', 'kaars binnen','buiten'], rotation=40)
#fig.autofmt_xdate()
plt.tight_layout()
# sla de data op
plt.savefig('boxplot.jpg')
plt.show()

