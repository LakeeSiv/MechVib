from math import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

init_f_signal = 80  # Hz

# Constants
f_n = 100  # Hz
w_n = 2 * pi * f_n  # rad s^-1
zeta = 0.03
T = 0.4
delta_t = 0.0003

t = np.arange(0, T, delta_t)
y_unit_imp_response = np.exp(-1 * zeta * w_n * t) * np.sin(w_n * t)


plt.style.use("seaborn")
fig, axs = plt.subplots(2, 1, figsize=(
    14, 7), gridspec_kw={'height_ratios': [1, 2]})


def plot_input(f):
    input_signal = np.sin(2 * pi * f * t)
    axs[0].plot(t, input_signal)
    axs[0].set(ylabel="$X$")
    axs[0].set_title(f"Input signal with $f={round(f,2)}Hz$")


def plot_response(f):
    input_signal = np.sin(2 * pi * f * t)
    response = np.convolve(y_unit_imp_response, input_signal)
    axs[1].plot(t, response[0:1334])
    axs[1].set(xlabel="$time/ s$", ylabel="$Y/X$")
    axs[1].set_title(f"Response to input signal")


plot_input(init_f_signal)
plot_response(init_f_signal)

axfreq = plt.axes([0.25, .95, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Input Frequency/Hz',
    valmin=50,
    valmax=200,
    valinit=init_f_signal,
)


def update(val):

    axs[0].clear()
    axs[1].clear()
    plot_input(freq_slider.val)
    plot_response(freq_slider.val)
    fig.canvas.draw_idle()


freq_slider.on_changed(update)


plt.show()
