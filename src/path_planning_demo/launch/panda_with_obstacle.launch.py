from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    moveit2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('moveit2'), 'launch', 'demo.launch.py')
        )
    )

    add_obstacle_node = Node(
        package='path_planning_demo',
        executable='add_obstacle',
        name='add_obstacle',
        output='screen'
    )

    return LaunchDescription([
        moveit2_launch,
        add_obstacle_node
    ])
