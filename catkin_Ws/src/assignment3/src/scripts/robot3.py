#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import copy
import numpy as np

final_range = []

def callback(msg):
   global g_range_ahead
   #print(msg.ranges[359])
   final_range = msg.ranges[-10:]+msg.ranges[:10]     
   np.array(final_range)
   g_range_ahead = np.mean(final_range)
   print(final_range)
   #print(msg.ranges)

g_range_ahead = 1

rospy.init_node('robot3',anonymous=True)
sub = rospy.Subscriber('/scan',LaserScan,callback)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
move = Twist()
move.linear.y = 0
move.linear.z = 0
move.angular.x = 0
move.angular.y = 0
move.angular.z = 0
while (1):
    move.linear.x = 0.2
    if g_range_ahead < 0.5:
        move.linear.x = 0
    else:
        move.linear.x = 0.2
    pub.publish(move)