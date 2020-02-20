#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    
    while not rospy.is_shutdown():
        vel_msg.linear.x = 0.2
  
        t0 = float(rospy.Time.now().to_sec())
        current_distance = 0

        while(current_distance < 2):
           
            velocity_publisher.publish(vel_msg)
            
            t1=float(rospy.Time.now().to_sec())
            
            current_distance= 0.2*(t1-t0)
        
        vel_msg.linear.x = 0
        
        velocity_publisher.publish(vel_msg)

        #Taking a turn of 90 degrees at 0.2rad/s
        vel_msg.angular.z = 0.2
        t0a = float(rospy.Time.now().to_sec())
        current_angle = 0
        while(current_angle < (90*PI/180)):
            velocity_publisher.publish(vel_msg)
            t1a = float(rospy.Time.now().to_sec())
            current_angle = 0.2*(t1a-t0a) 
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        
     
if __name__ == '__main__':
    try:
        #Testing our function
        move()
        move()
        move()
        move()
        
    except rospy.ROSInterruptException: pass
  
