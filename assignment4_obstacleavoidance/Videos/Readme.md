                            Obstacle avoidance

Part 1 :Wall following

Coded by:Rakshitaa Geetha Mohan and Rushikesh Kharade

Implementation:

First, the left and right distances were calculated. A sweep of distance values in left and right side was taken and the mean was found for this purpose. 
The difference between right and left values was used to determine the error. If the distance on right side was greater than the left side, then the bot was steered right. The Proportional controller was designed accordingly. The proportional gain was tested for a variety of values and the bot gave nearly perfect result for 1.1. Since the error can never be zero, a threshold of 0.2 was given, i.e, the bot will go straight if the difference between the left and right values is less than 0.2 and greater than -0.2.

In the terminal window: "roslaunch assignment4_obstacleavoidance follower.launch"

The user should have a copy of the world file - "turtlebot3_wallfollowing.world" in their turtlebot3_gazebo package. I tried to do this by having a copy in the world folder and changing the directory address in the launch, but it never worked. I had even mailed Adithi regarding this. So, I sought to this method of having a copy of the world file in turtlebot3_gazebo package and it worked perfectly.

Part 2: Obstacle avoidance:

Coded by: Adithya Suresh, Nicholas Yang, Avinash Pallela

Implementation:

This code was written based on basics that was learned from the model code in this website, "https://github.com/enansakib/obstacle-avoidance-turtlebot/blob/master/src/naive_obs_avoid_tb3.py". A range of 15 degrees from left and right was taken and mean was found. The bot goes straight when the distances at 0 degree, left and right turn out to be infinity. Else, the bot will steer either to left or right based on the error(difference between left and right). A proportional controller was used for this purpose. A variety of values were tested and nearly perfect results were observed for a proportional gain of 1.2.

In the terminal window: "roslaunch assignment4_obstacleavoidance obst_avoidance.launch"


Part 3: Obstacle Avoidance on Turtlebot

Contribution : All the members

The terminal window should be running roscore. In another window, the turtlebot3_bringup must be running. In another window, the world, "turtlebot3_obstacle avoidance.world" must be open.

In the terminal window: "python wander.py"

In the video, it can be can seen that the bot was not able to react to sudden changes in the environment. I could NOT edit the background noise in the video. 




References and Citation:
[1]https://github.com/enansakib/obstacle-avoidance-turtlebot/blob/master/src/naive_obs_avoid_tb3.py




 
