#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
import tf.transformations
import numpy as np


def random_pose():
    pose = PoseStamped()
    pose.header.stamp = rospy.Time.now()
    pose.header.frame_id = ""  # any frame you're working with
    pose.pose.position.x = np.random.uniform(0, 0.5) #0.15
    pose.pose.position.y = np.random.uniform(-0.7, 0.7) #0.0
    pose.pose.position.z = 0.5
    
    rotx = np.pi
    roty = 0
    rotz = 0
    
    quaternion = tf.transformations.quaternion_from_euler(rotx, roty, rotz)
    
    #print(quaternion)
    
    pose.pose.orientation.x = quaternion[0]
    pose.pose.orientation.y = quaternion[1]
    pose.pose.orientation.z = quaternion[2]
    pose.pose.orientation.w = quaternion[3]
    
    return pose


if __name__ == '__main__':
    rospy.init_node('move_bot', anonymous=True)
    pub = rospy.Publisher('/cartesian_impedance_example_controller/equilibrium_pose', PoseStamped, queue_size=1)
    rate = rospy.Rate(1)
    try:
        while not rospy.is_shutdown():
            pub.publish(random_pose())
            rospy.loginfo("Published pose message to equilibrium_pose")
            rate.sleep()    
    except rospy.ROSInterruptException:
        pass
