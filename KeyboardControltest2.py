#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi

#global key			

class GoForward(): #we use this function to go move in a straigh line
	def __init__(self,ncases,direction):
		# initiliaze
		linear_speed = 0.2

		global goal_centimeters #here the distance to go
		#rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + ctrl
		#rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
	# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);
	
		# Twist is a datatype for velocity
		move_cmd = Twist()
	# let's go forward at 0.2 m/s

		if direction==0: #said if you go forward or backward
			move_cmd.linear.x = linear_speed
		if direction==1:
			move_cmd.linear.x = -linear_speed

	# let's turn at 0 radians/s
			move_cmd.angular.z = 0


		rate=10
	   # global goal_centimeters=2.5
	
		ticks = int(ncases*2.5*8/7*rate) # the 2.5*8/7 is a to adapt the distance to each title

		for t in range(ticks): #loop moving the robot until the current postion

			self.cmd_vel.publish(move_cmd)

			r.sleep() 

			
	#def shutdown(self):
		# stop turtlebot
	 #   rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
	  ##  self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
			#rospy.sleep(1)	
				 
			
class Turn():
	def __init__(self, direction):
		# initiliaze
		rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
		# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
	# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
	# let's turn at 0 radians/s
	
		if direction==0:
			move_cmd.angular.z = 1
		if direction==1:
			move_cmd.angular.z = -1

		rate=10
		goal_angle=1*pi
	
		ticks = int(goal_angle * rate)

		#time.sleep(1) 
		for t in range(ticks): #loop turning the robot until the current postion


			self.cmd_vel.publish(move_cmd)

			r.sleep()
			
	def shutdown(self):
		# stop turtlebot
		#rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		#rospy.sleep(1)		
			

class Diagonal():
	def __init__(self,direction):
		# initiliaze
		rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
		# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
	# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
	# let's turn at 0 radians/s
		if direction==1 :
			move_cmd.angular.z = -1.0
		if direction==0 :
			move_cmd.angular.z = 1.0
	
		rate=10
		goal_angle=0.5*pi
		

		ticks = int(goal_angle * rate)

		for t in range(ticks):

			self.cmd_vel.publish(move_cmd)

			r.sleep()
			
	def shutdown(self):
		# stop turtlebot
		#rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		#rospy.sleep(1)		

class Diagonal2():
	def __init__(self,direction):
		# initiliaze
		rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
		# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
	# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
	# let's turn at 0 radians/s
		if direction==1 :
			move_cmd.angular.z = -1.0
		if direction==0 :
			move_cmd.angular.z = 1.0
	
		rate=10
		goal_angle=0.4*pi
		

		ticks = int(goal_angle * rate)

		for t in range(ticks):

			self.cmd_vel.publish(move_cmd)

			r.sleep()
			
	def shutdown(self):
		# stop turtlebot
		#rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		#rospy.sleep(1)		

class Secondturn():
	def __init__(self,direction):
		# initiliaze
		rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
		# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
	# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
	# let's turn at 0 radians/s
		if direction==1 :
			move_cmd.angular.z = -1.0
		if direction==0 :
			move_cmd.angular.z = 1.0
	
		rate=10
		goal_angle=0.75*pi
		

		ticks = int(goal_angle * rate)

		for t in range(ticks):

			self.cmd_vel.publish(move_cmd)

			r.sleep()
			
	def shutdown(self):
		# stop turtlebot
		#rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		#rospy.sleep(1)		

class Thirdturn():
	def __init__(self,direction):
		# initiliaze
		rospy.init_node('Chess_Move', anonymous=False)

	# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

		# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
		
	# Create a publisher which can "talk" to TurtleBot and tell it to move
		# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
	 
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
	# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
	# let's turn at 0 radians/s
		if direction==1 :
			move_cmd.angular.z = -1.0
		if direction==0 :
			move_cmd.angular.z = 1.0
	
		rate=10
		goal_angle=0.65*pi
		

		ticks = int(goal_angle * rate)

		for t in range(ticks):

			self.cmd_vel.publish(move_cmd)

			r.sleep()
			
	def shutdown(self):
		# stop turtlebot
		#rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		#rospy.sleep(1)		

class Stop():
	def __init__(self):
		# initiliaze
		#rospy.init_node('Chess_Move', anonymous=False)

		# tell user how to stop TurtleBot
		rospy.loginfo("To stop TurtleBot CTRL + C")

			# What function to call when you ctrl + c	
		rospy.on_shutdown(self.shutdown)
			
		# Create a publisher which can "talk" to TurtleBot and tell it to move
			# Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
		self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
		 
		#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
		r = rospy.Rate(10);

		move_cmd = Twist()
		# let's go forward at 0.2 m/s
		move_cmd.linear.x = 0
		# let's turn at 0 radians/s
		move_cmd.angular.z = 0
		rate=10
		
		
	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Chess_Move")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		rospy.sleep(1)
#############################################################################################################


class Tower(): #loop waiting for the input
	def __init__(self):
		# initiliaze
		
		global key
 		key=input("Tower Direction: ")
	
		if not key==0:
			dist=input("Tower Distance: ")
		
	 		try:
			
				
				if key == 8:
					GoForward(dist,0)
					Tower()
				if key == 2: 
					GoForward(dist,1)
					Tower()
				if key == 4:	 
	 				Turn(0)
					GoForward(dist,0)
					Diagonal(1)
					Tower() 
				if key == 6:
	 				Turn(1)
					GoForward(dist,0)
					Diagonal(0)#diagonal because in this case the turn function turn too much
					Tower() #go back to listen
				if key == 0:	 
					Listen()

			except:
			 	rospy.loginfo(key)

class Queen():
	def __init__(self):
		# initiliaze
		global key
 		key=input("Queen Direction: ")
	
		if not key==0:
			dist=input("Queen Distance: ")

	 		try :
				if key == 8:
					GoForward(dist,0)
					Queen()
				if key == 2: 
					GoForward(dist,1)
					Queen()
				if key == 4:	 
	 					Turn(0)
						GoForward(dist,0)
						Diagonal(1)
						Queen() 
				if key == 6:	
	 				Turn(1)
					GoForward(dist,0)
					Diagonal(0)
					Queen() 
				if key == 1:
					Diagonal(1)
					GoForward(dist*1.4142,1)
					Diagonal(0)
					Queen()	
				if key == 3:
					Diagonal(0)
					GoForward(dist*1.4142,1)
					Diagonal(1)
					Queen()	
				if key == 7:
					Diagonal(0)
					GoForward(dist*1.4142,0)
					Diagonal(1)
					Queen()	
				if key == 9:
					Diagonal(1)
					GoForward(dist*1.4142,0)
					Diagonal(0)
					Queen()	
				if key == 0:	 
					Listen()
			

			except:
				rospy.loginfo(key)

class King():
	def __init__(self):
		# initiliaze
		global key
		key=input("King Direction: ")
		
		if not key==0:
	
			try:
			
				
				if key == 8:
					GoForward(1,0)
					King()
				if key == 2: 
					GoForward(1,1)
					King()
				if key == 4:	 
					Turn(0)
					GoForward(1,0)
					Diagonal(1)
					King() 
				if key == 6:	
					Turn(1)
					GoForward(1,0)
					Diagonal(0)
					King() 
				if key == 1:
					Diagonal(1)
					GoForward(1.4142,1)
					Diagonal(0)
					King()	
				if key == 3:
					Diagonal(0)
					GoForward(1.4142,1)
					Diagonal(1)
					King()	
				if key == 7:
					Diagonal(0)
					GoForward(1.4142,0)
					Diagonal(1)
					King()	
				if key == 9:
					Diagonal(1)
					GoForward(1.4142,0)
					Diagonal(0)
					King()	
				if key == 0:	 
					Listen()
			

			except:
				rospy.loginfo(key)


class Pawn():
	def __init__(self):
		# initiliaze
		global key
		key=input("Pawn Direction: ")
		
		if not key==0 :
			dist=1
		
			try:
			
				if key == 'Start 2':
					GoForward(dist*2,0)
					Pawn()
				if key == 8:
					GoForward(dist,0)
					Pawn()
				if key == 'Eat 7':
					Diagonal(0)
					GoForward(1.4142,0)
					Diagonal(1)
					Pawn()	
				if key == 'Eat 9':
					Diagonal(1)
					GoForward(1.4142,0)
					Diagonal(0)
					Pawn()	
				if key == 0:	 
					Listen()
			

			except:
				rospy.loginfo(key)

class Shutdown():
	
	def __init__(self):
		rospy.on_shutdown(self.shutdown)
	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Chess_Move")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		rospy.sleep(1)

class Bishop():
	def __init__(self):
		# initiliaze
		global key
		key=input("Bishop Direction: ")
	
		if not key==0:
			dist=input("Bishop Distance: ")
		
			try:
			
				if key == 9:
					GoForward(dist,0)
					Bishop()
				if key == 1: 
					GoForward(dist,1)
					Bishop()
				if key == 7:	 
					Turn(0)
					GoForward(dist,0)
					Diagonal(1)
					Bishop() 
				if key == 3:	
					Turn(1)
					GoForward(dist,0)
					Diagonal(0)
					Bishop() 
				if key == 0:
					Diagonal(0)	 
					Listen()	

			except:
				rospy.loginfo(key)

class Horseman():
	def __init__(self):
		# initiliaze
		global direction1
		global direction2
		direction1=input("first movement : ")
		
		if not direction1==0:
				direction2=input("second movement : ")

				if direction1<0:
					direction1=direction1*-1
					dist=1
				else:	 
					dist=2

				try:
					if direction1 == 8 :
						GoForward(dist,0)

					if direction1 == 2:
						GoForward(dist,1)

					if direction1 == 4:
						Turn(0)
						GoForward(dist,0)
						Diagonal(1)

					if direction1 == 6:	
						Turn(1)
						GoForward(dist,0)
						Diagonal(0)

					if direction1 == 0:	 
						Listen()
				
					if dist==1:
						dist=2
					else:	 
						dist=1
									
					if direction2 == 8:
						GoForward(dist,0)
					
					if direction2 == 2: 
						GoForward(dist,1)
					
					if direction2 == 4:	 
						Secondturn(0)
						GoForward(dist,0)
						Thirdturn(1)
					
					if direction2 == 6:	
						Secondturn(1)
						GoForward(dist,0)
						Secondturn(0)
					
					Horseman() 
				except:
					rospy.loginfo(direction1)
							 		

class Shutdown():
	
	def __init__(self):
		rospy.on_shutdown(self.shutdown)
	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Chess_Move")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		rospy.sleep(1)


#####################################################################################################################################
class Listen(): #function launch at the beginning at programm launch
	def __init__(self):
		# initiliaze
		#global key
		if not rospy.is_shutdown():
			key=input("Piece: ") #ask for the user input
	
			try:
			
					if key == 'Queen':	 
						Queen()
						Listen()
					if key == 'King':
						King()	 
						Listen()
					if key == 'Pawn':
						Pawn() 
						Listen()
					if key == 'Bishop':	 
						Diagonal(1)				
						Bishop()
						Diagonal(0)
						Listen()
					if key=='Tower':
						Tower()
						Listen()
					if key=='Horseman':
						Horseman()
						Listen()
			except:
				rospy.loginfo(key)

class Shutdown():
	
	def __init__(self):
		rospy.on_shutdown(self.shutdown)
	def shutdown(self):
		# stop turtlebot
		rospy.loginfo("Chess_Move")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
		self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
		rospy.sleep(1)

while not rospy.is_shutdown():

	if __name__ == '__main__':
		rospy.init_node('Chess_Move', anonymous=False)
		Listen()
		
