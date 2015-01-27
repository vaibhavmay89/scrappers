import subprocess
import socket
import re
import smtplib
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
reg = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
rec= re.compile(reg,flags=re.IGNORECASE)

good_domains = set([])
bad_domains = set([])

responsive_domains =set([])
blocked_domains = set([])

def filewrite(data,fname,mode):
	if fname == 'final.txt':
		data = str(data)
		removals = ['[',']','(',"'",')']
		for r in removals:
			data = data.replace(r,'')
	f = open(fname,mode)
	f.write(str(data)+'\n')
	f.close()



def smtp_check(email,mxserver):
	global mailServers
	domain = email.split('@')[1]
	for i in mailServers: 
		if domain == i[0]:
			mxserver = i[2]
			break
	smtp = smtplib.SMTP(timeout=10)
	
	try:
		smtp.connect(mxserver)
		status = smtp.helo()
		mail_to = smtp.mail('vaibhav.singhal@askiitians.com')
		rcpt = smtp.rcpt(email)
	
	except:
		return(['No handshake'])

	return([status[0],mail_to[0],rcpt])


mailServers = []


def parser(t):
	# print(t)
	global mailServers
	t = t.split('\n')
	local_list = []
	minvar = 100000
	minindex = 0
	for line in t: 
		if "mail exchanger" in line:
			# print(line)
			line = line.replace('\r','')
			line = line.replace('\n','')
			line = line.replace('MX preference = ','')
			line = line.replace(' mail exchanger = ','')
			temp = [line.split('\t')[0],int(line.split('\t')[1].split(',')[0]),line.split('\t')[1].split(',')[1]]
			if 'root' in temp[2]:
				temp[2] = temp[0]
			local_list.append(temp)

	for i in range(0,len(local_list)):
		if local_list[i][1]< minvar:
			minvar = local_list[i][1]
			minindex = i
		else:
			continue
	print(local_list[minindex])
	mailServers.append(local_list[minindex])



def validate_server(domain): 
	# print(domain)
	t = ''
	try:
		# subprocess.Popen(('nslookup -q=mx '+domain))
		t = subprocess.Popen(('nslookup -q=mx '+domain), stdout=subprocess.PIPE).communicate()[0]
		new = t
	except:
		# print(-1)
		return([-1,'Didnt connect'])
	if 'MX preference' in t:
		parser(t)
		return([1,'Valid Mail Server'])
		
	else:
		return([0,'Mail Server not Found'])


def fn_check_mx(domain):
	global good_domains,bad_domains
	if domain in good_domains:
		return([1,'Has a valid smtp server'])
	elif(domain in bad_domains):
		return([0,'No smtp found'])
	else:
		p = validate_server(domain)
		if p[0] == 1:
			good_domains.add(domain)
			return([1,'Has a valid smtp server'])
		else:
			bad_domains.add(domain)
			filewrite(p,'bad_domains.txt','a')
			return(p)


def check_regex(email):
	global rec
	try:
		if email == re.match(rec,email).group():
			return([1,'regex matches'])
		else: 
			return([0,'regex doesnt match'])
	except:
		return([-1,'regex not formed'])
		

def check_email(email,check_mx=0):
	reg = []
	mx = []
	scheck = []

	reg = check_regex(email)
	if reg[0] == 1 and check_mx == 1 :
		mx = fn_check_mx(email.split('@')[1])
		if mx[0] == 1:

			scheck = smtp_check(email,'')
			print(scheck)

		return([reg,mx,scheck])
		print([reg,mx,scheck])
	else:
		return([reg])
	pass


f = open('emails.txt','r')
raw = []
validations = []

a = f.readlines()
for i in a: 
	raw.append(i.replace('\n',''))
filewrite(['Email','Reg Status','Reg Message','SMTP Exists ? ','SMTP EXsist message','HELO','FROM','RCPT','RCPT MESSAGE'],'final.txt','a')
for email in raw:
	validations.append([email,check_email(email, check_mx=1)]) 
	filewrite([email,check_email(email, check_mx=1)],'final.txt','a')



for i in good_domains: 
	print(i)