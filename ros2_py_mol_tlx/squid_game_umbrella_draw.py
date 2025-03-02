import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquidGameUmbrellaDraw(Node):
    def __init__(self):
        super().__init__('squid_game_umbrella_draw')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_move)  # Publish every 0.1 seconds
        self.move_cmd = Twist()

        self.get_logger().info("Squid Game Umbrella Draw Node Started")
        self.draw_umbrella()

    def draw_umbrella(self):
        # Drawing the umbrella
        self.get_logger().info("Drawing umbrella top (half-circle)")
        for _ in range(20):
            self.move_cmd.linear.x = 2.0
            self.move_cmd.angular.z = 0.35
            self.publisher.publish(self.move_cmd)
            self.get_logger().info(f"Publishing move: linear.x = {self.move_cmd.linear.x}, angular.z = {self.move_cmd.angular.z}")
            time.sleep(0.1)  # Sleep to allow movement
        
        self.get_logger().info("Drawing umbrella handle (straight line)")
        # Move the turtle down to simulate the umbrella handle
        self.move_cmd.linear.x = -2.0
        self.move_cmd.angular.z = 0.0
        for _ in range(10):
            self.publisher.publish(self.move_cmd)
            self.get_logger().info(f"Publishing move: linear.x = {self.move_cmd.linear.x}, angular.z = {self.move_cmd.angular.z}")
            time.sleep(0.1)

    def publish_move(self):
        # This method is triggered periodically by the timer
        self.publisher.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = SquidGameUmbrellaDraw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
