#!/usr/bin/python
import subprocess
import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.geometry("200x500+200+200") 


def oceanFadeSequence():

	blueToCyan=["#0000FF","#0017FF","#002EFF","#0046FF","#005DFF","#0074FF","#008BFF","#00A2FF","#00B9FF","#00D1FF","#00E8FF","#00F6FF"]

	var=0


 	x = 0
 	i = 0

	for i in range(0,10):
		while x < len(blueToCyan):
			#var = "#0000FF"
			subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[var]])
			var+=1
			x+=1

def sunsetFadeSequence():

	yellowToOrange=["#FFFF99","#FFF18B","#FFE37D","#FFD56F","#FFC761","#FFB953","#FFAC46","#FF9E38","#FF902A","#FF821C","#FF740E","#FF6600"]

	var=0


 	x = 0
 	i = 0

	for i in range(0,10):
		while x < len(yellowToOrange):
			#var = "#0000FF"
			subprocess.call(["tplight", "hex", "192.168.2.2", yellowToOrange[var]])
			var+=1
			x+=1
def xmasFadeSequence():

	greenToRed=["#00FF00","#17E800","#2ED100","#46B900","#5DA200","#748B00","#8B7400","#A25D00","#B94600","#D12E00","#E81700","#FF0000"]

	var=0


 	x = 0
 	i = 0

	for i in range(0,10):
		while x < len(greenToRed):
			#var = "#0000FF"
			subprocess.call(["tplight", "hex", "192.168.2.2", greenToRed[var]])
			var+=1
			x+=1

def rainbowFadeSequence():

	rainbow=["#9400D3","#4b0082","#0000FF","#00FF00","#FFFF00","#FF7F00","#FF0000"]
	
	global counter
	value = 2
	var=0
 	x = 0
 	i = 0

	#while(counter != inputvar):
	#for i in range(0,10):
	while x < len(rainbow):
		#var = "#0000FF"
		subprocess.call(["tplight", "hex", "192.168.2.2", rainbow[var]])
		var+=1
		x+=1
	counter+=1	

	if(counter != inputvar):
		rainbowFadeSequence()



def flashFadeSequence():

	blueToCyan=["#0000FF","#0017FF","#002EFF","#0046FF","#005DFF","#0074FF","#008BFF","#00A2FF","#00B9FF","#00D1FF","#00E8FF","#00F6FF"]

	var=0


 	x = 0
 	i = 0

	for i in range(0,10):
		while x < len(blueToCyan):
			#var = "#0000FF"
			subprocess.call(["tplight", "on", "192.168.2.2", blueToCyan[var]])
			subprocess.call(["tplight", "off", "192.168.2.2", blueToCyan[var]])
			var+=1
			x+=1


oceanFade = Tkinter.Button(top, text ="Ocean Fade", command = oceanFadeSequence)
sunsetFade = Tkinter.Button(top, text ="Sunset Fade", command = sunsetFadeSequence)
xmasFade = Tkinter.Button(top, text ="Christmas Fade", command = xmasFadeSequence)
rainbowFade = Tkinter.Button(top, text ="Rainbow Fade", command = rainbowFadeSequence)
endicottFade = Tkinter.Button(top, text ="Endicott Fade", command = flashFadeSequence)



oceanFade.pack()
sunsetFade.pack()
xmasFade.pack()
rainbowFade.pack()
endicottFade.pack()
top.mainloop()