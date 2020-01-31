import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
PI = 3.14

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self,goal_x,goal_y):
        #goal_pose = Pose()
        
        vel_msg = Twist()

        angle = (atan2(goal_y - self.pose.y, goal_x - self.pose.x) - self.pose.theta)
        print(self.pose.y)
        print(goal_y - self.pose.y)
        
        while abs(angle) > 0.01:
            print(angle)
            vel_msg.linear.x = 0 
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 5* (atan2(goal_y - self.pose.y, goal_x - self.pose.x) - self.pose.theta)
            self.velocity_publisher.publish(vel_msg)
            angle = (atan2(goal_y - self.pose.y, goal_x - self.pose.x) - self.pose.theta)
         
        dist = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        print(dist)
        while dist >= 0.7:
            if dist >= 0.7:
                
                vel_msg.linear.x = 5 * sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0 
                self.velocity_publisher.publish(vel_msg)
            dist = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        self.rate.sleep()    
        
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        
      

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal(5,5)
        #y = turtlebot()
      
        #y.move2goal(8,5)
        #z = turtlebot()
        #z.move2goal(8,8)
        #a = turtlebot()
        #a.move2goal(5,8)
        #b = turtlebot()
        #b.move2goal(5,5)
        x.move2goal(8,5)
        x.move2goal(8,8)
        x.move2goal(5,8)
        x.move2goal(5,5)
    except rospy.ROSInterruptException: pass
