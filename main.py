import numpy
import sys
import MPU
import Adafruit_BBIO.PWM as PWM
sys.path.insert(1, './src')
import IMU_calc
import calc_functions
import PID_Controller 

PID_object = PID_Controller.PID(0, 0, 0)
myPWM = "P8_13"
PWM.start(myPWM, 0, 100000)
IMU_static = MPU.MPU_9150(0, 0)
IMU_dynamic = MPU.MPU_9150(0, 1)


for i in range(0, 20):
    print("Do you want to change Gains? if yes press y: ")
    if input() == "y":
        new_Kp = float(input())
        PID_object.setKp(new_Kp)
        new_Ki = float(input())
        PID_object.setKi(new_Ki)
        new_Kd = float(input())
        PID_object.setKd(new_Kd)
    ref_angle = calc_functions.reference_angle()
    PID_object.setSetPoint(ref_angle)
    try:
        while True:
            vec_dynamic = IMU_dynamic.get_acceleration()
            vec_static = IMU_static.get_acceleration()
            current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
            output = PID_object.update(current_angle)
            # cut_output = calc_functions.output_cut(output)
            # mapped_output = calc_functions.output_mapped(cut_output)
            PWM.set_duty_cycle(myPWM, output)

    except KeyboardInterrupt:
        pass
    

PWM.stop(myPWM)
PWM.cleanup()