from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

#signal1 sampling_rate 20000Hz

t = np.linspace(0,1.0,2001)

sig_5hz =  np.sin(2*np.pi*5*t)
sig_250hz =  np.sin(2*np.pi*250*t)

plt.plot(sig_5hz)
plt.show()
 

 ##show 2
 ##show 3