from geometry_msgs.msg import Twist

from nav_msgs.msg import Odometry

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import BatteryState
from sensor_msgs.msg import Imu
from sensor_msgs.msg import LaserScan

from turtlesim.msg import Pose
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter
from typing import List

MAX_VEL = 0.21
MAX_ANGLE = 2.84


class Tbot_move(Node):
    def __init__(self):
        super().__init__("turtleBotMove")  # type: ignore
        laser_profile = qos_profile_sensor_data
        self.create_timer(0.01, self.pub_callback)
        self.create_timer(1 / 60, self.update_callback)
        self.pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.create_subscription(LaserScan, "scan", self.laser_callback, laser_profile)
        self.declare_parameter('vel', MAX_VEL)
        self.declare_parameter('angel', MAX_ANGLE)
        self.vel = 1.0
        self.angel = 1.0
        self.add_on_set_parameters_callback(self.paramUpdata)
        self.create_timer(1, self.print_param)
        self.create_subscription(Odometry, "odom", self.odom_callback, 10)
        self.create_subscription(Imu, "imu", self.imu_callback, 10)
        self.create_subscription(BatteryState, "battery", self.battery_callback, 10)
        self.velocity = 0.0
        self.angular_velocity = 0.0
        self.laserScan = LaserScan()
        self.laserScan.ranges = [0.0]
        self.odom = Odometry()
        self.imu = Imu()
        self.battery = BatteryState()
    def paramUpdata(self, params:List[Parameter]):
        for param in params:
            self.get_logger().info(f'name : {param.name}')
            if param.name == "vel":
                self.vel = param.value
                self.get_logger().info(f'{self.vel}')
                
            if param.name == "angel":
                self.get_logger().info(f'{param.value}')
                self.angel = param.value
                self.get_logger().info(f'{self.angel}')
        return SetParametersResult(successful = True)

    def print_param(self):
         self.get_logger().info(f"vel : {self.vel} angel: {self.angel}")

    def laser_callback(self, msg: LaserScan):
        self.laserScan = msg

    def odom_callback(self, msg: Odometry):
        self.odom = msg

    def imu_callback(self, msg: Imu):
        self.imu = msg

    def battery_callback(self, msg: BatteryState):
        self.battery = msg

    def pub_callback(self):
        msg = Twist()
        msg.linear.x = self.velocity
        msg.angular.z = self.angular_velocity
        msg = self.restriction(msg)
        self.pub.publish(msg)

    def restriction(self, msg: Twist):
        msg.linear.x = min(MAX_VEL, msg.linear.x)
        msg.linear.x = max(-MAX_VEL, msg.linear.x)
        msg.angular.z = min(MAX_ANGLE, msg.angular.z)
        msg.angular.z = max(-MAX_ANGLE, msg.angular.z)
        return msg

    def update_callback(self):

        if self.laserScan.ranges[0] > 0.25:
            self.velocity = self.vel/2
            self.angular_velocity = 0.0
        elif self.laserScan.ranges[0] < 0.2:
            self.velocity = -self.vel/2
            self.angular_velocity = 0.0
        else:
            self.velocity = 0.0
            self.angular_velocity = 0.0

    def pose_callback(self, msg: Pose):
        self.pose_x = msg.x
        self.pose_y = msg.y
        self.pose_theta = msg.theta


def main():
    rclpy.init()
    node = Tbot_move()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()