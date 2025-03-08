from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
         Node(
            package='mol_tlx',
            executable='car_draw',
            name='sim2',
            output='screen', 
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim1',
            output='screen', 
        ),
         Node(
            package='mol_tlx',
            executable='car_publisher', 
            name='car_publisher',
            output='screen',
        ),
        Node(
            package='mol_tlx',
            executable='car_subscriber',
            name='car_subscriber',
            output='screen',
        ),

    ])
