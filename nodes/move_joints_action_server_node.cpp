/**
 * @file move_joints_action_server_node.cpp
 * @author Panagiotis Angelakis
 * @brief
 * @version 0.1
 * @date 03-09-2020
 *
 * @copyright Copyright (c) 2020
 *
 */
#include <csignal>
#include <ros/ros.h>

#include "moveit_action_handlers/move_joints_action_server.h"

std::unique_ptr<MoveJointsActionServer> moveit_joints_action_ptr;

void signalHandler(int signum) {
  ROS_WARN_STREAM("[moveit_joints_motion_action] Interrupt signal (" << signum << ") received.\n");

  moveit_joints_action_ptr.reset();

  exit(signum);
}

int main(int argc, char **argv) {
  
  const std::string server_node_name = "move_joints_action_server_node";
  ros::init(argc, argv, server_node_name, ros::init_options::NoRosout);

  ros::NodeHandle nh("");
  ros::NodeHandle nh_priv("~");

  // register signal SIGINT and signal action
  signal(SIGINT, signalHandler);

  ROS_INFO_STREAM("[" << server_node_name << "]"
                      << "Initializing node with ns :" << nh.getNamespace());
  moveit_joints_action_ptr.reset(new MoveJointsActionServer(nh, nh_priv));

  if (!moveit_joints_action_ptr->initialize()) {
    ROS_ERROR_STREAM("["
                     << "Moveit Joints Action Initialization Error"
                     << "]");
    exit(1);
  }
  ros::spin();
  return 1;
}
