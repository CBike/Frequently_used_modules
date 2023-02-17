import time

import serial

class ArduinoSerial:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(port, baudrate, timeout=None)
        time.sleep(3)


    def send(self, data):
        try:
            print(data)
            data += '\n'
            self.ser.write(data.encode())

        except serial.SerialException:
            return f"Error sending data to port {self.port}"


    def receive(self):
        try:
            print(self.ser.readline().decode())
            return self.ser.readline().decode()
        except serial.SerialException:
            return f"Error receiving data from port {self.port}"

    def close(self):
        self.ser.close()


arduino = ArduinoSerial('COM15')
arduino.send('RCP,OFF')
time.sleep(1.5)
arduino.send('FCP,OFF')
time.sleep(1.5)
arduino.close()
