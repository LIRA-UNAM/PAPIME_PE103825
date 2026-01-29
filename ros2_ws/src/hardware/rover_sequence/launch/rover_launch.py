import os
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController

def generate_launch_description():
    # Usamos los recursos del paquete rover_control (URDF y world)
    rover_control_dir = get_package_share_directory('rover_control')
    robot_description_path = os.path.join(rover_control_dir, 'resource', 'my_rover.urdf')

    webots = WebotsLauncher(
        world=os.path.join(rover_control_dir, 'worlds', 'rover_practice.wbt')
    )

    my_rover_driver = WebotsController(
        robot_name='pumas_rover',
        parameters=[{'robot_description': robot_description_path}],
    )

    sequence_node = Node(
        package='rover_sequence',
        executable='rover_sequence',
        name='rover_sequence',
        output='screen',
    )

    return LaunchDescription([
        webots,
        my_rover_driver,
        sequence_node,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        ),
    ])
