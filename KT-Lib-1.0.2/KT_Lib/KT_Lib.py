#
# KIPR's Masked Control Library to interface with the DJI Tello EDU
# For Use with the KIPR Autonomous Aerial Challenge Program and Curriculum
# http://www.kipr.org
#
# 6/24/2019

import threading
import socket
import sys
import time

#Set up connection to the drone.
#host = ''
#port = 9000
#locaddr = (host,port)

#Init code made from help with DJI's Tello3.py Demo Program on GitHub
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ("192.168.10.1", 8889)
locaddr = ('',8889)
sock.bind(locaddr)

def recv():
	count = 0
	while True:
		try:
			data, server = sock.recvfrom(1518)
			print(data.decode(encoding="utf-8"))
		except Exception:
			print ('\nExit.\n')
			break

#recvThread create
#recvThread = threading.Thread(target=recv)
#recvThread.start()

class Tello:
	
	#Begin Masked Controls for Tello EDU SDK2.0
	#Sends the "command" command to Tello EDU Drone
	def connect(self):
		sock.sendto("command".encode(encoding="utf-8"), tello_address)
	
	#Sends the "command" command to Tello EDU Drone
	def disconnect(self):
		sock.close()
		sys.exit()
	
	#Sends the "takeoff" command to Tello EDU Drone
	def takeoff(self):
		sock.sendto("takeoff".encode(encoding="utf-8"), tello_address)
	
	#Sends the "land" command to Tello EDU Drone
	def land(self):
		sock.sendto("land".encode(encoding="utf-8"), tello_address)
	
	#Sends the "stop" command to Tello EDU Drone
	def stop(self):
		sock.sendto("stop".encode(encoding="utf-8"), tello_address)
	
	#Sends the "emergency" command to Tello EDU Drone
	def emergency(self):
		sock.sendto("emergency".encode(encoding="utf-8"), tello_address)
	
	#Sends the "streamon" command to Tello EDU Drone
	def streamon(self):
		sock.sendto("streamon".encode(encoding="utf-8"), tello_address)
	
	#Sends the "streamoff" command to Tello EDU Drone
	def streamoff(self):
		sock.sendto("streamoff".encode(encoding="utf-8"), tello_address)
	
	#Sends the "mon" command to Tello EDU Drone
	def mon(self):
		sock.sendto("mon".encode(encoding="utf-8"), tello_address)
	
	#Sends the "moff" command to Tello EDU Drone
	def moff(self):
		sock.sendto("moff".encode(encoding="utf-8"), tello_address)
	
	#Sends the "up x" command to Tello EDU Drone with a default distanc of 50cm
	def up(self, cm = "50"):
		cmd = "up " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "down x" command to Tello EDU Drone with a default distanc of 50cm
	def down(self, cm = "50"):
		cmd = "down " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "left x" command to Tello EDU Drone with a default distanc of 50cm
	def left(self, cm = "50"):
		cmd = "left " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "right x" command to Tello EDU Drone with a default distanc of 50cm
	def right(self, cm = "50"):
		cmd = "right " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "forward x" command to Tello EDU Drone with a default distanc of 50cm
	def forward(self, cm = "50"):
		cmd = "forward " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "back x" command to Tello EDU Drone with a default distanc of 50cm
	def back(self, cm = "50"):
		cmd = "back " + cm
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "cw x" command to Tello EDU Drone with a default degree of 90
	def cw(self, degrees = "90"):
		cmd = "cw " + degrees
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "ccw x" command to Tello EDU Drone with a default degree of 90
	def ccw(self, degrees = "90"):
		cmd = "ccw " + degrees
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "curve x1 y1 z1 x2 y2 z2 speed" command to Tello EDU Drone with a default degree of 90
	def curve(self, x1 = "30", y1 = "30", z1 = "30", x2 = "30", y2 = "30", z2 = "30", speed = "20"):
		cmd = "curve " + x1 + " " + y1 + " " + z1 + " " + x2 + " " + y2 + " " + z2 + " " + speed
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "flip x" command to Tello EDU Drone with a default direction of forward
	def flip(self, direction = "f"):
		cmd = "flip " + direction
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "speed x" command to Tello EDU Drone with a default distanc of 20cm/s
	def speed(self, cm_s = "20"):
		cmd = "speed " + direction
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "speed?" command to Tello EDU Drone
	def get_speed(self):
		sock.sendto("speed?".encode(encoding="utf-8"), tello_address)
	
	#Sends the "battery?" command to Tello EDU Drone
	def get_battery(self):
		sock.sendto("battery?".encode(encoding="utf-8"), tello_address)
	
	#Sends the "time?" command to Tello EDU Drone
	def get_time(self):
		sock.sendto("time?".encode(encoding="utf-8"), tello_address)
	
	#Sends the "wifi?" command to Tello EDU Drone
	def get_wifi(self):
		sock.sendto("wifi?".encode(encoding="utf-8"), tello_address)
	
	#Sends the "wifi ssid pass" command to Tello EDU Drone
	def wifi_ssid_pass(self, ssid, password):
		cmd = "wifi " + ssid + " " + password
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
	
	#Sends the "go x y z spped" command to Tello EDU Drone
	def go(self, x, y, z, speed):
		cmd = "go " + x + " " + y + " " + z + " " + speed
		sock.sendto(cmd.encode(encoding="utf-8"), tello_address)
