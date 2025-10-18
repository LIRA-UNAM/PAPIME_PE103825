import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RoverRos2(Node):
    def __init__(self):
        super().__init__('rover_ros2')

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.05, self.rover_movement_callback)
    
    def rover_movement_callback(self):
        msg = Twist()

        msg.linear.x = 0.5
        msg.angular.z = 0.0

        self.publisher.publish(msg)

def main():
    rclpy.init()
    rover = RoverRos2()
    rclpy.spin(rover)
    rover.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

