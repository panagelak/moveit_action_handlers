#! /usr/bin/env python
import rospy
# Brings in the SimpleActionClient
import actionlib

from moveit_action_handlers.msg import MoveToJointsMoveItAction
from moveit_action_handlers.msg import MoveToJointsMoveItGoal
# property value pair joint names joint values
from moveit_action_handlers.msg import PropertyValuePair


def moveit_tojoints_client():
    # ARM
    arm_client = actionlib
    arm_client = actionlib.simple_action_client.SimpleActionClient(
        'move_tojoints_action_server/arm/action', MoveToJointsMoveItAction)

    arm_client.wait_for_server()

    # Creates a goal to send to the action server arm.

    goal = MoveToJointsMoveItGoal()
    goal.endEffectorVelocity = 0.5
    goal.endEffectorAcceleration = 0.5
    goal.timeoutSeconds = 10
    # arm joint names list
    joint_names = ["shoulder_pan_joint", "shoulder_lift_joint",
                   "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"]
    # arm joint values (calibrated pose)
    joint_values = [0.0, 0.0, 1.57, 0.0, 0.0, 0.0]
    # retracted pos
    #joint_values = [0.0, -1.1, 2.0, 0.0, -1.5707, 0.0]
    
    # create and fill joint value pairs to goal
    for i in range(len(joint_names)):
        joint_pair = PropertyValuePair()
        joint_pair.name = joint_names[i]
        joint_pair.value = joint_values[i]
        # append to goal
        goal.joint_pairs.append(joint_pair)
    


    # send goal
    arm_client.send_goal(goal)

    # Waits for the server to finish performing the action.
    arm_client.wait_for_result()


if __name__ == '__main__':

    rospy.init_node('test_joints_client_python_node')
    result = moveit_tojoints_client()
