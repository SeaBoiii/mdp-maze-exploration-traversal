import socket
from time import sleep

from comms import ListenerThread
from robot import *
from utils import *
from constants import arduino_queue


class RealRobot(Robot):
    def __init__(self, handler):

        super().__init__(handler)
        family = socket.AF_INET
        socket_type = socket.SOCK_STREAM
        self.socket = socket.socket(family, socket_type)
        self.socket.settimeout(1)
        self.connected = False
        self.port = 1273
        self.host = ""
        self.listener = None

    def connect(self, host):
        self.host = host

        try:
            self.socket.connect((self.host, self.port))
            self.connected = True
            print("Connection established.")
            self.listener = ListenerThread(name='producer', socket=self.socket, handler=self.handler)
            self.listener.start()
            self.send('c\ns\n')
            # self.send('s')
        except socket.error as error:
            self.connected = False
            print("Unable to establish connection. ", error)

        return self.connected

    def disconnect(self):
        try:
            self.socket.shutdown(1)
            self.socket.close()
            self.connected = False
            print("Socket closed.")
        except socket.error as error:
            print("Unable to close socket. ", error)
            return False

        return True

    def send(self, msg):
        if not self.connected:
            self.connect(self.host)

        if self.connected:
            print("[Info] Sending message: ", msg)
            try:
                self.socket.sendall(str.encode(msg))
            except socket.error as error:
                print("Unable to send message. ", error)

    def receive(self):
        while True:
            if not arduino_queue.empty():
                break
            else:
                sleep(0.1)

        msg = arduino_queue.get()
        msg = msg.split()

        # Calibration
        # if abs(float(msg[0]) - float(msg[1])) >= 2.0:
        bearing = self.handler.robot.bearing
        can_calibrate = self.handler.map.find_left_wall_or_obstacle(self.x, self.y, bearing)

        if can_calibrate:
            print('calibrate')
            self.send('c\n')

        out = [convert_short(msg[2]),
               convert_short(msg[3]),
               convert_short(msg[4]),
               convert_short(msg[1]),
               convert_long(msg[5])]

        return out

    def move(self, sense, ir, steps=1):
        super().move(sense= sense, ir = ir, steps=steps)
        self.send('f' + str(steps) + '\n')

    def left(self):
        # rotate anticlockwise by 90 deg
        super().left()
        self.send('l90\n')

    def right(self):
        # rotate clockwise by 90 deg
        super().right()
        self.send('r90\n')

    def left_diag(self):
        super().left_diag()
        self.send('l45\n')

    def right_diag(self):
        super().right_diag()
        self.send('r45\n')
