#!/usr/bin/python

"""
Class for control point navigation of turtlebot3.
"""
import rospy
import tf
from geometry_msgs.msg import Point, Pose, Quaternion, PoseStamped
from actionlib_msgs.msg import GoalStatusArray
import time
import math
import sys 

class NavigatorCtrl():
    def __init__(self):
        rospy.loginfo("Setting Up the Node...")
        
        rospy.init_node('navigator_node')

        self._nav_msg       = PoseStamped()

        #--- Create the nav publisher 
        self.ros_pub_nav_msg = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)
        rospy.loginfo("> Publisher corrrectly initialized")

        #--- Create subscriber
        self.ros_sub_stat   = rospy.Subscriber("/move_base/status", GoalStatusArray, self.get_goal_status)

        self.x = 0.0
        self.y = 0.0
        self.th = 0.0

        self.positions = {}
        self.positions['A']  = [-2.5, 2.5, 90]
        self.positions['B']  = [ 2.0, 2.5, 90]
        self.positions['C']  = [-3.0, 0.5, 90]
        self.positions['Z']  = [4.0, -1.5, 90]
        self.room = 'Z'
        self.goal_stat = 'stoped'
        self.flag = 0
        self.arm  = 0

        #--- Get the last time e got a commands
        self.current_time = rospy.Time.now()

        rospy.loginfo("Initialization complete")


    def send_nav_msg(self):
        self._nav_msg.header.frame_id = "map"
        self._nav_msg.header.stamp = self.current_time

        # set the position
        self._nav_msg.pose = Pose(Point(self.x, self.y, 0.), Quaternion(*self.odom_quat))

        self.ros_pub_nav_msg.publish(self._nav_msg)

    def get_goal_status(self,goal_status):
        #self.goal_stat = goal_status.status_list[0].status
        if goal_status.status_list[0].status == 1 or self.flag == 1:
            self.flag = 1
            if goal_status.status_list[0].status == 3:
                self.goal_stat = 'Arrived'
                self.flag = 0

    def data_from_app(self):
        
        if self.goal_stat == 'Arrived' and self.arm == 1:
            file1 = open("./src/turtlebot3_project/myfile.txt","w") 
            file1.write("Robot Arrived to position: "+self.room) 
            file1.close()
            self.arm  = 0
            rospy.loginfo("Robot Arrived to position: "+self.room)
            sys.exit()

        elif self.arm == 0:
            file1     = open("./src/turtlebot3_project/myfile.txt","r+")  
            myarray   = file1.read()
            if (myarray[0] == 'A' or myarray[0] == 'B' or myarray[0] == 'C' or myarray[0] == 'Z'):
                self.room = myarray[0]
                self.x  = self.positions[myarray[0]][0]
                self.y  = self.positions[myarray[0]][1]
                self.th = self.positions[myarray[0]][2]
            file1.seek(0)
            file1.close()
            self.arm = 1
        rospy.loginfo('Moving...')
        
    @property
    
    def run(self):

        #--- Set the control rate
        rate = rospy.Rate(10)
        data_limit = 0
        self.goal_stat = ""
        self.arm  = 0
        while not rospy.is_shutdown():
            
            self.current_time = rospy.Time.now()
            # compute odometry in a typical way given the velocities of the robot
        
            #self.x = 1.5
            #self.y = 2.5
            #self.th = 90
            self.data_from_app()
            # since all odometry is 6DOF we'll need a quaternion created from yaw
            self.odom_quat = tf.transformations.quaternion_from_euler(0, 0, self.th)
            
            if data_limit < 5 and self.arm == 1:
                self.send_nav_msg()
                data_limit +=1
            #sys.exit()
            rate.sleep()

if __name__ == "__main__":
    navigator     = NavigatorCtrl()
    navigator.run()