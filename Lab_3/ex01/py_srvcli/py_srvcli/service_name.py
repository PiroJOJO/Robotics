from tutorial_interfaces.srv import FullNameSumService

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(FullNameSumService, 'service_name', self.full_name_callback)

    def full_name_callback(self, request, response):
        response.full_name = request.last_name + request.name + request.first_name
        self.get_logger().info('Incoming request\nlast_name: %s name: %s first_name: %s ' % (request.last_name, request.name, request.first_name))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
