#/turtle1/pose: turtlesim/msg/Pose
#rcl : ros client lib

import rclpy as rp

from turtlesim.msg import Pose
from rclpy.node import Node

class Turtlesimsubscriber(Node):

    prev_x = 0
    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.create_subscription(Pose, 'turtle1/pose', self.callback, 10)

    def callback(self, msg:Pose):
        if self.prev_x == msg.x:
            return
        self.prev_x = msg.x
        print(msg.x)

def main():
    rp.init()

    node = Turtlesimsubscriber()
    rp.spin(node)
    node.destroy_node()


    rp.shutdown()

if __name__ == '__main__':
    main()