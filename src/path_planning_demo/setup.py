from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'path_planning_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    package_dir={'': '.'},
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
        # (os.path.join('share', package_name, 'config'), glob('config/*')),
        # (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        # (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='harsha',
    maintainer_email='harsha@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        
    },
)