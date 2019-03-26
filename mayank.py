# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mayank.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton, QMessageBox
import rospy 
import actionlib 
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


list_X = [50.68,53.42,53.8]
list_Y = [48.7, 45.86, 51.72]
list_W = [0.93,0.8,-0.32]

sendArr = []

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 402)
        self.task1 = QtWidgets.QPushButton(Form)
        self.task1.setGeometry(QtCore.QRect(170, 30, 80, 25))
        self.task1.setObjectName("task1")
        self.task1.clicked.connect(self.onClick1)
        self.task2 = QtWidgets.QPushButton(Form)
        self.task2.setGeometry(QtCore.QRect(170, 80, 80, 25))
        self.task2.setObjectName("task2")
        self.task2.clicked.connect(self.onClick2)
        self.task3 = QtWidgets.QPushButton(Form)
        self.task3.setGeometry(QtCore.QRect(170, 140, 80, 25))
        self.task3.setObjectName("task3")
        self.task3.clicked.connect(self.onClick3)
        self.task4 = QtWidgets.QPushButton(Form)
        self.task4.setGeometry(QtCore.QRect(170, 180, 80, 25))
        self.task4.setObjectName("task4")
        self.task5 = QtWidgets.QPushButton(Form)
        self.task5.setGeometry(QtCore.QRect(170, 230, 80, 25))
        self.task5.setObjectName("task5")
        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(170, 320, 80, 25))
        self.quit.setObjectName("quit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def onClick1(self) :
      self.movebase_client(list_X[0], list_Y[0], list_W[0])
    
    def onClick2(self) :
      self.movebase_client(list_X[1], list_Y[1], list_W[1])
    
    def onClick3(self) :
      self.movebase_client(list_X[2], list_Y[2], list_W[2])



    def movebase_client(self,x,y,w):

      # Create an action client called "move_base" with action definition file "MoveBaseAction"
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    
      # Waits until the action server has started up and started listening for goals.
#        client.wait_for_server()

      # Creates a new goal with the MoveBaseGoal constructor
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
      # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
        goal.target_pose.pose.position.x = x
      # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
        goal.target_pose.pose.position.y = y
      # No rotation of the mobile base frame w.r.t. map frame
        goal.target_pose.pose.orientation.w = w

      # Sends the goal to the action server.
        client.send_goal(goal)
      # Waits for the server to finish performing the action.
#        wait = client.wait_for_result()
      # If the result doesn't arrive, assume the Server is not available
 #       if not wait:
  #          rospy.logerr("Action server not available!")
   #         rospy.signal_shutdown("Action server not available!")
    #    else:
        # Result of executing the action
     #       return client.get_result()   

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.task1.setText(_translate("Form", "TASK1 "))
        self.task2.setText(_translate("Form", "TASK2"))
        self.task3.setText(_translate("Form", "TASK3"))
        self.task4.setText(_translate("Form", "TASK4"))
        self.task5.setText(_translate("Form", "TASK5"))
        self.quit.setText(_translate("Form", "EXIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    rospy.init_node('movebase_client_py')    
    Dialog.show()
    sys.exit(app.exec_())



