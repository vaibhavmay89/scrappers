import telnetlib

# HOST = "mail.reddit.com"
# tn = telnetlib.Telnet(HOST,"25")
# tn.write("Hello\n")

# try:
#     serveroutput = tn.read_until(b'STARTTLS')
#     print(type(serveroutput))
# except Exception as e:
#     tlsbool = '?'
#     print('XXX')
# import dns.resolver

# answers = dns.resolver.query('dnspython.org', 'MX')
# for rdata in answers:
#     print 'Host', rdata.exchange, 'has preference', rdata.preference

import socket
server = "ymail.com"
ip_list = []
ais = socket.getaddrinfo(server,0,0,0,0)
for result in ais:
  ip_list.append(result[-1][0])
ip_list = list(set(ip_list))
serverList = ['yahoomail.com']
print(ip_list)
import subprocess # Import the subprocess module
 # Open the file and read each line
servs = []
for server in serverList:
	t = subprocess.Popen(('nslookup -q=mx '+server), stdout=subprocess.PIPE).communicate()[0] # Run the nslookup command for each server in the list
	print ('------sfgdfg---------')

	t = t.split('\n')
	for i in range(0,len(t)): 
		# if 'MX preference' in t[i]:
		servs.append(t[i])

# f = open('server_response.txt','w')
for i in servs: 
	print(i)
# tn = telnetlib.Telnet("alt2.aspmx.l.google.com","25")