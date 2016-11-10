import signal
from smtp_mail_brute import smtp_mail_brute
import os
from smtp_gmail_brute import smtp_gmail_brute

def smtp():

	while(1):
		usr_inp=raw_input(">>>smtp>>>")
		

		if usr_inp=="":
			usr_inp=raw_input(">>>smtp>>>")

		elif usr_inp=="clear":
			os.system("clear")
			usr_inp=raw_input(">>>smtp>>>")

		elif usr_inp=="exit" or usr_inp=="quit":
			quit()

		elif usr_inp=="help":
			help_smtp()

		elif usr_inp=="mail.com":
			smtp_mail_brute()

		elif usr_inp=="gmail.com":
			smtp_gmail_brute()

		else:
			print(usr_inp + ": command not recognised:~brutus")
			usr_inp=raw_input(">>>smtp>>>")
