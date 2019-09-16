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


PID_object = PID_Controller.PID(0, 0, 0)
PID = PIDlib.PidController([1, 10, 0], 0.01, 99)


myPWM = "P8_13"
PWM.start(myPWM, 0)
IMU_static = MPU.MPU_9150(0, 0)
IMU_dynamic = MPU.MPU_9150(0, 1)


for i in range(0, 10):
    print("Do you want to change Gains? if yes press y: ")
    if input() == "y":
        new_Kp = float(input())
        PID_object.setKp(new_Kp)
        new_Ki = float(input())
        PID_object.setKi(new_Ki)
        new_Kd = float(input())
        PID_object.setKd(new_Kd)
    ref_angle = calc_functions.reference_angle()
    DC = 28.266*np.log(ref_angle)-55.595
    PID_object.setSetPoint(ref_angle)
    PID_object.setWindup(20)
    PID_object.setSampleTime(0.5)
    try:
        while True:
            try:
                vec_dynamic = IMU_dynamic.get_acceleration()
                vec_static = IMU_static.get_acceleration()
                current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
                output = PID_object.update(current_angle)
                output_2 = PID.output(ref_angle, current_angle)
                print('measured angle:\t', current_angle)
                # cut_output = calc_functions.output_cut(output)
                new_DC = DC+output_2
                print('DC:\t\t', DC)
                print('output:\t\t', output)
                print('output2:\t\t', output_2, '\n')
                PWM.set_duty_cycle(myPWM, new_DC)

            except OSError:
                pass

    except KeyboardInterrupt:
        pass


PWM.stop(myPWM)
PWM.cleanup()
