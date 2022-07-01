#!/usr/bin/env python3

import rospy
import rosnode
import roslaunch

core_nodes = [
    '/turtlebot3_core', 
    '/turtlebot3_lds', 
    '/rosout', 
    '/camera/realsense2_camera', 
    '/camera/realsense2_camera_manager', 
    '/turtlebot3_diagnostics',
]

class heartbeat():
    
    def __init__(self):
        self.node_name = "tb3_status"
        self.startup = True
        
        rospy.init_node(self.node_name, anonymous=True)
        self.rate = rospy.Rate(1) # hz
                
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook) 

        timestamp = rospy.get_time()
        self.starttime = rospy.get_time()
        while (rospy.get_time() - timestamp) < 10:
            continue
        
        self.startup = False
        rospy.loginfo(f"The '{self.node_name}' node is active...")

    def shutdownhook(self):
        # print(f"Stopping the '{self.node_name}' node at: {rospy.get_time()}")
        self.ctrl_c = True

    def main(self):
        while self.startup:
            continue
        
        timestamp = rospy.get_time()
        while not self.ctrl_c:
            if (rospy.get_time() - timestamp) > 10:
                active_nodes = rosnode.get_node_names()
                if all([i in active_nodes for i in core_nodes]):
                    rospy.loginfo(f"TB3 active for {rospy.get_time() - self.starttime:.0f}s. Status OK...")
                else:
                    rospy.loginfo("TB3 ERROR: core node(s) missing from rosnode list")
                timestamp = rospy.get_time()
            
            self.rate.sleep()

if __name__ == '__main__':
    instance = heartbeat()
    try:
        instance.main()
    except rospy.ROSInterruptException:
        pass