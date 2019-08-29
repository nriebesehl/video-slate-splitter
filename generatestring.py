import os
import os.path
import sys
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('vid')
parser.add_argument('trt')
args = parser.parse_args()

vidfilename = os.path.split(args.vid)
newfilename = (vidfilename[1].split(".")[0])

with open('tindex.temp', 'r') as f:
	cmdlist = open('cmds.temp', 'w+')
	lineList = [line.rstrip('\n') for line in f]
	data = []
	for r in range(len(lineList)-2):
		data.append(lineList[r+2][2:].split(" "))
	for q in range(len(data)):
		if q == (len(data)-1):
			startime = (data[q][1].split(':')[1])
			duration = round((float(args.trt) - float(data[q][1].split(':')[1])), 3)
		else:
			startime = (data[q][1].split(':')[1])
			duration = round((float(data[q+1][0].split(':')[1]) - float(data[q][1].split(':')[1])), 3)
#		print(q)
		name = (newfilename + "_" + str(q) + ".mp4")
		arguments = ("ffmpeg -i " + args.vid + " -ss " + str(startime) + " -t " + str(duration) + " -c:v libx264 -pix_fmt yuv420p -b:v 10M -minrate 10M -maxrate 10M -bufsize 20M -preset fast -crf 21 -c:a aac -b:a 320k " + name)
		cmdlist.write(arguments+" \n")
	cmdlist.close()
