import rclpy
from rclpy.node import Node
import sys

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2, sqrt, pow, pi
import time

class Turtle_to_Goal(Node):

	def __init__(self, x, y, theta):
		super().__init__('minimal_publisher')
		self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
		self.subscriber = self.create_subscription(Pose, '/turtle1/pose' , self.update_pose, 10)
		self.pose = Pose()
		self.goal_pose = Pose(x = float(x), y = float(y), theta = float(theta))

	def update_pose(self, data):
		self.pose = data
		self.move_to_goal(self.goal_pose)

	def find_distance(self, goal_pose):
		return sqrt(pow(goal_pose.x - self.pose.x, 2)+pow(goal_pose.y - self.pose.y, 2))

	def find_angular(self, goal_pose):
		return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

	def move_to_goal(self, goal_pose):

		tw = Twist()
		angle = self.find_angular(goal_pose) - self.pose.theta
		tw.angular.z = angle
		self.publisher.publish(tw)
		time.sleep(1)

		tw.angular.z = 0.0
		tw.linear.x = self.find_distance(goal_pose)
		self.publisher.publish(tw)
		time.sleep(1)

		tw.linear.x = 0.0
		tw.linear.y = 0.0
		if goal_pose.theta > 180:
			goal_pose.theta -= 180
			goal_pose.theta *= -1
		res_angular = goal_pose.theta * pi / 180
		tw.angular.z = res_angular - self.pose.theta - angle
		self.publisher.publish(tw)
		time.sleep(2)

def main():
    rclpy.init()

    turtle_to_goal= Turtle_to_Goal(sys.argv[1], sys.argv[2], sys.argv[3])
    rclpy.spin_once(turtle_to_goal)

    turtle_to_goal.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


