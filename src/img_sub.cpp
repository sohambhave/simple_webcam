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



namespace simple_webcam
{

class Img_Sub : public nodelet::Nodelet
{


private:
	virtual void onInit()
	{
		ros::NodeHandle& private_nh = getPrivateNodeHandle();
		//ros::NodeHandle n;
		NODELET_DEBUG("Initialized the Nodelet");
		//pub = n.advertise<std_msgs::String>("msg_out",5);
		//sub = n.subscribe("msg_in",5, &Hello::callback, this);
		//pub = private_nh.advertise<sensor_msgs::Image>("img_stream",5);
		sub = private_nh.subscribe("/nodelet_pub/str_stream",5, &Img_Sub::callback, this);

	
	}
	
	void callback(const std_msgs::StringConstPtr input)
	//void callback(const sensor_msgs::ImageConstPtr input)
	{
		ROS_INFO("Msg recieved : %s",(input->data).c_str());
		//NODELET_DEBUG
	}

  ros::Subscriber sub;

};

}


PLUGINLIB_DECLARE_CLASS(simple_webcam,Img_Sub,simple_webcam::Img_Sub, nodelet::Nodelet);

PLUGINLIB_EXPORT_CLASS(simple_webcam::Img_Sub,nodelet::Nodelet);
