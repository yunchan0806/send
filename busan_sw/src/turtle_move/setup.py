from setuptools import setup
from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_move'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param', glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yunchan',
    maintainer_email='yunchan@todo.todo',
    description='TODO: Package description', 
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'moveTurtleSim = turtle_move.moveTurtleSim:main',
            'moveTurtleSim2 = turtle_move.moveTurtleSim2:main',
            'moveTurtleBot = turtle_move.moveTurtleBot:main',
            'simpleParam = turtle_move.simpleParam:main',

        ],
    },
)
