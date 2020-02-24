import os
with open("archive.mp4","wb") as output:
	for filename in os.listdir():
		
		if filename[-1] != 'y' and filename != 'archive.mp4':
			print(filename)
			file = open(filename,"rb")
			data = file.read()
			output.write(data)