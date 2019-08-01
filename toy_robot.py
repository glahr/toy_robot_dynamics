import numpy as np
import matplotlib.pyplot as plt
import math

L = 0.5  # m
m = 2  # kg
I = m*L*L/12 + m*L*L/4  #kg*m^2



theta_dd = []
theta_d = []
theta = []
error = []

n = 10000
Tmax = 20  # s
time = np.linspace(0,Tmax,n)
Tm = 1  # N*m
theta_desired = math.pi/3
Kp = 10
Kd = 1
A = math.pi/3
w = 1

for k in range(len(time)):
    if k == 0:
        theta_dd.append(0)
        theta_d.append(0)
        theta.append(0)
        error.append(theta_desired - theta[k])
    else:
        # error.append(theta_desired - theta[k-1])
        # error_d = (error[k] - error[k-1])/(time[k]-time[k-1])
        # u = Kp*error[k] + Kd*error_d
        # Tm = u
        Tm = A*math.sin(w*time[k])
        theta_dd.append(Tm/I)
        theta_d.append((theta_dd[k] + theta_dd[k-1])*(time[k]-time[k-1])/2 + theta_d[k-1])
        theta.append((theta_d[k] + theta_d[k-1])*(time[k]-time[k-1])/2 + theta[k-1])

plt.plot(time, theta)
# plt.plot(time, np.ones(len(time))*math.pi/3, '--')
plt.xlabel("Time [s]")
plt.ylabel("theta [rad]")
plt.grid()
plt.show()
