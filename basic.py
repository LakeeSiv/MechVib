from math import pi
import numpy as np
import matplotlib.pyplot as plt

# Input variables

f_signal = 80  # Hz

# Constants
f_n = 100  # Hz
w_n = 2 * pi * f_n  # rad s^-1
zeta = 0.03
T = 0.4
delta_t = 0.0003

t = np.arange(0, T, delta_t)
y_unit_imp_response = np.exp(-1 * zeta * w_n * t) * np.sin(w_n * t)
input_signal = np.sin(2 * pi * f_signal * t)
response = np.convolve(y_unit_imp_response, input_signal)

plt.style.use("seaborn")
fig, axs = plt.subplots(2, 1, figsize=(
    14, 7), gridspec_kw={'height_ratios': [1, 2]})
axs[0].plot(t, input_signal)
axs[0].set(xlabel="$time/ s$", ylabel="$X$")
axs[0].set_title(f"Input signal with $f={f_signal}Hz$")
axs[1].plot(t, response[0:1334])
axs[1].set(xlabel="$time/ s$", ylabel="$Y/X$")
axs[1].set_title(f"Response to input signal")
plt.tight_layout()
plt.show()
