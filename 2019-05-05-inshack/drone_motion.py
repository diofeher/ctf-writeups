import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.path as mpath
import matplotlib.patches as mpatches

def clean_num(txt):
    return float(txt[:-1].replace(',', '').replace(')', ''))

def clean_input(point):
    pps = point.split('=')
    x = clean_num(pps[1])
    y = clean_num(pps[2])
    z = clean_num(pps[3])
    return x, y, z

class DroneLog(object):
    def __init__(self, x, y, z, accel, history):
        self.x = 0
        self.y = 0
        self.z = 0
        self.lx = []
        self.ly = []
        self.lz = []
        self.movement = []
        self.history = history

    def move(self, point_0, point_1):
        return point_0 + point_1

    def direction(self, cmd):
        x, y, z = clean_input(cmd)
        self.x = self.move(self.x, x)
        self.y = self.move(self.y, y)
        self.z = self.move(self.z, z)
        self.lx.append(self.x)
        self.ly.append(self.y)
        self.lz.append(self.z)

    def run(self):
        for cmd in self.history:
            if 'accel' not in cmd:
                self.direction(cmd)

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.lx, self.ly, self.lz)
        plt.show()


if __name__ == "__main__":
    with open('sensors.log', 'r') as fp:
        points = fp.readlines()
    drone = DroneLog(0, 0, 0, 0, points)
    drone.run()
    drone.plot()

# INSA{66333db55e9ca50e9e9c4c94dc45250532832dc4681d531f0fab6d1a255c8578}
