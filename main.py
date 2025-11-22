import json
import subprocess
import time
from audio.audio import play_audio
from app_explorer.app import *

def run_cmd(cmd):
	r = subprocess.run(cmd,shell=True,capture_output=True,text=True)
	if r.returncode != 0:
		raise RuntimeError(f"Command Failed: {r.stderr.strip()}")
	return r.stdout

def text_to_speech(text):
	try:
		r = subprocess.run(["termux-tts-speak",text])
		duration = max(1, len(text) / 13)
		time.sleep(duration)
	except FileNotFoundError:
		print("For some reason, I have to check if the Termux API is installed")

def notification_handler(title,content):
	r = subprocess.run(["termux-notification","--title",title,"--content",content],capture_output=True,text=True)
	if r.returncode != 0:
		raise RuntimeError(f"Command Notification Failed: {r.stderr.strip()}")
	return r.stdout

def battery_manager(battery_data):
	battery_percent = battery_data.get("percentage")
	battery_status = battery_data.get("status")
	text_to_speech("Coolerpuutt has a notification")
	if battery_status != "CHARGING":
		match battery_percent:
			case 20:
				notification_handler("Low Battery","You need to charge your phone bruh")
			case 50:
				notification_handler("Mid-Alive Battery","Cool but not cool enough")
			case 100:
				notification_handler("Battery Full!","Your Battery it's at full capacity")
	else:
		notification_handler("Phone Charging","We charging here!")
		spoken_text = (
    f"Health is {battery_data['health']}. "
    f"Power source: {battery_data['plugged'].replace('PLUGGED_', '').lower()}. "
    f"Temperature is {battery_data['temperature']} degrees Celsius. "
    f"Charging current is {battery_data['current'] / 1000000:.2f} amperes."
)
		text_to_speech(spoken_text)

battery = run_cmd("termux-battery-status")
battery_data = json.loads(battery)
#output = subprocess.check_output(["dumpsys", "usagestats"]).decode()
#print(output)
#battery_manager(battery_data)
# print("Battery Percentage: ",data.get("percentage"))

#play_audio("./audio/sounds/myPrincess.mp3")
#open_chrome()
open_chess()
