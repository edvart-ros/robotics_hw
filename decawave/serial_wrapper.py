from typing import Any
import serial
import time
import datetime
from collections import Counter

class Decawave_Bridge_Node:
    def __init__(self):
        self.list =[]
        self.DWM=serial.Serial(port="COM3", baudrate=115200)
        print("Connected to " + self.DWM.name)
        self.DWM.flushInput()
        self.DWM.flushOutput()
        self.DWM.write("\r\r".encode())
        time.sleep(1)
        self.DWM.write("lec\r".encode())
        time.sleep(1)
        self.publish_decawave_data()

    def decawave_shutdown_sequence(self):
        print("Shutting down")
        self.DWM.write("\r".encode())
        self.DWM.close()

    def publish_decawave_data(self):
        while True:
            try:
                self.DWM.flushInput()
                self.DWM.flushOutput()
                line=self.DWM.readline()
                if(line):
                    if len(line)>=32:
                        parse=line.decode().split(",")
                        #print(parse)
                        dwm_name = parse[2]
                        x_pos=parse[3]
                        y_pos=parse[4]
                        z_pos=parse[5]
                        #val = (x_pos,y_pos)
                        print(dwm_name, ": ", datetime.datetime.now().strftime("%H:%M:%S"),"(",x_pos,", ",y_pos,", ",z_pos,")")
                        
                    else:
                        print("Position not calculated: ",line.decode())
            except Exception as ex:
                print(ex)
                break


if __name__ == "__main__":
    decawave_bridge_node = Decawave_Bridge_Node()