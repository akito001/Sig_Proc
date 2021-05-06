from scipy import signal
from matplotlib import pyplot as plt
window = signal.hann(51)
plt.plot(window)
plt.show()
