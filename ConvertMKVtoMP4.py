import os
import subprocess
import glob

files = glob.glob('*.mkv')

for i in files:
	name = i.split('.')[0]
	print(name)
	subprocess.call(['ffmpeg', '-i', name + '.mkv', '-strict',' -2', '-codec', 'copy', name + '.mp4'])
