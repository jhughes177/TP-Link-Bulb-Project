import subprocess

blueToCyan=["#0000FF","#0017FF","#002EFF","#0046FF","#005DFF","#0074FF","#008BFF","#00A2FF","#00B9FF","#00D1FF","#00E8FF","#00F6FF"]

var=0


x = 0
i = 0
j = 0
y = 0

for i in range(0,10):
	while x < len(blueToCyan):
		#var = "#0000FF"
		subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[var]])
		var+=1
		x+=1

for j in xrange(10,0,-1):
	while y < len(blueToCyan):
		subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[var]])
		var+=1
		y+=1


	#var = "#0017FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[1]])
	#var = "#002EFF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[2]])
	#var = "#0046FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[3]])
	#var = "#005DFF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[4]])
	#var = "#0074FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[5]])
	#var = "#008BFF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[6]])
	#var = "#00A2FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[7]])
	#var = "#00B9FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[8]])
	#var = "#00D1FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[9]])
	#var = "#00E8FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[10]])
	#var = "#00F6FF"
	#subprocess.call(["tplight", "hex", "192.168.2.2", blueToCyan[11]])





