#/turtle1/cmd_vel: geometry_msgs/msg/Twist
import rclpy as rp
from geometry_msgs.msg import Twist
z = 0.0
def pub_msg():
    global z
    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = z

    pub.publish(msg)

def timer_callback():
    global z
    pub_msg()
    z += 0.01
    print('.',end='')

rp.init()
node = rp.create_node("turtlesim_publisher")
pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)


node.create_timer(1, timer_callback)
rp.spin(node)