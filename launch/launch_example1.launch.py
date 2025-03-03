from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
         Node(
            package='mol_tlx',
            namespace='',
            executable='squid_game_umbrella_draw',
            name='sim2',
            output='screen',  # This will show logs in the terminal
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim1',
            output='screen',  # This will show logs in the terminal
        ),

    ])
