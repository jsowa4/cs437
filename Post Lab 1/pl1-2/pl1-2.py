from sense_hat import SenseHat
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

sense=SenseHat()
time = np.arange(10)
temperature_nr = []
temperature_r = []
temperature_avg = []


for i in range(10):
    temperature_nr.append(sense.get_temperature())
    sleep(1)
    
for i in range(10):
    temperature_r.append(round(sense.get_temperature(), 1))
    sleep(1)

for i in range(10):
    start = max(i-2, 0)
    end = min(i+2, 9)
    total = 0
    for j in range(start, end, 1):
        total += temperature_nr[j]
    temperature_avg.append(total * 1. / (end - start))
        

     
print(time)
print(temperature_nr)
print(temperature_r)
print(temperature_avg)

fig, ax = plt.subplots()
fig.suptitle('Temperature vs Time')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature')
ax.plot(time, temperature_nr, label='Not Rounded')
ax.plot(time, temperature_r, label='Rounded')
ax.plot(time, temperature_avg, label='Average')
ax.legend()
plt.show()