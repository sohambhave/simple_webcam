#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse
#import simple_webcam.srv

bridge = CvBridge()

def image_proc_client(BLUR,CROP,crop_x, crop_y, crop_H, crop_W):
	rospy.wait_for_service('image_proc')
	try:
		image_proc = rospy.ServiceProxy('image_proc', Image_Proc)
		resp1 = image_proc(BLUR,CROP,crop_x, crop_y, crop_H, crop_W)
		cv_image_out = bridge.imgmsg_to_cv2(resp1.image_out, "bgr8")
		return cv_image_out
	except rospy.ServiceException as e:
		print("Service call failed: %s"%e)

def usage():
	blur_img = image_proc_client(True, False, 0, 0, 0, 0)
	cv2.imshow('Camera 1 Blur',blur_img)
	crop_img = image_proc_client(False, True, 200, 100, 200, 200)
	cv2.imshow('Camera 1 Crop',crop_img)
	cv2.waitKey(1)
	

def video_sub():
	rospy.init_node('image_proc_client', anonymous=True)
	rospy.loginfo("Started Image Processing Client")
		
if __name__ == '__main__':
	video_sub()
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		usage()
		rate.sleep()
	rospy.loginfo("Closing subscriber")
	cv2.destroyAllWindows()
	