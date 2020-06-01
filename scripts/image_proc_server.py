#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse

bridge = CvBridge()

class my_img:
	def __init__(self):
		self.img = bridge.cv2_to_imgmsg(np.zeros((500,500,3), np.uint8), "bgr8")
	def get_img(self):
		return(self.img)
	def set_img(self,img):
		self.img = img

I = my_img()

def image_proc_handle(req):
	img = bridge.imgmsg_to_cv2(I.get_img(), "bgr8")
	if req.BLUR == True:
		img = cv2.blur(img,(10,10))
	
	if req.CROP == True:
		img = img[req.crop_y:req.crop_y+req.crop_H,req.crop_x:req.crop_x+req.crop_W]

	img = bridge.cv2_to_imgmsg(img, "bgr8")
	return(Image_ProcResponse(img))

def video_callback(Image_msg):
	I.set_img(Image_msg)
	
def image_proc_server():
	rospy.init_node('image_proc_server', anonymous=True)
	rospy.loginfo("Starting Image Processing Server")
	rospy.Subscriber("video_stream", Image, video_callback)
	s = rospy.Service('image_proc', Image_Proc, image_proc_handle)
	rospy.spin()
	
		
if __name__ == '__main__':
	image_proc_server()
	rospy.loginfo("Closing Image Processing Server")
	