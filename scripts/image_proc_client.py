#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse
#import simple_webcam.srv

bridge = CvBridge()

def image_proc_client(Img,BLUR,CROP,crop_x, crop_y, crop_H, crop_W):
	rospy.wait_for_service('image_proc')
	try:
		image_proc = rospy.ServiceProxy('image_proc', Image_Proc)
		resp1 = image_proc(Img,BLUR,CROP,crop_x, crop_y, crop_H, crop_W)
		cv_image_out = bridge.imgmsg_to_cv2(resp1.image_out, "bgr8")
		return cv_image_out
	except rospy.ServiceException as e:
		print("Service call failed: %s"%e)

def video_callback(Image_msg):
	cv_image = bridge.imgmsg_to_cv2(Image_msg, "bgr8")
	cv2.imshow('Camera 1 Raw',cv_image)
	blur_img = image_proc_client(Image_msg, True, False, 0, 0, 0, 0)
	cv2.imshow('Camera 1 Blur',blur_img)
	crop_img = image_proc_client(Image_msg, False, True, 200, 100, 200, 200)
	cv2.imshow('Camera 1 Crop',crop_img)
	cv2.waitKey(1)
	

def video_sub():
	rospy.init_node('image_proc_client', anonymous=True)
	rospy.Subscriber("video_stream", Image, video_callback)
	rospy.loginfo("Started Image Processing Client")
	rospy.spin()	
		
if __name__ == '__main__':
	video_sub()
	rospy.loginfo("Closing subscriber")
	cv2.destroyAllWindows()
	