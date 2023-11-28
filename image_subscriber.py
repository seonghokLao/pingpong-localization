import rospy
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage

i1 = 0
i2 = 0
i3 = 0

def callback1(data):
    bridge = CvBridge()
    global i1
    cv_img = bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv2.imwrite('/home/core-robotics/sean/imgs/camera1_' + str(i1) + '.jpg', cv_img)
    i1 += 1

def callback2(data):
    bridge = CvBridge()
    global i2
    cv_img = bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv2.imwrite('/home/core-robotics/sean/imgs/camera2_' + str(i2) + '.jpg', cv_img)
    i2 += 1

def callback3(data):
    bridge = CvBridge()
    global i3
    cv_img = bridge.compressed_imgmsg_to_cv2(data, desired_encoding="passthrough")
    cv2.imwrite('/home/core-robotics/sean/imgs/camera3_' + str(i3) + '.jpg', cv_img)
    i3 += 1

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera_1/image_color/compressed", CompressedImage, callback1)
    rospy.Subscriber("/camera_2/image_color/compressed", CompressedImage, callback2)
    rospy.Subscriber("/camera_3/image_color/compressed", CompressedImage, callback3)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()