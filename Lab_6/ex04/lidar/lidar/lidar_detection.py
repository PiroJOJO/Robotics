import rclpy
from rclpy.node import Node
import sys
from math import pi
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import numpy as np

class Lidar(Node):

    def __init__(self):
        super().__init__('lidar')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.subscriber = self.create_subscription(LaserScan, '/robot/scan', self.update_lidar, 10)
        self.timer = self.create_timer(0.1, self.check_lidar)
        self.lidar = LaserScan(ranges = np.zeros(360))
        self.distance = 0.5
        self.stop = False

    def update_lidar(self, data):
        self.lidar = data

    def check_lidar(self):
        tw = Twist()
        if (np.min(self.lidar.ranges[120:240]) < self.distance):
            tw.linear.x = 0.0
        else:
            tw.linear.x = 1.0
        self.publisher.publish(tw)

def main():
    rclpy.init()
    lidar= Lidar()
    rclpy.spin(lidar)
    lidar.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

