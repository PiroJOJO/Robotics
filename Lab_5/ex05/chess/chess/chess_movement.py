import rclpy
from rclpy.node import Node
import sys
from math import pi
from geometry_msgs.msg import Twist
import time

class Chess(Node):

    def __init__(self):
        super().__init__('chess')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.move_to_goal)
        self.step = self.declare_parameter('step', 1.0).get_parameter_value().double_value
        self.vec = True
        self.povorot = False

    def move_to_goal(self):
        tw = Twist()
        if self.vec:
                tw.linear.x = -self.step
                self.vec = False
        else:
                tw.angular.z = pi / 4
                self.vec = True

        self.publisher.publish(tw)

def main():
    rclpy.init()
    chess = Chess()
    rclpy.spin(chess)
    circle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

