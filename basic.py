from math import pi
import numpy as np
import matplotlib.pyplot as plt

f_n = 100  # Hz
w_n = 2*pi*f_n  # rad s^-1
zeta = 0.03
T = 0.4
delta_t = 0.0003

t = np.arange(0, T, delta_t)
y_unit_imp_response = np.exp(-1*zeta*w_n*t)*np.sin(w_n*t)
test_signal = np.sin(2*pi*80*t)
res = np.convolve(y_unit_imp_response, test_signal)
plt.plot(t, res[0:1334])
plt.show()
