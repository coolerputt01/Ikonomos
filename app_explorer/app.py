import os
import time

def open_chrome():
	print("Opening Chrome....\n")
	time.sleep(5)
	os.system("am start -a android.intent.action.VIEW -d https://google.com")


def open_x():
	print("Opening X...\n")
	time.sleep(3)
	os.system("am start -n com.twitter.android/.StartActivity")

def open_whatsapp():
	print("Opening Whatsapp...\n")
	time.sleep(5)
	os.system("am start -n com.whatsapp/.Main")

def open_freefire():
	print("Opening Freefire...\n")
	time.sleep(5)
	os.system("am start -n com.dts.freefireth/.FFMainActivity")


def open_chatgpt():
	print("Opening ChatGPT...\n")
	time.sleep(5)
	os.system("am start -n com.openai.chatgpt/.MainActivity")

def open_chess():
	print("Opening Chess App...\n")
	time.sleep(5)
	os.system("am start -n com.chess/.activities.SplashActivity")
