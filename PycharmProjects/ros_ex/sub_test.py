#/turtle1/pose: turtlesim/msg/Pose
#rcl : ros client lib
import rclpy as rp
from turtlesim.msg import Pose
perv_x = 0
perv_y = 0
def callback(msg):
    global perv_y,perv_x
    if(msg.x != perv_x or msg.y != perv_y):
        print(f'x: {msg.x}, y:{msg.y}')
    # else:
    #     print(".",end='')
    perv_x = msg.x
    perv_y = msg.y

rp.init()
node = rp.create_node("turtlesim_subscriber")
sub = node.create_subscription(Pose,'/turtle1/pose', callback,10)
#rp.spin_once(node)
rp.spin(node)