import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class BatmanDraw(Node):
    def __init__(self):
        super().__init__('batman_draw')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.001, self.loop)
        self.count = 0
        self.get_logger().info("Drawing a batman logo to turtlesim.")
        self.loop()

    def publish_message(self, fwd, turn):
        # Create a Twist message and set the speed and angular velocity
        msg = Twist()
        msg.linear.x = fwd
        msg.angular.z = turn
        self.count += 1
        self.get_logger().info(f"Step {self.count}. speed: '{msg.linear.x}' turn: '{msg.angular.z}'")
        self.publisher.publish(msg)
        time.sleep(2)  # Delay for 2 seconds

    def loop(self):
        self.get_logger().info("Loop started.")
        time.sleep(1)  # Initial sleep for 2 seconds

        self.publish_message(4.5, 0.0)  # Move forward
        self.publish_message(0.0, -115 * math.pi / 180)  # Rotate 115 degrees to the right 
        self.publish_message(1.5, 0.0)  # Move forward
        self.publish_message(0.0, -67 * math.pi / 180)  # Rotate 65 degrees to the right
        self.publish_message(1.0, 0.0)  # Move forward
        for _ in range(12):  # 360 degrees / 10 degrees per step = 36 steps
            self.publish_message(0.25, 30 * math.pi / 180)  # Move forward and rotate by 10 degrees
        self.publish_message(5.5, 0.0)  # Move forward
        for _ in range(12):  # 360 degrees / 10 degrees per step = 36 steps
            self.publish_message(0.25, 30 * math.pi / 180)  # Move forward and rotate by 10 degrees
        self.publish_message(1.0, 0.0)  # Move forward
        self.publish_message(0.0, -93 * math.pi / 180)  # Rotate 65 degrees to the right
        self.publish_message(1.2, 0.0)  # Move forward
        self.publish_message(0.0, -math.pi / 2)  # Rotate 90 degrees
        self.publish_message(2.0, 0.0)  # Move forward









        self.get_logger().info("Program finished")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = BatmanDraw()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
