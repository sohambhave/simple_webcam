#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse
#import simple_webcam.srv

bridge = CvBridge()

def image_proc_handle(req):
	img = req.image_in
	img = bridge.imgmsg_to_cv2(img, "bgr8")
	
	if req.BLUR == True:
		img = cv2.blur(img,(10,10))
	
	if req.CROP == True:
		img = img[req.crop_y:req.crop_y+req.crop_H,req.crop_x:req.crop_x+req.crop_W]

	img = bridge.cv2_to_imgmsg(img, "bgr8")
	return(Image_ProcResponse(img))


def image_proc_server():
	rospy.init_node('image_proc_server', anonymous=True)
	rospy.loginfo("Starting Image Processing Server")
	s = rospy.Service('image_proc', Image_Proc, image_proc_handle)
	rospy.spin()
	
		
if __name__ == '__main__':
	image_proc_server()
	rospy.loginfo("Closing Image Processing Server")
	