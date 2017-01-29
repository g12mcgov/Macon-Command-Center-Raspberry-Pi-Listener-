#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
# @Author: grantmcgovern
# @Date:   2015-09-07 00:27:57
# @Email:   me@grantmcgovern.com
# @Web:    http://grantmcgovern.com
#
# @Last Modified by:   Grant McGovern
# @Last Modified time: 2016-02-25 21:06:41

from Adafruit_MotorHAT import (
	Adafruit_MotorHAT,
	Adafruit_DCMotor, 
	Adafruit_StepperMotor
	)

import time
import atexit

class Blinds(object):
	def __init__(self):
		# create a default object, no changes to I2C address or frequency
		self.mh = Adafruit_MotorHAT()
		atexit.register(self.turnOffMotors)
		# 200 steps/rev, motor port #1
		self.side_blinds = self.mh.getStepper(200, 1)
		# 30 RPM
		self.side_blinds.setSpeed(30)

	# recommended for auto-disabling motors on shutdown!
	def turnOffMotors(self):
		self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
		self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

	def backward(self, motor):
		motor.step(86, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)

	def forward(self, motor):
		motor.step(86, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)

	def adjust_forward(self, motor):
		motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)

	def adjust_backward(self, motor):
		motor.step(5, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)