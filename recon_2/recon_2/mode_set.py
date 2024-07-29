#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from px4_msgs.msg import VehicleCommand
import time

publish_data = VehicleCommand
subscribe_data = list

publish_topic = "/fmu/in/vehicle_command"
subscribe_topic = "//"

class mode_set(Node):

    def __init__(self):
        super().__init__("land")
        self.cmd_publisher_ = self.create_publisher(
            publish_data, publish_topic, 10
        )
                        
        self.create_service = self.create_service(int, 'recon_2/set_mode', self.callback)
        
        self.pose_subscriber_ = self.create_subscription(
            subscribe_data, subscribe_topic, self.callback, 10
        )
        
        self.get_logger().info("mode setting node has been started.")
                        
    def callback(self, command):
        match command:
            case 1:
                self.arm()
            case 2:
                self.enter_takeoff()
            case 3:
                self.land()
            case 4:
                self.enter_hold()
                
        
        
    def land(self, msg = None):
        cmd = VehicleCommand()
        cmd.timestamp = int(time.time() * 1e6)  # Convert time to microseconds
        cmd.param1 = 0.0  # Landing altitude
        cmd.param2 = 0.0
        cmd.param3 = 0.0
        cmd.command = 21
        cmd.target_system = 1  # Target system ID
        cmd.target_component = 1  # Target component ID
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True

        self.cmd_publisher_.publish(cmd)
        self.get_logger().info("Published vehicle command to start ground landing")
        if msg != None:
            self.get_logger().error(msg)
            
    def arm(self, msg = None):
        cmd = VehicleCommand()
        cmd.timestamp = int(time.time() * 1e6)  # Convert time to microseconds
        cmd.param1 = 1.0  # 1 for arming
        cmd.param2 = 0.0
        cmd.param3 = 0.0
        cmd.command = 400
        cmd.target_system = 1  # Target system ID
        cmd.target_component = 1  # Target component ID
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True

        self.cmd_publisher_.publish(cmd)
        self.get_logger().info("Published vehicle command to set mode to manual.")
        if msg != None:
            self.get_logger().error(msg)

    def disarm(self, msg = None):
        cmd = VehicleCommand()
        cmd.timestamp = int(time.time() * 1e6)  # Convert time to microseconds
        cmd.param1 = 0.0  # 0 for disarming
        cmd.param2 = 0.0
        cmd.param3 = 0.0
        cmd.command = 400
        cmd.target_system = 1  # Target system ID
        cmd.target_component = 1  # Target component ID
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True

        self.cmd_publisher_.publish(cmd)
        self.get_logger().info("Published vehicle command to set mode to manual.")
        if msg != None:
            self.get_logger().error(msg)

    def enter_takeoff(self, target_altitude=1.0, msg=None):
        cmd = VehicleCommand()
        cmd.timestamp = int(time.time() * 1e6)  # Convert time to microseconds
        cmd.param1 = target_altitude # Takeoff altitude
        cmd.param2 = 0.0
        cmd.param3 = 0.0
        cmd.command = 22
        cmd.target_system = 1  # Target system ID
        cmd.target_component = 1  # Target component ID
        cmd.source_system = 1
        cmd.source_component = 1
        cmd.from_external = True

        self.cmd_publisher_.publish(cmd)
        self.get_logger().info("Published vehicle command to set mode to manual.")
        if msg != None:
            self.get_logger().error(msg)
            
        for i in range(20):
            self.arm()

def main(args=None):
    rclpy.init(args=args)
    
    node = Land()
    
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()
