import subprocess
import socket
import re
import smtplib
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
reg = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
rec= re.compile(reg)

good_domains = set([])
bad_domains = set([])

responsive_domains =set([])
blocked_domains = set([])

def smtp_check(email,mxserver):
	smtp = smtplib.SMTP(timeout=10)
	smtp.connect(mxserver)
	try:
		status = smtp.helo()
		mail_to = smtp.mail('vaibhav.singhal@askiitians.com')
		rcpt = smtp.rcpt(email)
	except:
		return('No handshake')
	return([status[0],mail_to[0],rcpt])


def validate_server(domain): 
	print(domain)
	t = ''
	try:
		t = subprocess.Popen(('nslookup -q=mx '+domain), stdout=subprocess.PIPE).communicate()[0:]
	except:
		# print(-1)
		return([-1,'Didnt connect'])
	if 'MX preference' in t:
		print (1)
		return([1,'Valid Mail Server'])
	else:
		print([0,'Mail Server not Found'])


def fn_check_mx(domain):
	global good_domains,bad_domains
	if domain in good_domains:
		return(1)
	elif(domain in bad_domains):
		return(0)
	else:
		p = validate_server(domain)
		if p[0] == 1:
			good_domains.add(domain)
			return([1,'Has a valid smtp server'])
		else:
			bad_domains.add(domain)
			return([0,'No smtp found'])


def check_regex(email):
	global rec
	try:
		if email == re.match(rec,email).group():
			return([1,'regex matches'])
		else: 
			return([0,'regex doesnt match'])
	except:
		return([0,'regex not formed'])
		

def check_email(email,check_mx=0):

	reg = check_regex(email)
	if reg[0] == 1 and check_mx == 1 :
		mx = fn_check_mx(email.split('@')[1])

		return([reg,mx])
	else:
		return([reg])
	pass


f = open('emails.txt','r')
raw = []
validations = []

a = f.readlines()
for i in a: 
	raw.append(i.replace('\n',''))

for email in raw:
	validations.append([email,check_email(email, check_mx=1)]) 


for i in good_domains: 
	print(i)