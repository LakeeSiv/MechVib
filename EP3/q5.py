import numpy as np
from numpy.linalg import eig, inv

# --- inputs ------

# ratio of M/m
ratio = 1

# True if you want the answers to be rounded, making them more resonable
# False if you want to see the value calculated
rounding = True

# -----------------------

m = 1
M = m*ratio

K = np.array([[1, -1, 0],
              [-1, 2, -1],
              [0, -1, 1]])

M = np.array([[m, 0, 0],
              [0, M, 0],
              [0, 0, m]])

# A*Y = w^2*Y where A = M^-1*K
A = np.matmul(inv(M), K)

w, v = eig(A)
"""
w: vector containing eigenvals
v: matrix containing **normalized** eigenvectors
"""
for i in range(w.size):
    w_sq = w[i]
    e_vec = v[:, i]

    # unnormalize the vector
    u_e_vec = e_vec / e_vec[0]

    if rounding:
        w_sq = np.round(w_sq, 3)
        u_e_vec = np.round(u_e_vec, 3)

    print(f"""
    Mode {i+1}: eigenfreq squared = {w_sq} rad^2/s^2
            mode shape = {u_e_vec}
    """)
