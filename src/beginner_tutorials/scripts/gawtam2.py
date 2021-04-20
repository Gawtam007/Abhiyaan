#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String

def gawtam2():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rospy.init_node('gawtam2', anonymous=True)
#   r = rospy.Rate(10) # 10hz
#   while not rospy.is_shutdown():
    str1 = "Team Abhiyaan"
    rospy.loginfo(str1)
    pub.publish(str1)
#        r.sleep()

if __name__ == '__main__':
    try:
        gawtam2()
    except rospy.ROSInterruptException:
        pass
