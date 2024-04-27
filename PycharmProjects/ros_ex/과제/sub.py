import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist
class sub(Node):
    def __init__(self):
        super().__init__('sub')
        self.sub = self.create_subscription(Twist, '/hello', self.sub_callback, 10)
    def sub_callback(self, msg:Twist):
        print(msg.linear.x)


def main():
    rp.init()


    node = sub()
    rp.spin(node)

    node.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
