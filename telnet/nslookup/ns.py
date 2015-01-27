import subprocess

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
	# print(local_list[minindex])
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



email = 'vaibhavmay89@gmail.com'

print(validate_server(email.split('@')[1]))

for i in mailServers: 
	print i