# Robot arm path planning with obstacle avoidance (ROS2 + MOVEIT2 + RVIZ2)

## PROJECT STRUCTURE
├── moveit2_panda_config/ # MoveIt 2 config package for Panda arm 
│ ├── config/ # Includes planning config, kinematics, controllers, etc. 
│ └── launch/ # Launch file for MoveIt and RViz2 
│
├── path_planning_demo/ # Custom demo package 
│ ├── launch/ 
│ │ └── panda_with_obstacle.launch.py #launches the full demo 
│ └── path_planning_demo/ #scripts folder for python files
│   └── add_obstacle_node.cpp #Adds a static obstacle to the planning scene 

## HOW TO RUN
### PREREQUISITES:
- ROS2 humble installed (includes RVIZ2)
- MOVEIT2 installed
- 'xacro' and 'joint state gui' for testing the URDF

```
sudo apt update
sudo apt install ros-humble-moveit ros-humble-joint-state-publisher-gui
```

###BUILD AND LAUNCH
1. Create a workspace 'abc_ws'
   ```
   cd ~/abc_ws
   git clone https://github.com/harshavarthanv/OA_robot_simulation.git
   cd src
   ```
   
