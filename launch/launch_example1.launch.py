from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim1'
        ),
        Node(
            package='mol_tlx',
            executable='squid_game_umbrella_draw',
            name='sim2'
        ),

    ])
