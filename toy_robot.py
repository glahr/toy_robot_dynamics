import numpy as np
import matplotlib.pyplot as plt
import math

L = 0.5  # m
m = 2  # kg
I = m*L*L/12 + m*L*L/4  #kg*m^2



theta_dd = []
theta_d = []
theta = []

n = 100
Tmax = 3  # s
time = np.linspace(0,Tmax,n)
Tm = 1  # N*m

for k in range(len(time)):
    Tm = 1*math.sin(10*time[k])
    theta_dd.append(Tm/I)
    if k == 0:
        theta_d.append(0)
        theta.append(0)
    else:
        theta_d.append((theta_dd[k] + theta_dd[k-1])*(time[k]-time[k-1])/2 + theta_d[k-1])
        theta.append((theta_d[k] + theta_d[k-1])*(time[k]-time[k-1])/2 + theta[k-1])

plt.plot(time, theta)
plt.xlabel("Time [s]")
plt.ylabel("theta [rad]")
plt.show()
