#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def lidar(msg):
    left_range =0
    right_range=0
    for i in range(1,15):
        left_range = left_range + msg.ranges[i]       
    left_dist = left_range/15

    for i in range(345,360):
        right_range = right_range + msg.ranges[i]      
    right_dist = right_range/15
    
    vel_msg = Twist()
    
    if msg.ranges[0]>1 and right_dist>1 and left_dist>1:
        vel_msg.linear.x = 0.2 #Go straight when all the distances are inf
        vel_msg.angular.z = 0.0
        
    else:
      
        vel_msg.linear.x = 0.0 
        vel_msg.angular.z = 1.2*(left_dist - right_dist)
       

    pub.publish(vel_msg) 
   
rospy.init_node('wallfollower',anonymous=True)
sub = rospy.Subscriber('/scan',LaserScan,lidar)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
vel_msg=Twist()
rospy.spin()
