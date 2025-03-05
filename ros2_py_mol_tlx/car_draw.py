import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class CarDrawNode(Node):  # Corrected class name
    def __init__(self):
        super().__init__('car_draw')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.001, self.loop)
        self.count = 0
        self.get_logger().info("CarDrawNode initialized.")  # Fixed missing parentheses

    def publish_message(self, fwd, turn):
        msg = Twist()
        msg.linear.x = fwd
        msg.angular.z = turn
        self.count += 1
        self.get_logger().info(f"Step {self.count}. Speed: {msg.linear.x}, Turn: {msg.angular.z}")
        self.publisher.publish(msg)
        time.sleep(2)  # Delay for 2 seconds

    def loop(self):
        self.get_logger().info("Loop started.")
        time.sleep(1)

        self.publish_message(4.5, 0.0)  
        self.publish_message(0.0, -115 * math.pi / 180)  
        self.publish_message(1.5, 0.0)  
        self.publish_message(0.0, -67 * math.pi / 180)  
        self.publish_message(1.0, 0.0)  

        for _ in range(12):  
            self.publish_message(0.25, 30 * math.pi / 180)  

        self.publish_message(5.5, 0.0)  

        for _ in range(12):  
            self.publish_message(0.25, 30 * math.pi / 180)  

        self.publish_message(1.0, 0.0)  
        self.publish_message(0.0, -93 * math.pi / 180)  
        self.publish_message(1.2, 0.0)  
        self.publish_message(0.0, -88 * math.pi / 180)  
        self.publish_message(2.0, 0.0)  
        self.publish_message(0.0, 60 * math.pi / 180) 
        self.publish_message(2.0, 0.0)  
        self.publish_message(0.0, -60 * math.pi / 180) 
        self.publish_message(2.0, 0.0)  
        self.publish_message(0.0, -50 * math.pi / 180) 
        self.publish_message(2.15, 0.0)  
        self.publish_message(0.0, -128 * math.pi / 180) 
        self.publish_message(4.5, 0.0)  


        self.get_logger().info("Program finished")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = CarDrawNode()  # Use the corrected class name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
