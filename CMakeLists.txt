cmake_minimum_required(VERSION 3.8)
project(mol_tlx)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# Install Python nodes
install(
  PROGRAMS
  scripts/car_publisher.py
  scripts/car_subscriber.py
  scripts/car_draw.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
