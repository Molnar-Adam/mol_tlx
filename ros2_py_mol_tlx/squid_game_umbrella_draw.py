import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class CircleDrawer(Node):
    def __init__(self):
        super().__init__('circle_drawer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_move)  # Publish every 0.1 seconds
        self.move_cmd = Twist()

        self.get_logger().info("Circle Drawing Node Started")
        self.draw_circle()

    def draw_circle(self):
        # Define the radius and speed for the circle
        radius = 2.0  # radius of the circle
        speed = 1.0   # forward speed

        # Linear and angular velocity to make the turtle draw a circle
        self.move_cmd.linear.x = speed  # Move forward
        self.move_cmd.angular.z = speed / radius  # Turn to create a circular path

        self.get_logger().info("Drawing a circle")
        
        # Publish the command for 100 steps (can be adjusted for different circle sizes)
        for _ in range(100):
            self.publisher.publish(self.move_cmd)
            self.get_logger().info(f"Publishing move: linear.x = {self.move_cmd.linear.x}, angular.z = {self.move_cmd.angular.z}")
            time.sleep(0.1)  # Sleep to allow movement

    def publish_move(self):
        # This method is triggered periodically by the timer
        self.publisher.publish(self.move_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = CircleDrawer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
