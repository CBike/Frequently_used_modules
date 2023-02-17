import serial

class ArduinoSerial:
    def __init__(self, port, baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def __enter__(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
        except serial.SerialException:
            return f"Error opening port {self.port}"

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ser is not None:
            self.ser.close()

    def send(self, data):
        try:
            print(data)
            self.ser.write(data.encode())
        except serial.SerialException:
            return f"Error sending data to port {self.port}"


    def receive(self):
        try:
            print(self.ser.readline().decode())
            return self.ser.readline().decode()
        except serial.SerialException:
            return f"Error receiving data from port {self.port}"



