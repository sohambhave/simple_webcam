#include "opencv2/opencv.hpp"
//#include <iostream>

//using namespace std;
using namespace cv;

int main(){

  // Create a VideoCapture object and use camera to capture the video
  VideoCapture video_capture(0); 

  // Check if camera opened successfully
  if(!video_capture.isOpened())
  {
    //cout << "Error opening video stream" << endl; 
    return -1; 
  } 

  // Default resolution of the frame is obtained.The default resolution is system dependent. 
  //int frame_width = video_capture.get(CV_CAP_PROP_FRAME_WIDTH); 
  //int frame_height = video_capture.get(CV_CAP_PROP_FRAME_HEIGHT); 
  
  // Define the codec and create VideoWriter object.The output is stored in 'outcpp.avi' file. 
  //VideoWriter video("outcpp.avi",CV_FOURCC('M','J','P','G'),10, Size(frame_width,frame_height)); 
  Mat edges;
  namedWindow("edges",1);
  while(1)
  { 
    Mat frame; 
    
    // Capture frame-by-frame 
    video_capture >> frame;
    cvtColor(frame,edges,COLOR_BGR2GRAY);
    // If the frame is empty, break immediately
    //if (frame.empty())
    //  break;
    
    // Write the frame into the file 'outcpp.avi'
    //video.write(frame);
   
    // Display the resulting frame    
    imshow("edges", edges );
 
    // Press  ESC on keyboard to  exit
    /*
    char c = (char)waitKey(1);
    if( c == 27 ) 
      break;
    */
    if(waitKey(30) >= 0) break;
  }

  // When everything done, release the video capture and write object
  video_capture.release();
  //video.release();

  // Closes all the windows
  destroyAllWindows();
  return 0;
}

