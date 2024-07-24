#!/usr/bin/env python3

#arm_node

import rclpy
from rclpy.node import Node
import serial
from px4_msgs.msg import ActuatorArmed

class Arming_node(Node):
    def __init__(self):
        super().__init__("arm_node")
        self.create_timer(0.1, self.Armed_callback)
        self.pose_subscriber = self.create_publisher(ActuatorArmed, "uORB/topics/safety", 10)
        self.cmd_arm_publisher_ = self.create_publisher(
            bool, "/arm_node/pose", 10
        )
    def Armed_callback(self, arm:ActuatorArmed):
        cmd = bool()
        if arm:
            cmd = True
        else:
            cmd = False
        self.cmd_arm_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = Arming_node()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
