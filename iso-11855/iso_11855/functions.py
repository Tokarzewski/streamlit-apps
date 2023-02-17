from math import exp, log, sqrt, prod, e, pi
import numpy as np
from scipy.interpolate import CubicSpline, interp2d, interpn


def q1(t_S_m, t_i):
    """Function 1 - Heat flux for floor heating and ceiling cooling."""
    return 8.92 * (t_S_m - t_i) ^ 1.1


def q2(t_S_m, t_i):
    """Function 2 - Heat flux for wall heating and cooling."""
    return 8 * abs(t_S_m - t_i)


def q3(t_S_m, t_i):
    """Function 3 - Heat flux for ceiling heating."""
    return 6 * abs(t_S_m - t_i)


def q4(t_S_m, t_i):
    """Function 4 - Heat flux for floor cooling."""
    return 7 * abs(t_S_m - t_i)


def power_product(a_i, m_i) -> float:
    return prod([a**m for a, m in zip(a_i, m_i)])


def q5(B, a_i, m_i, deltat_H):
    """Function 5 - Universal single power heat flux function."""
    return B * power_product(a_i, m_i) * deltat_H


def q_des(h_t, t_S_m, t_i):
    """Function 6 - Heat flux for heating and cooling."""
    return h_t * abs(t_S_m - t_i)


# Annex A - Calculation of the heat flux


def deltat_H(t_V, t_R, t_i):
    """Function A.1 - Temperature difference
    between heating fluid and room."""
    return (t_V - t_R) / log((t_V - t_i) / (t_R - t_i))


# Function A.2 = Function 5


def q6(a_B, a_W, a_U, a_D, m_W, m_U, m_D, deltat_H, B=6.7):
    """Function A.3 - Heat flux for system types A, C, H, I, J."""
    a_i = [a_B, a_W, a_U, a_D]
    m_i = [1, m_W, m_U, m_D]
    return q5(B, a_i, m_i, deltat_H)


def a_B1(alfa, k_E, R_k_B):
    """Function A.4 - Surface covering factor for system types A, C, H, I, J."""
    s_u_0 = 0.045
    k_u_0 = 1
    return (1 / alfa + s_u_0 / k_u_0) / (1 / alfa + s_u_0 / k_E + R_k_B)


def m_W(W):
    """Function A.5 - Exponent m_W for system types A, B, C, H, I, J."""
    return 1 - W / 0.075


def m_U(s_u):
    """Function A.6 - Exponent m_U."""
    return 100 * (0.045 - s_u)


def m_D(D):
    """Function A.7 - Exponent m_D."""
    return 250 * (D - 0.02)


def K_H1(a_i, m_i, s_u, s_u_star, lambda_E):
    """Function A.8 - Heat transfer coefficient."""
    return 1 / (1 / power_product(a_i, m_i) + (s_u - s_u_star) / lambda_E)


def q7(K_H, deltat_H):
    """Function A.9 - Heat flux."""
    return K_H * deltat_H


def q8(q_0375, W):
    """Function A.10 - Heat flux for pipe spacing W > 0.375 m for system types A, C, H, I, J."""
    return q_0375 * 0.375 / W


def q9(a_B, a_W, a_U, a_WL, a_K, m_W, deltat_H, B=6.5):
    """Function A.11 - Heat flux for system type B."""
    a_i = [a_B, a_W, a_U, a_WL, a_K]
    m_i = [1, m_W, 1, 1, 1]
    return q5(B, a_i, m_i, deltat_H)


def a_B2(a_U, a_W, m_W, a_WL, a_K, R_k_B, W, B=6.5):
    """Function A.12 - Surface covering factor for system type B."""
    return 1 / (1 + B * a_U * a_W**m_W * a_WL * a_K * R_k_B * (1 + 0.44 * sqrt(W)))


def a_U2(alfa, s_u, k_E):
    """Function A.13 - Covering factor for system types B and D."""
    s_u_0 = 0.045
    k_u_o = 1
    return (1 / alfa + s_u_0 / k_u_o) / (1 / alfa + s_u / k_E)


# Function A.14 = A.5


def K_WL(s_WL, k_WL, b_u, s_u, k_E):
    """
    Function A.15 - Characteristic value for heat conducting device.
    Arguments:
    s_WL - thickness of the heat conducting material,
    k_WL - thermal conductivity of the heat conducting material,
    b_u - correction factor depending on the pipe spacing from table A.17,
    s_u - thickness of the screed,
    k_E - thermal conductivity of the screed.
    """
    return (s_WL * k_WL + b_u * s_u * k_E) * 8


def a_WL1(a_WL, a_0, L_WL, W):
    """Function A.16 - Corrected heat conduction device factor for system type B."""
    x = L_WL / W
    return a_WL - (a_WL - a_0) * (1 - 3.2 * x + 3.4 * x * x - 1.2 * x * x * x)


def q10(a_B, a_U, deltat_H, B=6.5):
    """Function A.17 - Heat flux for system type D."""
    a_i = [a_B, 1.06, a_U]
    m_i = [1, 1, 1]
    return q5(B, a_i, m_i, deltat_H)
    # return B * a_B * 1.06 * a_U * deltat_H


def a_B3(a_U, R_k_B):
    """Function A.18 - Surface covering factor for system type D."""
    B = 6.5
    return 1 / (1 + B * a_U * 1.06 * R_k_B)


def q_G1(fi, B_G, deltat_H, n_G):
    """Function A.19 - Limit curve of heat flux."""
    return fi * B_G * (deltat_H / fi) ** n_G


def fi(t_F_max, t_i, deltat_o=9):
    """Function A.20 - Factor for conversion to any values."""
    return ((t_F_max - t_i) / deltat_o) ** 1.1


def deltat_H_G(fi, B_G, B, a_i, m_i, n_G):
    """Function A.21 - The intersection of the characteristic curve with the limit curve."""
    return fi * (B_G / (B * power_product(a_i, m_i))) ** (1 / (1 - n_G))


def q_G2(q_G_0375, W, f_G):
    """Function A.22 - Limit curve of heat flux for type A and C system types where W > 0.375 m."""
    return q_G_0375 * 0.375 / W * f_G


def deltat_H_G(t_H_G_0375, f_G):
    """Function A.23 - The limit tempertature difference between the heating medium and the room."""
    return t_H_G_0375 * f_G


def f_G(s_u, W, q_G_max, q_G_0375):
    """Function A.24 -"""
    if s_u / W > 0.173:
        x = q_G_0375 * 0.375 / W
        return (q_G_max - (q_G_max - x) * e ** (-20 * (s_u / W - 0.173) ** 2)) / x
    else:
        return 1


def q_G3(a_WL, a_WL_W, q_G_W):
    """Function A.25 - Correction formula for system type B."""
    return a_WL / a_WL_W * q_G_W


def B1(B_0, a_i, m_i, W, k_R, d_a, s_R):
    """
    Function A.26 - Influence of material and thickness factor without sheathing.
    Arguments:
    B_0 - default influence factor depending on the system type,
    W - pipe spacing
    k_R - pipe material,
    s_R - pipe wall thickness.
    """
    k_R_0 = 0.35
    s_R_0 = 0.002
    x = 1 / B_0 + 1.1 / pi * power_product(a_i, m_i) * W * (
        1 / (2 * k_R) * log(d_a / (d_a - 2 * s_R))
        - 1 / (2 * k_R_0) * log(d_a / (d_a - 2 * s_R_0))
    )
    return 1 / x


def B2(B_0, a_i, m_i, W, k_R, d_a, s_R, k_M, d_M):
    """
    Function A.27 - Influence of material and thickness factor with sheathing.
    Arguments:
    B_0 - default influence factor depending on the system type,
    W - pipe spacing
    k_R - pipe material,
    s_R - pipe wall thickness,
    k_M - sheathing material,
    d_M - sheathing thickness.
    """
    k_R_0 = 0.35
    s_R_0 = 0.002
    x = 1 / B_0 + 1.1 / pi * power_product(a_i, m_i) * W * (
        1 / (2 * k_M) * log(d_M / d_a)
        + 1 / (2 * k_R) * log(d_a / (d_a - 2 * s_R))
        - 1 / (2 * k_R_0) * log(d_M / (d_M - 2 * s_R_0))
    )
    return 1 / x


def k_E_prim(psi, k_E, k_W):
    """Function A.28 - Thermal conductivity of screed with fixing inserts."""
    return (1 - psi) * k_E + psi * k_W


def q_U1(R_u, R_o, q, t_i, t_u):
    """Function A.29 - Downward heat loss."""
    return 1 / R_u * (R_o * q + t_i - t_u)


def R_o(R_k_B, s_u, k_u, alfa=10.8):
    """Function A.30 - Upwards partial heat transmission
    resistance of the floor structure."""
    return 1 / alfa + R_k_B + s_u / k_u


def R_u(R_k_ins, R_k_construction, R_k_plaster, R_alfa):
    """Function A.31 - Downwards partial heat transmission
    resistance of the floor structure."""
    return R_k_ins + R_k_construction + R_k_plaster + R_alfa


def q_U2(q, R_o, R_u):
    """Function A.32 - Downward heat loss when t_i == t_u."""
    return q * R_o / R_u


def K_H2(K_H_Floor, deltaR_alfa, R_k_B, K_H_Floor_star, R_k_B_star=0.15):
    """Function A.33 - Equivalent heat transmission coefficient."""
    return K_H_Floor / (
        1 + ((deltaR_alfa + R_k_B) / R_k_B_star) * (K_H_Floor / K_H_Floor_star - 1)
    )


# Function A.34 = A.9


def deltaR_h(alfa):
    """Function A.35 - Additional thermal transfer resistance."""
    return 1 / alfa - 1 / 10.8


def a_W1(R_k_B):
    """Table A.2 - Pipe spacing factor for system types A, C, H, I, J."""
    x_R_k_B = [0.0, 0.05, 0.1, 0.15]
    y_a_W = [1.23, 1.188, 1.156, 1.134]
    cs = CubicSpline(x_R_k_B, y_a_W)

    """
    import matplotlib.pyplot as plt
    import numpy as np
    xs = np.arange(0, 0.15, 0.01)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xs, cs(xs), label="CubicSpline")
    ax.legend(loc='lower left', ncol=2)
    plt.show()
    """
    return cs(R_k_B)


def a_U1(R_k_B, W):
    """Table A.3 - Covering factor for system types A, C, H, I, J."""

    x_R_k_B = [0.0, 0.05, 0.1, 0.15]
    y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]
    z_a_U = [
        [1.069, 1.056, 1.043, 1.037],
        [1.066, 1.053, 1.041, 1.035],
        [1.063, 1.050, 1.039, 1.0335],
        [1.057, 1.046, 1.035, 1.0305],
        [1.051, 1.041, 1.0315, 1.0275],
        [1.048, 1.038, 1.0295, 1.026],
        [1.0395, 1.031, 1.024, 1.021],
        [1.03, 1.0221, 1.0181, 1.015],
    ]
    cs = interp2d(x_R_k_B, y_W, z_a_U, kind="cubic")
    return float(cs(R_k_B, W))


def a_D(R_k_B, W):
    """Table A.4 - Pipe external diameter factor for system types A, C, H, I, J."""

    x_R_k_B = [0.0, 0.05, 0.1, 0.15]
    y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]
    z_a_D = [
        [1.013, 1.013, 1.012, 1.011],
        [1.021, 1.019, 1.016, 1.014],
        [1.029, 1.025, 1.022, 1.018],
        [1.040, 1.034, 1.029, 1.024],
        [1.046, 1.040, 1.035, 1.030],
        [1.049, 1.043, 1.038, 1.033],
        [1.053, 1.049, 1.044, 1.039],
        [1.056, 1.051, 1.046, 1.042],
    ]
    cs = interp2d(x_R_k_B, y_W, z_a_D, kind="cubic")
    return float(cs(R_k_B, W))


def B_G1(s_u, k_E, W):
    """Table A.5 - Coefficient for s_u/k <= 0.792 for system types A, C, H, I, J."""

    x_s_u_k_E = [0.01, 0.0208, 0.0292, 0.0375, 0.0458, 0.0542, 0.0625, 0.0708, 0.0792]
    y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375]
    z_B_G = [
        [85.0, 91.5, 96.8, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
        [75.3, 83.5, 89.9, 96.3, 99.5, 100.0, 100.0, 100.0, 100.0],
        [66.0, 75.4, 82.9, 89.3, 95.5, 98.8, 100.0, 100.0, 100.0],
        [51.0, 61.1, 69.2, 76.3, 82.7, 87.5, 91.8, 95.1, 97.8],
        [38.5, 48.2, 56.2, 63.1, 69.1, 74.5, 81.3, 86.4, 90.0],
        [33.0, 42.5, 49.5, 56.5, 62.0, 67.5, 75.3, 81.6, 86.1],
        [20.5, 26.8, 31.6, 36.4, 51.5, 47.5, 57.5, 65.3, 72.4],
        [11.5, 13.7, 15.5, 18.2, 21.5, 27.5, 40.0, 49.1, 58.3],
    ]
    cs = interp2d(x_s_u_k_E, y_W, z_B_G, kind="cubic")
    return float(cs(s_u / k_E, W))


def B_G2(s_u, W):
    """Table A.6 - Coefficient for s_u/k > 0.792 for system types A, C, H, I, J."""
    x = s_u / W
    if x <= 0.7:
        x_s_u_W = [0.173, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
        y_B_G = [27.5, 40, 57.5, 69.5, 78.2, 84.5, 88.3, 91.6, 94, 96.3, 98.6, 99.8]
        cs = CubicSpline(x_s_u_W, y_B_G)
        return cs(x)
    else:
        return 100.0


def n_G1(s_u, k_E, W):
    """Table A.7 - Exponent for s_u/k <= 0.792 for system types A, C, H, I, J."""

    x_s_u_k_E = [0.01, 0.0208, 0.0292, 0.0375, 0.0458, 0.0542, 0.0625, 0.0708, 0.0792]
    y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.2625, 0.3, 0.3375, 0.375]
    z_n_G = [
        [0.008, 0.005, 0.002, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.024, 0.021, 0.018, 0.011, 0.002, 0.0, 0.0, 0.0, 0.0],
        [0.046, 0.043, 0.041, 0.033, 0.014, 0.005, 0.0, 0.0, 0.0],
        [0.088, 0.085, 0.082, 0.076, 0.055, 0.038, 0.024, 0.014, 0.006],
        [0.131, 0.130, 0.129, 0.123, 0.105, 0.083, 0.057, 0.040, 0.028],
        [0.155, 0.154, 0.153, 0.146, 0.130, 0.110, 0.077, 0.056, 0.041],
        [0.197, 0.196, 0.196, 0.190, 0.173, 0.150, 0.110, 0.083, 0.062],
        [0.254, 0.253, 0.253, 0.245, 0.228, 0.195, 0.145, 0.114, 0.086],
        [0.322, 0.321, 0.321, 0.310, 0.293, 0.260, 0.187, 0.148, 0.115],
        [0.422, 0.421, 0.421, 0.405, 0.385, 0.325, 0.230, 0.183, 0.142],
    ]
    cs = interp2d(x_s_u_k_E, y_W, z_n_G, kind="cubic")
    return float(cs(s_u / k_E, W))


def n_G2(s_u, W):
    """Table A.8 - Exponent for s_u/k > 0.792 for system types A, C, H, I, J."""
    x = s_u / W
    if x <= 0.7:
        x_s_u_W = [0.173, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
        y_n_G = [0.32,0.23,0.145,0.097,0.067,0.048,0.033,0.023,0.015,0.009,0.005,0.002]
        cs = CubicSpline(x_s_u_W, y_n_G)
        return cs(x)
    else:
        return 0.0


def a_W2(s_u, k_E):
    """Table A.9 - Pipe spacing factor for system type B."""
    x_s_u_k_E = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15, 0.18]
    y_a_W = [1.103, 1.1, 1.097, 1.094, 1.091, 1.088, 1.082, 1.075, 1.064, 1.059]
    cs = CubicSpline(x_s_u_k_E, y_a_W)
    return cs(s_u / k_E)


def b_u(W):
    """Table A.10 - Pipe spacing factor for system type B."""
    if W <= 0.1:
        return 1.0
    elif W < 0.45:
        x_W = [0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
        y_b_u = [1.0, 0.7, 0.5, 0.43, 0.25, 0.1, 0.0]
        cs = CubicSpline(x_W, y_b_u)
        return cs(W)
    else:
        return 0.0


def a_WL2(K_WL, W, D):
    """Tables A.11 - A.15 - Heat conduction device factor for system type B."""
    x_K_WL = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
    z_D = [0.014, 0.016, 0.018, 0.020, 0.022]
    a_WL = [
        [  # Table A.11 for K_WL = 0.0
            [0.82, 0.86, 0.9, 0.93, 0.96],
            [0.59, 0.644, 0.7, 0.754, 0.8],
            [0.488, 0.533, 0.576, 0.617, 0.658],
            [0.387, 0.415, 0.444, 0.47, 0.505],
            [0.337, 0.357, 0.379, 0.4, 0.422],
            [0.32, 0.34, 0.357, 0.376, 0.396],
            [0.288, 0.3, 0.315, 0.33, 0.344],
            [0.266, 0.278, 0.29, 0.3, 0.312],
            [0.25, 0.264, 0.28, 0.29, 0.3],
        ],
        [  # Table A.12 for K_WL = 0.1
            [0.88, 0.905, 0.93, 0.955, 0.975],
            [0.74, 0.776, 0.812, 0.836, 0.859],
            [0.66, 0.693, 0.726, 0.76, 0.77],
            [0.561, 0.58, 0.6, 0.621, 0.642],
            [0.49, 0.51, 0.53, 0.55, 0.57],
            [0.467, 0.485, 0.504, 0.522, 0.54],
            [0.435, 0.444, 0.453, 0.462, 0.472],
            [0.411, 0.421, 0.434, 0.446, 0.46],
            [0.41, 0.42, 0.43, 0.44, 0.45],
        ],
        [  # Table A.13 for K_WL = 0.2
            [0.92, 0.937, 0.955, 0.97, 0.985],
            [0.845, 0.865, 0.885, 0.893, 0.902],
            [0.81, 0.821, 0.832, 0.843, 0.855],
            [0.735, 0.745, 0.755, 0.765, 0.775],
            [0.68, 0.688, 0.695, 0.703, 0.71],
            [0.655, 0.663, 0.67, 0.678, 0.685],
            [0.585, 0.592, 0.6, 0.608, 0.615],
            [0.55, 0.558, 0.565, 0.573, 0.58],
            [0.55, 0.555, 0.56, 0.565, 0.57],
        ],
        [  # Table A.14 for K_WL = 0.3
            [0.95, 0.96, 0.97, 0.98, 0.99],
            [0.92, 0.925, 0.93, 0.935, 0.94],
            [0.9, 0.905, 0.91, 0.915, 0.92],
            [0.855, 0.855, 0.855, 0.855, 0.855],
            [0.8, 0.8, 0.8, 0.8, 0.8],
            [0.79, 0.79, 0.79, 0.79, 0.79],
            [0.72, 0.72, 0.72, 0.72, 0.72],
            [0.69, 0.69, 0.69, 0.69, 0.69],
            [0.68, 0.68, 0.68, 0.68, 0.68],
        ],
        [  # Table A.15 for K_WL = 0.4
            [0.97, 0.978, 0.985, 0.99, 0.995],
            [0.965, 0.964, 0.963, 0.962, 0.96],
            [0.94, 0.94, 0.94, 0.94, 0.94],
            [0.895, 0.895, 0.895, 0.895, 0.895],
            [0.86, 0.86, 0.86, 0.86, 0.86],
            [0.84, 0.84, 0.84, 0.84, 0.84],
            [0.78, 0.78, 0.78, 0.78, 0.78],
            [0.76, 0.76, 0.76, 0.76, 0.76],
            [0.75, 0.75, 0.75, 0.75, 0.75],
        ],
        [  # Table A.16 for K_WL >= 0.5
            [0.995, 0.995, 0.995, 0.995, 0.995],
            [0.979, 0.979, 0.979, 0.979, 0.979],
            [0.963, 0.963, 0.963, 0.963, 0.963],
            [0.924, 0.924, 0.924, 0.924, 0.924],
            [0.894, 0.894, 0.894, 0.894, 0.894],
            [0.88, 0.88, 0.88, 0.88, 0.88],
            [0.83, 0.83, 0.83, 0.83, 0.83],
            [0.815, 0.815, 0.815, 0.815, 0.815],
            [0.81, 0.81, 0.81, 0.81, 0.81],
        ],
    ]
    points = (x_K_WL, y_W, z_D)
    point = np.array([K_WL, W, D])
    # xyz change linear interpolation to quadratic spline
    return float(interpn(points, a_WL, point, method="linear", bounds_error=False))


def a_WL_inf(W):
    """Table A.16 - Single column for K_WL = infinity."""
    x_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
    y_a_WL_inf = [1, 1.01, 1.02, 1.04, 1.06, 1.07, 1.09, 1.1, 1.1]
    cs = CubicSpline(x_W, y_a_WL_inf)
    return cs(W)


def a_WL3(K_WL, W, D):
    """Table A.16 - Heat conduction device factor for system type B, K_WL >= 0.5"""
    if K_WL > 1:
        a_WL_KL_inf = a_WL_inf(W)
        a_WL_KL_0 = a_WL2(K_WL=0, W=W, D=D)
        return (
            a_WL_KL_inf
            - (a_WL_KL_inf - a_WL_KL_0)
            * ((a_WL_KL_inf - 1) / (a_WL_KL_inf - a_WL_KL_0)) ** K_WL
        )

    else:  # 0.5 <= K_WL <= 1
        x_K_WL = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        y_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
        z_a_WL = [
            [0.995, 0.998, 1.0, 1.0, 1.0, 1.0],
            [0.979, 0.984, 0.99, 0.995, 0.998, 1.0],
            [0.963, 0.972, 0.98, 0.988, 0.995, 1.0],
            [0.924, 0.945, 0.96, 0.974, 0.99, 1.0],
            [0.894, 0.921, 0.943, 0.961, 0.98, 1.0],
            [0.88, 0.908, 0.934, 0.955, 0.975, 1.0],
            [0.83, 0.87, 0.91, 0.94, 0.97, 1.0],
            [0.815, 0.86, 0.9, 0.93, 0.97, 1.0],
            [0.81, 0.86, 0.9, 0.93, 0.97, 1.0],
        ]
        cs = interp2d(x_K_WL, y_W, z_a_WL, kind="cubic")
        return float(cs(K_WL, W))


def a_K(W):
    """Table A.17 - Correction factor for the contact for system type B."""
    x_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
    y_a_K = [1.0, 0.99, 0.98, 0.95, 0.92, 0.9, 0.82, 0.72, 0.60]
    cs = CubicSpline(x_W, y_a_K)
    return cs(W)


def B_G3(K_WL, W):
    """Table A.18 - Coefficient for system type B."""
    x_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
    y_K_WL = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    z_B_G = [
        [92.0, 86.7, 79.4, 64.8, 50.8, 45.8, 27.5, 9.9, 0.0],
        [93.1, 88.0, 81.3, 67.5, 54.2, 49.0, 31.8, 15.8, 2.4],
        [94.2, 89.5, 83.3, 70.2, 57.6, 52.5, 36.0, 21.3, 7.0],
        [95.4, 90.7, 85.2, 72.9, 60.8, 56.0, 40.2, 25.7, 11.9],
        [96.6, 92.1, 87.2, 75.6, 64.1, 59.3, 44.4, 30.0, 16.6],
        [97.8, 93.7, 89.2, 78.3, 67.3, 62.6, 48.6, 34.1, 21.1],
        [98.7, 95.0, 91.0, 81.0, 70.6, 66.3, 52.8, 38.5, 25.5],
        [99.3, 96.3, 93.0, 83.7, 74.0, 69.7, 57.0, 42.8, 29.6],
        [99.8, 97.7, 95.0, 86.3, 77.2, 73.0, 61.2, 47.0, 33.6],
        [100, 98.5, 96.5, 89.0, 80.7, 76.6, 65.4, 51.4, 37.3],
        [100, 99.3, 97.8, 91.5, 84.0, 80.0, 69.4, 55.6, 40.9],
        [100, 99.6, 98.5, 93.8, 87.2, 83.3, 73.2, 59.8, 44.3],
        [100, 99.8, 99.3, 95.8, 90.0, 86.3, 76.6, 63.8, 47.5],
        [100, 100, 99.8, 97.5, 92.5, 89.0, 80.0, 67.3, 50.5],
        [100, 100, 100, 98.6, 94.8, 91.7, 83.0, 71.0, 53.4],
    ]
    cs = interp2d(x_W, y_K_WL, z_B_G, kind="cubic")
    return float(cs(W, K_WL))


def n_G3(K_WL, W):
    """Table A.19 - Exponent for system type B."""
    x_W = [0.05, 0.075, 0.1, 0.15, 0.2, 0.225, 0.3, 0.375, 0.45]
    y_K_WL = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    z_n_G = [
        [0.0029, 0.017, 0.032, 0.067, 0.122, 0.151, 0.235, 0.333, 1.0],
        [0.0024, 0.015, 0.027, 0.055, 0.097, 0.12, 0.184, 0.288, 0.725],
        [0.0021, 0.013, 0.024, 0.048, 0.086, 0.104, 0.169, 0.256, 0.482],
        [0.0018, 0.012, 0.022, 0.044, 0.08, 0.095, 0.156, 0.228, 0.38],
        [0.0015, 0.011, 0.02, 0.04, 0.074, 0.088, 0.143, 0.204, 0.31],
        [0.0012, 0.0099, 0.018, 0.037, 0.067, 0.082, 0.131, 0.183, 0.25],
        [0.0009, 0.0087, 0.016, 0.033, 0.061, 0.074, 0.118, 0.162, 0.21],
        [0.0006, 0.0074, 0.014, 0.03, 0.055, 0.067, 0.106, 0.144, 0.187],
        [0.0003, 0.0062, 0.012, 0.027, 0.049, 0.06, 0.095, 0.126, 0.165],
        [0.0, 0.005, 0.01, 0.024, 0.044, 0.053, 0.083, 0.11, 0.143],
        [0.0, 0.0038, 0.008, 0.021, 0.038, 0.046, 0.072, 0.096, 0.121],
        [0.0, 0.0025, 0.006, 0.018, 0.032, 0.038, 0.063, 0.084, 0.107],
        [0.0, 0.0012, 0.004, 0.015, 0.027, 0.034, 0.054, 0.073, 0.093],
        [0.0, 0.0, 0.002, 0.012, 0.022, 0.029, 0.047, 0.063, 0.080],
        [0.0, 0.0, 0.0, 0.009, 0.02, 0.025, 0.04, 0.055, 0.07],
    ]
    cs = interp2d(x_W, y_K_WL, z_n_G, kind="cubic")
    return float(cs(W, K_WL))


def alfa(case_of_application="floor heating"):
    """
    Table A.20 - Heat transfer coefficient [W/m2K]
    XYZ This function should not be used for calculating q.
    """
    switcher = {
        "floor heating": 10.8,
        "wall heating": 8,
        "ceiling heating": 6.5,
        "floor cooling": 6.5,
        "wall cooling": 8,
        "ceiling cooling": 10.8,
    }
    return switcher.get(case_of_application.lower())


def R_t1(R_z, R_w, R_r, R_x):
    """Function B.1 - Resistance between supply temperature t_v
    and average temperature of conductive later t_c."""
    return R_z + R_w + R_r + R_x


def R_t2(R_w, R_r, R_x, U_1, U_2, m_H_sp, c):
    """Function B.2 - Resistance between supply temperature t_v
    and average temperature of conductive later t_c."""
    U = 1 / (U_1 + U_2)
    mc = m_H_sp * c
    return 1 / mc * (1 - exp(-1 / ((R_w + R_r + R_x + U) * mc))) - U


def q11(R_1, R_2, R_t, t_1, t_2, t_v):
    """
    Function B.3 - Steady state heat flux into the adjacent spaces.
    """
    return (R_t * (t_2 - t_1) + R_2 * (t_v - t_1)) / (R_1 * R_2 + R_1 * R_t + R_2 * R_t)


def q12(R_1, R_2, R_t, t_1, t_2, t_v):
    """
    Function B.4 - Steady state heat flux into the adjacent spaces.
    """
    return (R_t * (t_1 - t_2) + R_1 * (t_v - t_2)) / (R_1 * R_2 + R_1 * R_t + R_2 * R_t)


def K_H3(R_w, R_r, R_x, R_i):
    """Function B.5 - Equivalent heat transmission coefficient for system E and F."""
    return 1 / (R_w + R_r + R_x + R_i)


def R_w1(W, d_a, s_r, m_H_sp, l):
    """Function B.6 - Resistance w for system E."""
    return W**0.13 / 8 * pi * ((d_a - 2 * s_r) / (m_H_sp * l)) ** 0.87


def R_r1(W, d_a, s_r, k_r):
    """Function B.7 - Resistance r of pipe wall for system E."""
    return W * log(d_a / (d_a - 2 * s_r)) / (2 * pi * k_r)


def R_x1(W, d_a, k_b):
    """Function B.8 - Resistance x between pipe outside wall
    and conductive later for system E."""
    return W * log(W / (pi * d_a)) / (2 * pi * k_b)


def U_i(h_i, s_i, k_b):
    """Function B.9 - Heat transfer coefficient."""
    return 1 / (1 / h_i + s_i / k_b)


def R_i(U_i):
    """Function B.10 - Resistance from function B.9, B.14 or B.15."""
    return 1 / U_i


def R_w2(W, k_w, m_H_sp, c):
    """Function B.11 - Resistance w for system F."""
    return W / (pi * k_w) * (49.03 + 16.68 / pi * m_H_sp * c * W / k_w) ** (-1 / 3)


def R_r2(W, d_a, s_r, k_r):
    """Function B.12 - Resistance r of pipe wall for system F."""
    return W * log(d_a / (d_a - 2 * s_r)) / (2 * pi * k_r)


def R_x2(W, d_a, k_l):
    """Function B.13 - Resistance x between pipe outside wall
    and conductive later for system F."""
    return W / 3 * (W / (pi * d_a)) / (2 * pi * k_l)


def U_1(h_1, s_1, k_b, s_l, k_l):
    """Function B.14 - Heat transfer coefficient 1 for system F."""
    return 1 / (1 / h_1 + s_1 / k_b + s_l / (2 * k_l))


def U_2(h_2, s_l, k_l):
    """Function B.15 - Heat transfer coefficient 2 for system F."""
    return 1 / (1 / h_2 + s_l / (2 * k_l))


# Function B.16 is equal to B.10
