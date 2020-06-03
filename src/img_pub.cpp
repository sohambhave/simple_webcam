/*

Author: Lentin Joseph
Name : hello_world.cpp

This node will republish the message which is subscribing 

*/

#include <pluginlib/class_list_macros.h>
#include <nodelet/nodelet.h>

#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <std_msgs/String.h>
#include <stdio.h>
#include "opencv2/opencv.hpp"

using namespace cv;

namespace simple_webcam
{


class Img_Pub : public nodelet::Nodelet
{


private:
	virtual void onInit()
	{
		ros::NodeHandle& private_nh = getPrivateNodeHandle();
		//ros::NodeHandle n;
		NODELET_DEBUG("Initialized the Nodelet");
		//pub = n.advertise<std_msgs::String>("msg_out",5);
		//sub = n.subscribe("msg_in",5, &Hello::callback, this);
		timer_ = private_nh.createTimer(ros::Duration(1.0), boost::bind(& Img_Pub::timerCb, this, _1));
		//pub = private_nh.advertise<sensor_msgs::Image>("img_stream",5);
		pub = private_nh.advertise<std_msgs::String>("str_stream",5);
		//sub = private_nh.subscribe("msg_in",5, &Img_Pub::callback, this);
	}
	/*
	void callback(const std_msgs::StringConstPtr input)
	{

		std_msgs::String output;
		output.data = input->data;

		NODELET_DEBUG("Message data = %s",output.data.c_str());
		ROS_INFO("Message data = %s",output.data.c_str());
		pub.publish(output);
		
	}*/
	void timerCb(const ros::TimerEvent& event){
	  // Using timers is the preferred 'ROS way' to manual threading
	  //NODELET_INFO_STREAM("The time is now " << event.current_real);
	  /*
	  Mat frame;
	  cap >> frame;
	  if (frame.empty())
	    break;
	  imshow( "Frame", frame );
	  waitKey(1);
	  pub.publish(new_message);
	  */ 
	  std_msgs::String output;
      output.data = "Hello world";
      ROS_INFO("Message data = %s",output.data.c_str());
      pub.publish(output);
	}

  ros::Publisher pub;
  ros::Timer timer_;
  //VideoCapture cap(0); 
};

}


PLUGINLIB_DECLARE_CLASS(simple_webcam,Img_Pub,simple_webcam::Img_Pub, nodelet::Nodelet);

PLUGINLIB_EXPORT_CLASS(simple_webcam::Img_Pub,nodelet::Nodelet);
