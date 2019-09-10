import numpy
import sys
import MPU
sys.path.insert(1, './src')
import IMU_calc
import reference_angle
import PID_Controller 

PID_object = PID(0, 0, 0)

for i in range(0, 100):    
    print("Do you want to change Gains? if yes press y: ")
    if input()=="y":
        new_Kp=input()
        if type(new_Kp) is not float:
            print('Bitte float')
        elif new_Kp is float:
            PID_object.setKp(new_Kp)
        new_Ki=input()
        PID_object.setKi(new_Ki)
        new_Kd=input()
        PID_object.setKd(new_Kd)
    ref_angle = reference_angle.reference_angle()
    PID_object.setSetPoint(ref_angle)
    try:
        while True:
                IMU_dynamic = MPU.MPU_9150(0, 1)
                vec_dynamic = IMU_dynamic.get_acceleration()
                IMU_static = MPU.MPU_9150(0, 0)
                vec_static = IMU_static.get_acceleration()
                current_angle = IMU_calc.calc_angle(vec_dynamic, vec_static)
                PID_object.update(current_angle)
    except KeyboardInterrupt:
        pass
                
