from matplotlib import pyplot
import numpy 
from textwrap import wrap
import matplotlib.ticker as ticker

with open('settings.txt') as file: 
    settings = [float(i) for i in file.read().split('\n')]

data = numpy.loadtxt('data.txt', dtype = int) * settings[1]
data_time = numpy.array([i*settings[0] for i in range(data.size)]) 

fig, ax = pyplot.subplots(figsize=(16,10), dpi= 500)
ax.set_title('U(t) of RC', fontsize = 20)
ax.axis([data_time.min(), data_time.max() + 1, data.min(), data.max() + 0.2])
ax.set_ylabel('U, Вольты', fontsize = 20)
ax.set_xlabel('t, Секунды', fontsize = 20)

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.grid(which = 'major', color = 'black')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'blue', linestyle = ':')

ax.plot(data_time, data, c = 'black', linewidth = 1, label = 'U(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 's', c = 'blue', s = 10)

ax.legend(shadow = False, loc = 'upper right', fontsize = 30)
ax.text(6, 2.25, 'Время зарядки ~ 6.1с', fontsize = 25)
ax.text(6, 1.75, 'Время разрядки ~ 6.9с', fontsize = 25)

fig.savefig('U(t).svg')
fig.savefig('U(t).png')
