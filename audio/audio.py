import subprocess
import time
import os

def play_audio(audio):
	if not os.path.exists(audio):
		print("File not found")
	result = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",audio],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	print(result.stdout)
	duration = float(result.stdout)
	subprocess.run(["termux-media-player","play",audio])
	time.sleep(duration)
