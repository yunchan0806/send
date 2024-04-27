import rclpy
from typing import List
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import SetParametersResult

class ParamNode(Node):
    def __init__(self):
        super().__init__("paramNode")
        self.declare_parameter('myparam', '내가 만든 파라미터')
        self.myparam = ""
        self.create_timer(1, self.print_param)
        self.add_on_set_parameters_callback(self.paramUpdata)
    def print_param(self):
        self.get_logger().info(f"{self.myparam}")

    def paramUpdata(self, params: List[Parameter]):
        for param in params:
            if param.name == "myparam":
                self.myparam = param.value
                self.get_logger().info(f"{self.myparam}")
        return SetParametersResult(successful=True)

def main():
    rclpy.init()
    node = ParamNode()
    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        node.destroy_node()
    
if __name__ == "__main__":
    main()