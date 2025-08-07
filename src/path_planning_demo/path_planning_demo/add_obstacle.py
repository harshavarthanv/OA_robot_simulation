import rclpy
from rclpy.node import Node
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose
from moveit_msgs.msg import CollisionObject, PlanningScene
from std_msgs.msg import Header

class ObstaclePublisher(Node):
    def __init__(self):
        super().__init__('obstacle_publisher')

        self.publisher_ = self.create_publisher(PlanningScene, '/planning_scene', 10)

        #publish once after 2 seconds
        self.timer = self.create_timer(2.0, self.publish_obstacle)

    def publish_obstacle(self):
        self.get_logger().info("Publishing obstacle to planning scene...")

        #define the collision object
        collision_object = CollisionObject()
        collision_object.header = Header()
        collision_object.header.frame_id = "panda_link0"
        collision_object.id = "obstacle_box"

        box = SolidPrimitive()
        box.type = SolidPrimitive.BOX
        box_height = 0.2
        box_width = 0.7
        box_length = 0.2    
        box.dimensions = [box_length, box_width, box_height]

        pose = Pose()
        pose.orientation.w = 1.0
        pose.position.x = 0.5
        pose.position.y = 0.1
        pose.position.z = box_height / 2.0 #to make sure the box is above the ground

        collision_object.primitives = [box]
        collision_object.primitive_poses = [pose]
        collision_object.operation = CollisionObject.ADD

        planning_scene = PlanningScene()
        planning_scene.world.collision_objects = [collision_object]
        planning_scene.is_diff = True

        self.publisher_.publish(planning_scene)
        self.get_logger().info("Obstacle added")

        # Only send once
        self.destroy_timer(self.timer)

def main():
    rclpy.init()
    node = ObstaclePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
