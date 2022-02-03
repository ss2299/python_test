import serial
from serial.tools import list_ports

ports_list = list_ports.comports()
port = '/dev/cu.usbserial-AG0K5F4O'
baud = 9600             # 시리얼 보드레이트(통신속도)

ser = serial.Serial(port, baud, timeout=1)


while True:
    if ser.inWaiting() > 0:
        myData = ser.readline()

        print(f'read : {myData}')

    ser.write(b'Test')

