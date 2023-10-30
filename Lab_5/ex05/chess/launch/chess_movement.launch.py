import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, SetParameter


from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import TimerAction

def generate_launch_description():
     # Configure ROS nodes for launch

    # Setup project paths
    pkg_project_bringup = get_package_share_directory('my_robot')

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_project_bringup, 'launch', 'robot_gazebo.launch.py')),
    )

    return LaunchDescription([
        gz_sim,
        
        Node(
            package='chess',
            executable='chess_movement',
            name='chess_movement',
            parameters=[
                {'step': LaunchConfiguration('step', default = 1.0)},

            ]
        ),
    ])
