#/turtle1/cmd_vel: geometry_msgs/msg/Twist


import rclpy as rp
from geometry_msgs.msg import Twist
from rclpy.node import Node

class Turtlesim_Publisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher') #node에 대한 초기화
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0

        self.pub.publish(msg)



def main():
    rp.init()

    node = Turtlesim_Publisher()
    rp.spin(node)

    node.destroy_node()

    rp.shutdown()

if __name__ == '__main__':
    main()