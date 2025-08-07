# Robot arm path planning with obstacle avoidance (ROS2 + MOVEIT2 + RVIZ2)

## PROJECT STRUCTURE
├── moveit2_panda_config/ # MoveIt 2 config package for Panda arm │ ├── config/ # Includes planning config, kinematics, controllers, etc. │ └── launch/ # Launch file for MoveIt and RViz2 │ ├── path_planning_demo/ # Custom demo package │ ├── launch/ │ │ └── panda_with_obstacle.launch.py # Launches the full demo │ └── src/ │ └── add_obstacle_node.cpp # Adds a static obstacle to the planning scene 
