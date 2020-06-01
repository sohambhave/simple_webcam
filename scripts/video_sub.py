#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def video_callback(Image_msg):
	cv_image = bridge.imgmsg_to_cv2(Image_msg, "bgr8")
	cv2.imshow('Camera 1',cv_image)
	cv2.waitKey(1)
	

def video_sub():
	rospy.init_node('video_sub', anonymous=True)
	rospy.Subscriber("video_stream", Image, video_callback)
	rospy.loginfo("Started subscriber")
	rospy.spin()

if __name__ == '__main__':
	video_sub()
	rospy.loginfo("Closing subscriber")
	cv2.destroyAllWindows()