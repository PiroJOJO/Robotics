import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import MessageTurtleCommands
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

class TurtleActionServer(Node):

    def __init__(self):
        super().__init__('turtle_action_server')
        self._action_server = ActionServer(self,MessageTurtleCommands,'MessageTurtleCommands',self.execute_callback)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose,'/turtle1/pose', self.position, 10)

    def position(self, msg):
        self.x = msg.x
        self.y = msg.y
    		
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        command = goal_handle.request.command
        s = goal_handle.request.s
        angle = goal_handle.request.angle
        
        feedback_msg = MessageTurtleCommands.Feedback()
        feedback_msg.odom = 0.0
        tw = Twist()
        step = s/2
        
        if command == 'forward':
        	while(feedback_msg.odom < s):
        		tw.linear.x = step
        		feedback_msg.odom += step
        		self.publisher.publish(tw)
        		time.sleep(1)
        		
        if command == 'turn_left':
        	tw.angular.z = angle * 3.14 / 180
        	goal_handle.publish_feedback(feedback_msg)
        	self.publisher.publish(tw)
        	time.sleep(1)
        	
        if command == 'turn_right':
                tw.angular.z = -1 * angle * 3.14 / 180   
                self.publisher.publish(tw)
                time.sleep(1)    
        
        result = MessageTurtleCommands.Result()
        goal_handle.succeed()
        result.result = True
       
        return result


def main(args=None):
    rclpy.init(args=args)

    turle_action_server = TurtleActionServer()

    rclpy.spin(turle_action_server)


if __name__ == '__main__':
    main()
