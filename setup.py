from setuptools import setup
from glob import glob

package_name = 'ardupilot_simple_flight'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A simple flight routine for ArduPilot using ROS 2.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_flight_node = ardupilot_simple_flight.simple_flight_node:main'
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/ardupilot_simple_flight']),
        ('share/ardupilot_simple_flight', ['package.xml']),
        ('share/ardupilot_simple_flight/launch', glob('launch/*.launch.py')),
    ],
)
