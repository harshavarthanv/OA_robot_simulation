from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    panda_config_path = get_package_share_directory('moveit_resources_panda_moveit_config')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(panda_config_path, 'launch', 'demo.launch.py')
            )
        )
    ])
