#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import tf_transformations

def pos(navigator : BasicNavigator,pose_x,pose_y,orient_z):
    qx , qy , qz , qw = tf_transformations.quaternion_from_euler(0.0 , 0.0 , orient_z)
    pose=PoseStamped()
    pose.header.frame_id='map'
    pose.header.stamp=navigator.get_clock().now().to_msg()
    pose.pose.position.x=pose_x
    pose.pose.position.y=pose_y
    pose.pose.position.z=0.0
    pose.pose.orientation.x=qx
    pose.pose.orientation.y=qy
    pose.pose.orientation.z=qz
    pose.pose.orientation.w=qw
    return pose
def main():
    rclpy.init()
    nav=BasicNavigator()
    
    initial_pose=pos(nav,0.0,0.0,0.0)
    nav.setInitialPose(initial_pose)

    nav.waitUntilNav2Active()

    goal1=pos(nav,-2.5,2.5,1.57)
    goal2=pos(nav,-1.0,-3.0,3.14)
    goal3=pos(nav,2.0,2.0,-1.57)
    goal4=pos(nav,0.0,4.0,-1.57)
    

    waypoints=[goal1,goal2,goal3,goal4]
    nav.followWaypoints(waypoints)
    for i in range(0,3):
        while not nav.isTaskComplete():
            feedback=nav.getFeedback()
            print(feedback)
    print(nav.getResult())

    rclpy.shutdown()

if __name__=="__main__":
    main()
