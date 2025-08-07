# Robot arm path planning with obstacle avoidance (ROS2 + MOVEIT2 + RVIZ2)

## PROJECT STRUCTURE
├── moveit2_panda_config/ # MoveIt 2 config package for Panda arm <br>
│ ├── config/ # Includes planning config, kinematics, controllers, etc. <br>
│ └── launch/ # Launch file for MoveIt and RViz2 <br>
│<br>
├── path_planning_demo/ # Custom demo package <br>
│ ├── launch/ <br>
│ │ └── panda_with_obstacle.launch.py #launches the full demo <br>
│ └── path_planning_demo/ #scripts folder for python files<br>
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

### BUILD AND LAUNCH
1. Create a workspace 'abc_ws'
   ```
   cd ~/abc_ws
   git clone https://github.com/harshavarthanv/OA_robot_simulation.git
   cd src
   ```
2. Build the workspace
   ```
   colcon build --symlink-install
   source install/setup.bash
   ```
3. Launch the workspace
   ```
   ros2 launch path_plannning_demo panda_with_obstacle.launch.py
   ```

### TEST PLANNING
Once launched the rviz2 can be seen with the panda arm and a cuboid obsctacle (green color)<br>
Under motion planning in the planning tab, choose the Start_state as "<current>" and the goal_state as "init_pose" ( This makes the arm move to the init pose)<br>
Click "plan & execute" to see how it plans and executes the planned path.<br>
Then to test the obstacle avoidance by the Moveit2 builtin default solver (RRTCONNECT), change the start_state to "init_pose" and goal_state as "target_pose1"<br>
Click "plan & execute" and observe how it avoid the obstacle and moves to the goal_state.


## TIPS:
1. If the arm is repeating the plan movement, disable "loop animation" in the planned path under motion planning (Under Displays)
2. You can change the path planner to CHOMP in context under motion planning. It will then use CHOMP planner that improves the smoothness and collision-free nature of the path using gradient-based cost minimization. (It is much slower compared to RRTCONNECT)
