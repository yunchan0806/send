import rclpy as rp
from turtlesim.srv import TeleportAbsolute
#/turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute

rp.init()

node = rp.create_node('turtlesim_client')
cli = node.create_client(TeleportAbsolute, '/turtle1/teleport_absolute',)

req = TeleportAbsolute.Request()
req.x = 1.0
req.y = 1.0

req.theta = 3.14


future = cli.call_async(req)

while not future.done():
    rp.spin_once(node)
    print(putt.don(),future.set_result())