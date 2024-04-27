#example/turtle1/cmd_vel: geometry_msgs/msg/Twist


import rclpy as rp
from geometry_msgs.msg import Twist
from rclpy.node import Node

class EXPublisher(Node):
    x = 0
    def __init__(self):
        super().__init__('ex_publisher') #node에 대한 초기화
        self.pub = self.create_publisher(Twist, '/example/cmd_vel', 10)

        self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = float(self.x)
        self.x += 0.1

        self.pub.publish(msg)

def main():
    rp.init()

    node = EXPublisher()
    rp.spin(node)

    node.destroy_node()

    rp.shutdown()

if __name__ == '__main__':
    main()