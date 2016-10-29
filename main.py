from menu import menu
from disclaimer import disclaimer
import os


def main():
	disclaimer()
	print("\n")
	print("Do you agree?[y/n]")
        inp=raw_input("brutus>")
	while 1:
		if inp=="y" or inp=="Y":
			break
		elif inp=="n" or inp=="N":
			print("Goodbye!!")
			quit()
		else:
			print("[!]Do you agree?[y/n]")
			inp=raw_input("brutus>")
	menu()

main()
