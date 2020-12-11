from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import sys, getopt

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "p:v:m",["program=","volume=", "mute"])
	except getopt.GetoptError:
		print("volume.py -p <program> [-v <volume change by> | -m]")
		sys.exit(2)

	program = ""
	volume = ""
	mute = False
	
	for opt, arg in opts:
		if opt in ("-p", "--program"):
			program = arg
		elif opt in ("-v", "--volume"):
			diffvol = arg
		elif opt in ("-m", "--mute"):
			mute = True

	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session._ctl.QueryInterface(ISimpleAudioVolume)
		if session.Process and program.lower() in session.Process.name().lower():
			if mute:
				if volume.GetMute() == 1:
					volume.SetMute(0, None)
				else:
					volume.SetMute(1, None)
			else:
				if volume.GetMasterVolume()+float(diffvol) > 1:
					diffvol = 1 - volume.GetMasterVolume()
				volume.SetMasterVolume(volume.GetMasterVolume()+float(diffvol), None)

if __name__ == "__main__":
	main(sys.argv[1:])