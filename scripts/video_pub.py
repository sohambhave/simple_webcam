#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0) #Video capture object for first camera
bridge = CvBridge()

def video_pub():
	video_pub = rospy.Publisher('video_stream', Image, queue_size = 10) # Publisher with message type sensor_msgs.msg/Image
	rospy.init_node('video_pub', anonymous=True)
	rospy.loginfo("Starting Webcam")
	while not rospy.is_shutdown():
		ret, cv_image = cap.read()
		Image_msg = bridge.cv2_to_imgmsg(cv_image, "bgr8")
		video_pub.publish(Image_msg)
		
if __name__ == '__main__':
	video_pub()
	rospy.loginfo("Closing Webcam")
	cap.release()