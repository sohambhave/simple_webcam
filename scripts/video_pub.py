#!/usr/bin/env python

import rospy
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def video_pub():
	#pub = rospy.Publisher('video_pub', String, queue_size=10)
	rospy.init_node('video_pub', anonymous=True)
	#rate = rospy.Rate(10) # 10hz
	#while not rospy.is_shutdown():
	while True:
		ret, frame = cap.read()
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
