import rclpy
from rclpy.node import Node
import sys
from math import pi
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time
import numpy as np

class Depth_camera(Node):

    def __init__(self):
        super().__init__('depth_camera')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 10)
        self.subscriber = self.create_subscription(Image, '/depth/image', self.update_camera, 10)
        self.timer = self.create_timer(0.1, self.check_camera)
        self.camera = Image()
        self.bridge_object = CvBridge()
        self.distance = 1.0

    def update_camera(self, data):
        self.camera = data

    def check_camera(self):
        if len(self.camera.data)!=0:
            tw = Twist()
            original_image = np.array(self.bridge_object.imgmsg_to_cv2(self.camera, self.camera.encoding))
            i = int(self.camera.height/2)
            j = int(self.camera.width/2)
            area = original_image[i - 150:i + 150, j  - 150:j + 150]

            d = np.min(area)
            if (d < self.distance):
                tw.linear.x = 0.0
            else:
                tw.linear.x = 1.0
            self.get_logger().info(str(d))
            self.publisher.publish(tw)

def main():
    rclpy.init()
    depth_camera= Depth_camera()
    rclpy.spin(depth_camera)
    depth_camera.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

