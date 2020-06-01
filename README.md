# simple_webcam

## Nodes
**1. video_pub**<br>
Publishes video stream from webcam on topic **video_stream**.<br>

**2. video_sub**<br>
Subscribes to topic **video_stream** and displays the stream.<br>

**3. image_proc_server**<br>
Server for the service **image_proc**.<br>

**4. image_proc_server**<br>
Subscribes to topic **video_stream** and call the service **image_proc**.<br>

## Topics

**1. video_stream**<br>
Of message type **sensor_msgs/Image** used for carrying webcam video stream.<br>

## Services

**1. image_proc**<br>
<br>
**Arguments:**
* image_in (Of type **sensor_msgs/Image**)
* BLUR (Of type Bool) 
* CROP (Of type Bool)
* crop_x (Of type Int16)
* crop_y (Of type Int16)
* crop_H (Of type Int16)
* crop_W (Of type Int16)

