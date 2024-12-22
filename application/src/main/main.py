import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt


# initialize serial port and get serial port choice
ports = serial.tools.list_ports.comports()

print("Avalable Ports:")
for port, desc, hwid in ports:
    print(f"{port}: {desc}")
    
def check_for_ports(port_list, port_name):
    for port in port_list:
        if port.device == port_name:
            return True
    return False

user_port = input("enter port identifier: ")
substr = ""
if (len(user_port) > 0):
    substr = user_port[len(user_port) - 1]

while (not len(user_port) > 0 or
       not user_port.startswith("COM") or
       not substr.isnumeric or
       not check_for_ports(ports, user_port)):
    substr = user_port[len(user_port) - 1]
    print("error please enter valid port:")
    print("\t port format: COM#")
    user_port = input("enter port identifier: ")

print("\n\n" + user_port)
# open serial port and initialize object
ser = serial.Serial(user_port, 115200, timeout=1)

def updateSerial():
    voltage = []
    time = []
    
    data = ser.read_all()
    # data = ser.read_until('\')
    for i in range(0, 20):
        try:
            data = ser.read_until(b'\n').decode('ascii').strip('\n')
            data_split = data.split(",")
            if len(data_split) == 2:
                voltage.append(float(data_split[0]) / 1023.0 * 5.0)
                time.append(int(data_split[1]))
            else :
                print("error splitting")
        except UnicodeDecodeError:
            print("error decoding data")
        data = ser.read_until(b'\r')
        
    time0 = time[0]
    for i in range(0, len(time)):
        time[i] -= time0
    return time, voltage
    
    # clear and then read serial data
    # data = ser.read_all()
    # try:
    #     decoded_data = data.decode(encoding='ascii', errors='ignore').strip()
    #     split_data = decoded_data.split("\n")
    #     i = 0
    #     time0 = 0
    #     for s in split_data:
    #         s2 = s.split(",")
    #         if (len(s2) == 2 and s2[0].isnumeric() and s2[1].isnumeric()):
    #             voltage.append(float(s2[0]) / 1023.0 * 5.0)
    #             if i == 0:
    #                 time0 = int(s2[1])
    #                 time.append(0)
    #                 i += 1
    #             else:
    #                 time.append(int(s2[1]) - time0)
    # except UnicodeDecodeError:
    #     print("error decoding data")

    return time, voltage

t, v = updateSerial()

print(t)
print(v)

ser.close()
