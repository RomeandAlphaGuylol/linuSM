import os
import time
def unkown_distro():
	print("UKNOWN DISTRO")

def on_startup():
	print("""
	##              $$$$$$$$$       |\            /|
	##              $$$             |  \        /  |
	##              $$$             |    \    /    |
	##              $$$$$$$$$       |      \/      |
	##                    $$$       |              |
	##                    $$$       |              |
	############    $$$$$$$$$       |              |
	  
	  
	  """)

def quit_on_cmd():
	print("QuitOnCommand")
	quit()
class neofetch:
	def find(distro):
		if distro=="ubuntu":
			os.system("neofetch --ascii_distro ubuntu")
		elif distro=="kali":
			os.system("neofetch --ascii_distro kali")
		elif distro=="kernal":
			os.system("neofetch --ascii_distro kernal")
		elif distro=="arch":
			os.system("neofetch")
neo_args_distro_ubuntu = "-D ubuntu"
neo_args_distro_kali = "-D kali"
neo_args_kernal = "-D kernal"
on_startup()
while True:
	linusm = input("linusm >>> ")
	if linusm=="neofh "+neo_args_distro_ubuntu:
		neofetch.find("ubuntu")
	elif linusm=="neofh "+neo_args_distro_kali:
		neofetch.find("kali")
	elif linusm=="neofh "+neo_args_kernal:
		neofetch.find("kernal")
	elif linusm=="exit()":
		quit_on_cmd()
	elif linusm=="neofh "+"-D chrome":
		try:
			neofetch.find("chrome")
		except:
			neofetch.find("chromeOS")
	elif linusm=="neofh "+"-D steam":
		try:
			neofetch.find("steam")
		except:
			neofetch.find("steamOS")
	elif linusm=="neofh "+"-D windows10":
		neofetch("windows10")
	elif linusm=="neofh "+"-D windows7":
		try:
			neofetch.find("windows7")
		except:
			neofetch("windows")
	elif linusm=="neofh --redirectOS ubuntu => kali":
		os.system("clear")
		print("Linusm >>> neofh -D ubuntu")
		time.sleep(1)
		neofetch.neofetch("kali")
	elif linusm=="neofh --changefechOS -Or ubuntu => kali":
		os.system("clear")
		print("Linusm >>> neofetch --ascii_distro ubuntu")
		time.sleep(1)
		neofetch("kali")
	elif linusm=="disp()":
		disp = input("disp: ")
		os.system("echo "+disp)
	elif linusm=="clear --startuplogo":
		os.system("clear")
		on_startup()
	elif linusm=="clear":
		os.system("clear")
	elif linusm=="cls":
		os.system("clear")
	elif linusm=="neofh -D arch":
		neofetch.find("arch")
	else:
		print(" ")
		print("Unkown Command Try again")
		print(" ")
		print(" ")
