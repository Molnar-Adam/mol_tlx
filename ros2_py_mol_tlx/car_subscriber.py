import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class CarSubscriber(Node):

    def __init__(self):
        super().__init__('car_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    car_subscriber = CarSubscriber()

    rclpy.spin(car_subscriber)

    car_subscriber.destroy_node()  # ✅ Correct variable name
    rclpy.shutdown()


if __name__ == '__main__':
    main()
