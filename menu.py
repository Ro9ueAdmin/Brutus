from initialize import initialize
from help import help
import os
from ssh_brute import ssh_brute
def menu():
	initialize()
	while 1:
		usr_inp=raw_input("brutus>")

		if usr_inp=="":
			usr_inp=raw_input("brutus>")

		elif usr_inp=="quit" or usr_inp=="exit":
			quit()

		elif usr_inp=="help":
			print("\n")
			help()	

		elif usr_inp=="clear":
			os.system("clear")
		
		elif usr_inp=="ssh":
			ssh_brute()

		else:
			print(usr_inp+": command not recognised ~brutus")
		
