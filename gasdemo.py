import os
import sys
import time
from smbus2 import SMBusWrapper
from sgp30 import Sgp30
import displayv4
#blink fast:0x83 2hz  medium:0x85 1hz solid:0x81 

def main():
    if (len(sys.argv)<2):
        print"run the command in the following format:"
        print"-c for CO2eq (ppm),  -t for TVOC "
    else:
        with SMBusWrapper(2) as bus:
                print("the SGP30 takes at least 15 seconds to warm up, 12 hours before the readigs become really stable")
                sgp=Sgp30(bus,baseline_filename="/tmp/mySGP30_baseline")
                print("resetting all i2c devices")
                sgp.i2c_geral_call() #WARNING: Will reset any device on the i2cbus that listens for general call
                print(sgp.read_features())
                print(sgp.read_serial())
                sgp.init_sgp()
                print(sgp.read_measurements())
                while True:
                    time.sleep(1)  
                    sensor_value=(sgp.read_measurements())
                    print(sensor_value)
                    if sys.argv[1]=="-c":
                        sensor_value=sensor_value[0][0]
                        if sensor_value < 2000:
                                os.system("i2cset -y 2 0x70 0x81")
                        elif sensor_value > 5000:
                                os.system("i2cset -y 2 0x70 0x83")
                        else: 
                                os.system("i2cset -y 2 0x70 0x85")
                    elif sys.argv[1]=="-t":
                        sensor_value=sensor_value[0][1]
                    displayv4.displaySeg(sensor_value)
if __name__=='__main__':
        main()
