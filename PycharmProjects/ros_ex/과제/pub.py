import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist


class pub(Node):
    def __init__(self):
        super().__init__('pub')
        self.pub = self.create_publisher(Twist, 'hello', 10)
def main():
    rp.init()
    node = pub()
    rp.spin(node)

    node.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()