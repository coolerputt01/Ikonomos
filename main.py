import json
import subprocess

def run_cmd(cmd):
	r = subprocess.run(cmd,shell=True,capture_output=True,text=True)
	if r.returncode != 0:
		raise RuntimeError(f"Command Failed: {r.stderr.strip()}")
	return r.stdout

out = run_cmd("termux-battery-status")
data = json.loads(out)
print("Battery Percentage: ",data.get("percentage"))
