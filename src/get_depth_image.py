#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
import sensor_msgs.point_cloud2 as pc2
from cv_bridge import CvBridge

def callback(data):
    
    points = list(pc2.read_points(data, skip_nans=True, field_names=("x", "y", "z", "rgb")))
    
    # Convert PointCloud2 to numpy array
    # points = np.array(list(pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)))
    
    rospy.loginfo(data.fields)
    
    # if points.size == 0:
    #     return

    # # Here, you would add the transformation logic to project the 3D points onto a 2D plane.
    # # For simplicity, let's assume we're directly using the 'z' values as pixel intensities for a depth image.
    
    # # Normalize depth values for visualization
    # depth_image = (points[:, 2] - points[:, 2].min()) / (points[:, 2].max() - points[:, 2].min()) * 255
    # depth_image = depth_image.astype(np.uint8)
    
    # # Reshape the depth image to your desired image size
    # # This example assumes a square image shape for simplicity; adjust as needed.
    # image_size = (640,480)
    # depth_image = depth_image.reshape(image_size)
    
    # # Convert the depth image to a ROS Image message and publish it
    # depth_image_msg = self.bridge.cv2_to_imgmsg(depth_image, encoding="mono8")
    # self.image_publisher.publish(depth_image_msg)

if __name__ == '__main__':
    try:
        rospy.init_node('pointcloud_to_image', anonymous=True)
        
        # Initialize CV Bridge
        bridge = CvBridge()
        
        # Create a subscriber to the point cloud data
        pc_subscriber = rospy.Subscriber("/camera/depth/points", PointCloud2, callback)
        
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
