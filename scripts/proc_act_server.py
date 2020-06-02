#!/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from simple_webcam.srv import Image_Proc,Image_ProcResponse
from simple_webcam.msg import image_procAction,image_procGoal,image_procFeedback,image_procResult
import actionlib

bridge = CvBridge()

class ImgProcAction(object):
	_feedback = image_procFeedback()
	_result = image_procResult()

	def __init__(self):
		self._as = actionlib.SimpleActionServer('image_proc', image_procAction, execute_cb=self.execute_cb, auto_start = False)
		self._as.start()

	def execute_cb(self,goal):
		rospy.loginfo("Started process")
		r = rospy.Rate(1)
		success = True

		img = bridge.imgmsg_to_cv2(goal.image_in, "bgr8")

		W = img.shape[0]
		H = img.shape[1]
		
		
		if W % 3 == 0:
			w = [0, W/3, 2*W/3, W] 
		else:
			w = [0, int(W/3), int(2*W/3) + 1, W]

		if H % 3 == 0:
			h = [0, H/3, 2*H/3, H]
		else:
			h = [0, int(H/3), int(2*H/3) + 1, H]
		
		for i in range(3):
			for j in range(3):
				rospy.loginfo("Processing %d %d",i,j)
				img[w[i]:w[i+1],h[j]:h[j+1]] = cv2.blur(img[w[i]:w[i+1],h[j]:h[j+1]],(10,10))

				if self._as.is_preempt_requested():
					rospy.loginfo('%s: Preempted' % self._action_name)
					self._as.set_preempted()
					success = False
					break
				self._feedback.image_inter = bridge.cv2_to_imgmsg(img, "bgr8") 
				self._as.publish_feedback(self._feedback)
				r.sleep()
			if self._as.is_preempt_requested():
				break

		if success:
			self._result.image_out = bridge.cv2_to_imgmsg(img, "bgr8")
			self._as.set_succeeded(self._result)
			rospy.loginfo("Result sent")

if __name__ == '__main__':
    rospy.init_node('proc_action_server')
    server = ImgProcAction()
    rospy.spin()	