Since the file was huge, I divided the submission files into 3 parts, Please find: 1) Assignment5.7z which contains the codes and scripts 2)Assignment5_dependencies.7z - for dependencies 3)Assignment5_videos_and_readme
Part 1: Line Following

Coded by: Adithya Suresh, Rushikesh Kharade, Nicholas Yang

There are two files, one for running the bot in simulation world and the other for running the turtlebot in real world

Implementation:

First the image dimensions detected by the camera has many pixels and the desired pixel is selected by 'crop_img' up to the length of the yellow line. Then the cropped image is used to convert the RGB channels to HSV channels. The yellow channel is only selected by creating an upper and a lower threshold for the yellow color hsv channel and a mask is applied in that range. The center position in any instance is determined using the cv2.moments() function and the height and the width values are divided by 2 for the exact center position. The controller was designed with error calculation by setting the central height as reference and the original width was divided by 2 to maintain the relative center position while the bot travels. The linear x was set to 0.07 since the angular z was set to overall error calculation divided by a threshold value. While performing this part, https://github.com/nsa31/Line-Lane-Follower-Robot_ROS/blob/master/white_yellow_lane_follower_sim.py was used for reference.
In real world ,the yellow line in simulation world was not used. Instead A4 sheet was used. The camera topics that is being subscribed to was changed to raspicam_node/image_raw. 

Part 2 : Apriltag Detection 

Coded by: Rakshitaa Geetha Mohan and Avinash Pallela

Implementation:

Tag Follower was implemented in the real world. The raspicamera was fixed using mounts and cellotape. The camera was connected to the Raspberry pi board. The Apriltag_ros raspicamera node
packages were installed. The apriltag_ros package could not be made into a package and the catkin_make_isolated had to be used. This created duplicate build_isolated and devel_isolated files which had to be sourced. The camera was calibrated using chessboard-like image and the intrinsic parameters of the camera were found out and comitted. The ids of tags to be detected were added in the tags.yaml. The launch file was changed so that the camera topic that is being published is the right one from the camera. The raspicam publishes compressed images which was changed using a command as documented below After the camera could detect the tag, a python file was created to make the turtlebot follow the tag. The aprildetectionsArray message had the coordinates of the Apriltag with respect to camera frame. This was used as the error and the turtlebot was steered accordingly with a proportional gain multiplied to the steering inputs. 

Steps followed:
Step 1:roscore
Step 2: ssh into turtlebot and type the command: roslaunch turtlebot3_bringup turtlebot3_robot.launch
Step 3: roslaunch turtlebot3_bringup turtlebot3_rpicamera.launch
Step 4: source the devel_isolated file
Step 5:rosrun image_transport republish compressed in:=raspicam_node/image raw out:=raspicam_node/image_raw
Step 6:roslaunch apriltag_ros continuous_detection.launch
Step 7:rqt_image_view - This command is used to view the video feed of the camera. Make sure that it has been changed to the right topic which is: tag_detection_image

NOTE:
Do not connect and run the bot on cell phone's mobile data because it did not work. 
The line follower was implemented in real world and was made to follow white line. There were lot of problems, because there were times when there was white light reflected off the floor or any shiny surface which the bot detected and changed its course of movement.
