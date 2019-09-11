#!/usr/bin/python

#A BMI calculator to demonstrate the use of functions in Python#

def gather_info():
	height=float(raw_input("Your height in inches or metres: "))
	weight=float(raw_input("Your weight in pounds or kilograms: "))
	unit=raw_input("Metric system metric or imperial: ").lower().strip()
	return(height,weight,unit)

def calculate_bmi(weight, height,unit='metric'):	# Arguments to function and set default value for unit
	if unit == 'metric':
		bmi = (weight / (height ** 2))
	else: 
		bmi = 703 * (weight / (height ** 2))
	print ("BMI is %s" % bmi)

while True:
	height,weight,unit=gather_info()
	if unit.startswith('i'):
		calculate_bmi(weight,unit='imperial',height=height)	#provide parameters to function#
		break
	
	elif unit.startswith('m'):
		calculate_bmi(weight,height)	#default value of unit will be ued#
		break
	else:
		print "Unknown measurement system"
