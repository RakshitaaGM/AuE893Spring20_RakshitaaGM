#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


def lidar(msg):
    
    front_range = 0
    left_range = 0
    right_range = 0
    #To calculate thedistance in the right
    c1=1;c2=1
    steer=0
    for i in range(265,359):
        if msg.ranges[i]<=2:
            c1+=1
            right_range = right_range + msg.ranges[i] 
           
    	right_dist = right_range/c1#Finding average
         
    for j in range(0,95):
        if msg.ranges[j]<=2:
             c2+=1
             
             left_range = left_range + msg.ranges[j]
    	left_dist = left_range/c2 #Finding average
    
    vel_msg = Twist()
     
    steer = left_dist-right_dist
    
       
    if steer <=0.2 and steer >= -0.2:
       print 'left',left_dist
       print 'right', right_dist
       vel_msg.linear.x = 0.4
       vel_msg.linear.y = 0
       vel_msg.linear.z = 0
       vel_msg.angular.x = 0
       vel_msg.angular.y = 0
       vel_msg.angular.z = 0
       pub.publish(vel_msg)
    
    else:
       print'steer=', steer*1.2
       print 'left',left_dist
       print 'right', right_dist
       vel_msg.linear.x = 0.1 #To make the turns smooth
       vel_msg.linear.y = 0
       vel_msg.linear.z = 0
       vel_msg.angular.x = 0
       vel_msg.angular.y = 0
       vel_msg.angular.z = steer*1.1 # Proportional controller
       pub.publish(vel_msg)
         
rospy.init_node('wallfollower',anonymous=True)
sub = rospy.Subscriber('/scan',LaserScan,lidar)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
vel_msg=Twist()
rospy.spin()
