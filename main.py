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

a = -3.607e-12
b = 2.426e-9
c = -6.82e-7
d = 0.0001
e = -0.172
f = 1.7438
g = -3.5151

PID = PIDlib.PidController([0.0, 1.0, 0.0], 0.05, 50)


myPWM = "P8_13"
PWM.start(myPWM, 0)
IMU_static = MPU.MPU_9150(0, 0)
IMU_dynamic = MPU.MPU_9150(0, 1)


for i in range(0, 10):

    ref_angle = calc_functions.reference_angle()
    DC = a*(ref_angle**6) + b*(ref_angle**5) + c*(ref_angle**4) + d*(ref_angle**3) + e*(ref_angle**2) + f*ref_angle + g

    try:
        while True:
            try:
                vec_dynamic = IMU_dynamic.get_acceleration()
                vec_static = IMU_static.get_acceleration()
                current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
                output = PID.output(ref_angle, current_angle)
                print('measured angle:\t', current_angle)
                new_DC = DC  # + output
                if new_DC > 99:
                    new_DC = 99
                elif new_DC < .01:
                    new_DC = .01
#                print('DC:\t\t', DC)
#                print('output:\t\t', output)
                print('output:\t\t', output, '\n')
                PWM.set_duty_cycle(myPWM, new_DC)
                sleep(.05)

            except OSError:
                pass

    except KeyboardInterrupt:
        pass


PWM.stop(myPWM)
PWM.cleanup()
