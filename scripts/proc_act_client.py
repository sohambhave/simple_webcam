#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse
import actionlib
from simple_webcam.msg import image_procAction,image_procGoal,image_procFeedback,image_procResult

bridge = CvBridge()

img_rec_flag = False

class my_img:
	def __init__(self):
		self.img = bridge.cv2_to_imgmsg(np.zeros((500,500,3), np.uint8), "bgr8")
		self.img_rec_flag = False
	def get_img(self):
		return(self.img)
	def set_img(self,img):
		self.img = img
	def set_flag(self):
		self.img_rec_flag = True
	def get_flag(self):
		return(self.img_rec_flag)

I = my_img()

def video_callback(Image_msg):
	I.set_img(Image_msg)
	I.set_flag()

def callback_feedback(feedback):
	rospy.loginfo("Feedback recieved")	
	cv_feedback = bridge.imgmsg_to_cv2(feedback.image_inter, "bgr8")
	cv2.namedWindow("Camera 1 Blur feedback")
	cv2.imshow('Camera 1 Blur feedback',cv_feedback)
	cv2.waitKey(1)

def proc_act_client():
	client = actionlib.SimpleActionClient('image_proc', image_procAction)

	# Waits until the action server has started up and started
	# listening for goals.
	client.wait_for_server()

	# Creates a goal to send to the action server.
	goal = image_procGoal(I.get_img())

	# Sends the goal to the action server.
	client.send_goal(goal,feedback_cb=callback_feedback)

	# Waits for the server to finish performing the action.
	client.wait_for_result()
	
	rospy.loginfo("Result recieved")
	cv2.destroyAllWindows()
	return client.get_result()

if __name__ == '__main__':
	rospy.init_node('proc_act_client', anonymous=True, disable_signals = True)
	rospy.loginfo("Starting Image Processing Action Client")
	rospy.Subscriber("video_stream", Image, video_callback)
	while not I.get_flag():
		pass
	# try:
	cv_result = bridge.imgmsg_to_cv2(proc_act_client().image_out, "bgr8")
	# cv2.namedWindow("Camera 1 Blur result")
	# cv2.imshow('Camera 1 Blur result',cv_result)
	# cv2.waitKey(0)
	# # except rospy.ROSInterruptException:
	# 	rospy.loginfo("program interrupted before completion")
	cv2.destroyAllWindows()
	rospy.signal_shutdown("Recieved responce. Shutting down client")
