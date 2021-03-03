height=float(input("Enter Height in Centimeters: "))
weight=float(input("Enter Weight in Kilograms: "))
height = height/100
BMI=weight/(height*height)
print("Body Mass Index (BMI) is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")
