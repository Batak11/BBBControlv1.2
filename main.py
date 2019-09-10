import numpy
import sys
import MPU
sys.path.insert(1, './src')
import IMU_calc
import reference_angle

IMU_dynamic = MPU.MPU_9150(0, 1)
x_dynamic, y_dynamic, z_dynamic = IMU_dynamic.get_acceleration()
vec_dynamic = IMU_dynamic.get_acceleration()

IMU_static = MPU.MPU_9150(0, 0)
x_static, y_static, z_static = IMU_static.get_acceleration()
vec_static = IMU_static.get_acceleration()

current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
print(current_angle)
ref_angle = reference_angle.ref_angle()
