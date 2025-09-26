import json
import subprocess

def run_cmd(cmd):
	r = subprocess.run(cmd,shell=True,capture_output=True,text=True)
	if r.returncode != 0:
		raise RuntimeError(f"Command Failed: {r.stderr.strip()}")
	return r.stdout

def text_to_speech(text):
	try:
		r = subprocess.run(["termux-tts-speak",text])
	except FileNotFoundError:
		print("For some reason, I have to check if the Termux API is installed")

def notification_handler(title,content):
	r = subprocess.run(["termux-notification","--title",title,"--content",content])
	if r.returncode != 0:
		raise RuntimeError(f"Command Notification Failed: {r.stderr.strip()}")
	return r.stdout

def battery_manager(battery_data):
	battery_percent = battery_data.get("percentage")
	battery_status = battery_data.get("status")
	if battery_status != "CHARGING":
		if battery_percent < 15:
			print("Please plug your phone as it is very low")
		elif battery_percent > 15 and battery_percent < 75:
			print("Still surviving")
		elif battery_percent > 75 and battery_percent <= 100:
			print("Nice Battery you have there")
	else:
		notification_handler("Phone Charging","We charging here!")
		text_to_speech("You have a notification")

battery = run_cmd("termux-battery-status")
battery_data = json.loads(battery)
battery_manager(battery_data)
# print("Battery Percentage: ",data.get("percentage"))
