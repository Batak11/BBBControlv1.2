import numpy as np
from time import sleep
import sys
import MPU
import Adafruit_BBIO.PWM as PWM
sys.path.insert(1, './src')
import IMU_calc
import calc_functions
import PID_Controller 
import PID as PIDlib 

a = -.00000204
b = 0.0006
c = -0.0675
d = 3.9591
e = -19.343
# f = -21.65


PID = PIDlib.PidController([.0, 1, 0.0], 0.01, 30)


myPWM = "P8_13"
PWM.start(myPWM, 0)
IMU_static = MPU.MPU_9150(0, 0)
IMU_dynamic = MPU.MPU_9150(0, 1)


for i in range(0, 10):

    ref_angle = calc_functions.reference_angle()
    DC = a * (ref_angle ** 4) + b * (ref_angle ** 3) + c * (ref_angle ** 2) + d * ref_angle + e

    try:
        while True:
            try:
                vec_dynamic = IMU_dynamic.get_acceleration()
                vec_static = IMU_static.get_acceleration()
                current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
                output = PID.output(ref_angle, current_angle)
                print('measured angle:\t', current_angle, ref_angle)
                new_DC = DC + output
                if new_DC > 99:
                    new_DC = 99
                elif new_DC < .01:
                    new_DC = .01
#                print('output:\t\t', output, '\n')
                PWM.set_duty_cycle(myPWM, new_DC)
                sleep(.01)

            except OSError:
                pass

    except KeyboardInterrupt:
        pass


PWM.stop(myPWM)
PWM.cleanup()
