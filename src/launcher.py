#!/usr/bin/env python3

import os

nodes = os.popen("rosnode list").readlines()

nodes = [name.replace("\n", "") for name in nodes]

print(nodes)

# import rospy
# import rosnode
# import roslaunch

# rospy.init_node('tb3_ros_launcher')

# nodelist = rosnode.get_node_names()

# core_nodes = ["/camera/realsense2_camera",
#               "/camera/realsense2_camera_manager",
#               "/turtlebot3_core",
#               "/turtlebot3_diagnostics",
#               "/turtlebot3_lds",
#               ]

# if all([core in nodelist for core in core_nodes]):
#     print('all good')
# else:
#     print('no joy')