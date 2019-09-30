import numpy as np


def calc_angle(vec1, vec2, rotate_angle=0., delta_out=False, jump=np.pi*.5):
    theta = np.radians(rotate_angle)
    vec1 = rotate(vec1, theta)
    x1, y1, z1 = normalize(vec1)
    x2, y2, z2 = normalize(vec2)
    phi1 = np.arctan2(y1, x1)
    vec2 = rotate([x2, y2, 0], phi1+jump)
    phi2 = np.degrees(np.arctan2(vec2[1], vec2[0]) - jump)

    alpha_IMU = phi2

    if delta_out:
        z = np.mean([z1, z2])
        delta = np.degrees(np.arccos(z))

    return alpha_IMU if not delta_out else (alpha_IMU, delta)


def normalize(vec):
    x, y, z = vec
    l = np.sqrt(x**2 + y**2 + z**2)
    return x/l, y/l, z/l


def rotate(vec, theta):
    c, s = np.cos(theta), np.sin(theta)
    return (c*vec[0]-s*vec[1], s*vec[0]+c*vec[1], vec[2])
