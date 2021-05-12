
import numpy as np


def unit_imp_resp(t, zeta, w_n):
    """
    values returned are y/w_n
    """
    return np.exp(-1*zeta*w_n*t)*np.sin(w_n*t)
