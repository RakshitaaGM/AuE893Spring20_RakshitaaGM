**Part 1**
The launch file made for Part 1 of the assignment requires requires input from the user. The launch file must be launched as such : $roslaunch assignment3 move.launch code:=circle for the turtlebot to move in a circle or$roslaunch assignment3 move.launch code:=square for the turtlebot3 to move in a square. 

**The Turtlebot moving in a circle:**
![image](https://user-images.githubusercontent.com/59737146/118004966-f4589d80-b317-11eb-9492-82f2b46ff4c3.png)

**The Turtlebot moving in a square:**
![image](https://user-images.githubusercontent.com/59737146/118005389-574a3480-b318-11eb-8985-3b25f0a84337.png)

**Part2**
The launch file does not require any input from the user. The turtlebot3_wall.world was created and is present in the world folder. The scripts folder contains the python script which is used for carrying out the task. The lidar scans all the values from 0 to 360 degrees with zero starting from the start position of the turtlebot. These values are in the /scan topic from which it is subscribed. To get the accurate distance, the distance value measured by the lidar in a small window of 10 degrees to the left and right of the 0 degree(center value is taken and mean was found. If the distance value was found to be less than 0.5, the velocity of the turtlebot was set 0 by publishing the same to \cmd _vel topic.

