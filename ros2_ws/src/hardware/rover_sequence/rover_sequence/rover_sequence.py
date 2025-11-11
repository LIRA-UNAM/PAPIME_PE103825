import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RoverRos2(Node):
    def __init__(self):
        super().__init__('rover_ros2_sequence')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.rover_movement_callback)

        # Lista de movimientos en secuencia (x, z, duración en segundos)
        # Puedes modificar libremente esta lista:
        self.sequence = [
            {"x": 0.0, "z": 0.0, "duration": 5.0},  
            {"x": 0.0, "z": 0.5, "duration": 5.0},  
            {"x": 0.0, "z": 0.0, "duration": 2.0},  
            {"x": -0.5, "z": 0.0, "duration": 1.5},  
            {"x": 0.0, "z": 0.5, "duration": 10.0},
            {"x": -0.5, "z": 0.0, "duration": 2.5},  
            {"x": 0.0, "z": 0.5, "duration": 10.0},
            {"x": -0.5, "z": 0.0, "duration": 2.5},  
            {"x": 0.0, "z": 0.5, "duration": 10.0},
            {"x": -0.5, "z": 0.0, "duration": 2.5},  
            {"x": 0.0, "z": 0.5, "duration": 10.0},
            {"x": -0.5, "z": 0.0, "duration": 2.5},
            {"x": 0.5, "z": 2.0, "duration": 10},
               
        ]

        # Control del estado actual
        self.current_step = 0
        self.start_time = self.get_clock().now()

    def rover_movement_callback(self):
        # Si ya completó todos los pasos, detener y apagar nodo
        if self.current_step >= len(self.sequence):
            msg = Twist()
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            self.get_logger().info("Secuencia completada.")
            # self.destroy_node()
            # rclpy.shutdown()
            return

        current_time = self.get_clock().now()
        elapsed = (current_time - self.start_time).nanoseconds / 1e9

        step = self.sequence[self.current_step]

        msg = Twist()

        # Mientras no se acabe el tiempo de este paso
        if elapsed < step["duration"]:
            msg.linear.x = step["x"]
            msg.angular.z = step["z"]
        else:
            # Pasar al siguiente paso
            self.current_step += 1
            self.start_time = current_time
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info(f"Paso {self.current_step} completado, avanzando al siguiente.")

        self.publisher.publish(msg)


def main():
    rclpy.init()
    rover = RoverRos2()
    rclpy.spin(rover)
    rover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
