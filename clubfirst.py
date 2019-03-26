# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draft1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class Ui_Form(object):


    def initializeClients (self):
        self.client1 = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.client2 = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.client3 = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.client4 = actionlib.SimpleActionClient('move_base',MoveBaseAction)                

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(400, 449)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.table1 = QtWidgets.QPushButton(Form)
        self.table1.setGeometry(QtCore.QRect(150, 110, 80, 25))
        self.table1.setObjectName("table1")
        self.table1.clicked.connect(self.onClickTable1)
        self.table2 = QtWidgets.QPushButton(Form)
        self.table2.setGeometry(QtCore.QRect(150, 150, 80, 25))
        self.table2.setObjectName("table2")
        self.table2.clicked.connect(self.onClickTable2)
        self.table12 = QtWidgets.QPushButton(Form)
        self.table12.setGeometry(QtCore.QRect(150, 190, 80, 25))
        self.table12.setObjectName("table12")
        self.table12.clicked.connect(self.onClickTable12)
        self.table21 = QtWidgets.QPushButton(Form)
        self.table21.setGeometry(QtCore.QRect(150, 230, 80, 25))
        self.table21.setObjectName("table21")
        self.table21.clicked.connect(self.onClickTable21)
        self.table22 = QtWidgets.QPushButton(Form)
        self.table22.setGeometry(QtCore.QRect(150, 270, 80, 25))
        self.table22.setObjectName("table22")
        self.table22.clicked.connect(self.onClickTable22)
        self.table11 = QtWidgets.QPushButton(Form)
        self.table11.setGeometry(QtCore.QRect(150, 310, 80, 25))
        self.table11.setObjectName("table11")
        self.table11.clicked.connect(self.onClickTable11)
        self.home = QtWidgets.QPushButton(Form)
        self.home.setGeometry(QtCore.QRect(150, 350, 80, 25))
        self.home.setObjectName("home")
        # self.home.clicked.connect(self.onClickTableHome)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(150, 50, 72, 25))
        self.comboBox.setSizeIncrement(QtCore.QSize(0, 3))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CLUB FIRST"))
        self.table1.setText(_translate("Form", "TABLE 1"))
        self.table2.setText(_translate("Form", "TABLE 2"))
        self.table12.setText(_translate("Form", "TABLE 12"))
        self.table21.setText(_translate("Form", "TABLE 21"))
        self.table22.setText(_translate("Form", "TABLE 22"))
        self.table11.setText(_translate("Form", "TABLE 11"))
        self.home.setText(_translate("Form", "HOME"))
        self.comboBox.setItemText(0, _translate("Form", "1"))
        self.comboBox.setItemText(1, _translate("Form", "2"))
        self.comboBox.setItemText(2, _translate("Form", "3"))
        self.comboBox.setItemText(3, _translate("Form", "4"))


    def onClickTable1(self) :
      if self.comboBox.currentText() == "1" :
        self.movebase_client(48.77, 50.06, 0.66,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(48.77, 50.06, 0.66,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(48.77, 50.06, 0.66,3)                
      else :
        self.movebase_client(48.77, 50.06, 0.66,4)

    def onClickTable2(self) :

      if self.comboBox.currentText() == "1" :
        self.movebase_client(49.52, 51.44, -0.101,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(49.52, 51.44, -0.101,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(49.52, 51.44, -0.101,3)               
      else :
        self.movebase_client(49.52, 51.44, -0.101,4)

      # self.movebase_client(49.52, 51.44, -0.101)
    
    def onClickTable12(self) :
      if self.comboBox.currentText() == "1" :
        self.movebase_client(53.72, 48.09, 0.673,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(53.72, 48.09, 0.673,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(53.72, 48.09, 0.673,3)               
      else :
        self.movebase_client(53.72, 48.09, 0.673,4)
      

    def onClickTable21(self) :
      if self.comboBox.currentText() == "1" :
        self.movebase_client(87.636, 46.83, 0.699,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(87.636, 46.83, 0.699,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(87.636, 46.83, 0.699,3)               
      else :
        self.movebase_client(87.636, 46.83, 0.699,4)
      

    def onClickTable22(self) :
      if self.comboBox.currentText() == "1" :
        self.movebase_client(57.40, 53.19, 0.65,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(57.40, 53.19, 0.65,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(57.40, 53.19, 0.65,3)               
      else :
        self.movebase_client(57.40, 53.19, 0.65,4)      

    def onClickTable11(self) :
      if self.comboBox.currentText() == "1" :
        self.movebase_client(48.60, 47.66, -0.102,1)
      elif self.comboBox.currentText() == "2" :
        self.movebase_client(48.60, 47.66, -0.102,2)
      elif self.comboBox.currentText() == "3" :
        self.movebase_client(48.60, 47.66, -0.102,3)               
      else :
        self.movebase_client(48.60, 47.66, -0.102,4)         

    # def onClickTableHome(self) :
    #   self.movebase_client()

    def movebase_client(self,x,y,w, client_no):
      print("details are",x,y,w,client_no)
      # Create an action client called "move_base" with action definition file "MoveBaseAction"
        # client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    
      # Waits until the action server has started up and started listening for goals.
#        client.wait_for_server()

      # # Creates a new goal with the MoveBaseGoal constructor
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
        if client_no ==1 :
          self.client1.send_goal(goal)
        elif client_no == 2:
          self.client2.send_goal(goal)
        elif client_no ==3:
          self.client3.send_goal(goal)
        else :
          self.client4.send_goal(goal)

        # client.send_goal(goal)
      # Waits for the server to finish performing the action.
#        wait = client.wait_for_result()
      # If the result doesn't arrive, assume the Server is not available
 #       if not wait:
  #          rospy.logerr("Action server not available!")
   #         rospy.signal_shutdown("Action server not available!")
    #    else:
        # Result of executing the action
     #       return client.get_result()   





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    ui.initializeClients()
    rospy.init_node('movebase_client_py')    
    Dialog.show()
    sys.exit(app.exec_())

