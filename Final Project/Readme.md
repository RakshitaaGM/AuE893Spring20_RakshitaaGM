AuE893 Final Project Gazebo Model

Important notes:
1)The launch file is in auefinals -> turtlebot3_auefinals -> launch
2)The launch file includes the launch of hector SLAM mapping. THe hectaor SLAM package must also be installed for this to work.
3)To run this package, the dependency packages must be installed : 1)person_sim 2)turtle_3d 3)People_detection package 4)gazebo_apriltag
4)Since the trigger for each of the functional block depends on TinyYOLO, the results are perfect when the FPS is around 1 - 1.8 FPS
5)To run : roslaunch turtlebot3_auefinals turtlebot3_autonomy_final.launch


Task 1: Wall following and Obstacle avoidance
Contributors: Rakshitaa Geetha Mohan and Rushikesh Kharade
Code Implementation: The lidar scan values were used for this purpose. The difference between the average of the lidar scan values on the left side and right side were used to calculate the error. The error along with a controller gain value (in this case, 1.8) was used to give the steer required for the bot. Lidar distance value at 0 degree was also taken to take the obstacle in the front into account. The error value can never be exactly zero for the bot to go straight, therefore, a range of 0.1 was taken buffer.   
 ![image](https://user-images.githubusercontent.com/59737146/118009053-b52c4b80-b31b-11eb-9e73-e0ed01d798da.png)


Task 2: Line following and Stop sign detection
Contributors: Adithya Suresh and Nicholas Yang
Code Implementation: The code for the line following and stop sign detection block was defined in a function camera_callback(), where the function will be executed when the trigger flag 'f' is set to the value 1 and if it detects only one person using the camera with respect to the Tiny YOLO frame. Since the turtlebot3 burger model has a camera attached as noted from the waffle_pi model xacro, the image has to be cropped at a particular height and width values after careful consideration. The line following needs to be done with the detection of yellow line in the gazebo environment and the hsv values for the yellow color is mentioned for the masking of the image. When the bot follows the yellow line and detects the stop_sign which was accessed using the ID of the 'stop_sign' class and the time for waiting was set to 3 seconds with respect to the current time using rospy.get_time(). The velocity of the bot, both linear.x and angular.z was set to 0 if it detects the stop sign. Moreover, if the bot is done with the stop sign detection and stayed in that place for 3 seconds, it will establish the velocity with respect to the P controller of the line following part of the code. The line following was performed using a P controller with the linear.x value to be 0.1 and the angular.z value was set with respect to the negative of error value/ 930 after tuning the parameters for controller.
The screenshot of stop sisgn detection is in 'Pictures' folder
Task 3:Leg tracking
Contributors: Adithya Suresh and Krishna Sai Avinash Pallela
Code Implementation: The leg tracking part was performed using the functions bot_location() and legtracking_callback() where in the first function, the x, y and the yaw of the bot was taken and found. The orientation of the bots were taken and a simple transformation of euler from the quaternion was made to get the yaw of the bot. The relative x and y positions of the bot was also figured out by accessing the position of the class. In the legtracking_callback() function, the x, y and the z position of the person was taken. Here the absolute value was prescribed to the y position of the bot because of the rotation in the counter-clockwise direction which will give the negative value to the y position. This function will be functionable when the Tiny YOLO detection of two person is detected which corresponds to the two legs of the person. Moreover, the leg tracking works with maintaing the relative distance between the person and the human as 0.3 units and the relative distance is calculated using the euclidean distance formula. The change in angle of the bot was calculated using the slope between the person and the bot. The error in angle is calculated by the difference between the change in angle and yaw of the bot. When the distance is less than 0.3 units, the robot's velocity should be 0 and this was achieved by setting linear.x and angular.z to 0. And if the distance is greater than 0.3 units the P controller is used to change the linear.x value to the product of euclidean distance and the linear P controller value and the angular.z to the product of error angle and angular P controller value and the velocities are published

Task 4: Code integration
Contributors: Rakshitaa Geetha Mohan and Adithya Suresh
Code Implementation: All the required nodes for the tasks performed above are initialized in the beginning and they will be running simultaneously. Triggers were used to switch between the different functions. For switching the function from wall following code to Line following, an April Tag has been placed in the world. As the April Tag was detected as a person (because of low accuracy detection of TinyYOLO), we could not differentiate between the actual person and the April Tag. But, when the bot reaches the actual person, it identifies both the legs as two persons. This was used as the trigger for leg tracking function. 
The pictures of first and second triggers are present in the 'Pictures' folder


The final video is present in 'videos' folder

