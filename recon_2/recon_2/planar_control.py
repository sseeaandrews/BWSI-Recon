#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

publish_data = list
subscribe_data = list

publish_topic = "//"
subscribe_topic = "//"

class planar_control(Node):

    def __init__(self):
        super().__init__("planar_control")
        self.cmd_publisher_ = self.create_publisher(
            publish_data, publish_topic, 10

        )
        
        self.pose_subscriber_ = self.create_subscription(
            subscribe_data, subscribe_topic, self.callback, 10
        )
        
        self.get_logger().info("planar_control online")
        
    def callback(self, ):
        cmd = None

        self.cmd_publisher_.publish(cmd)

    def callback_error(self, future):
        try:
            response = future.result
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args = None):
    rclpy.init(args=args)
    
    node = planar_control()
    
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
