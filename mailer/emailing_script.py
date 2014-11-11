import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

user_email = 'apurva.iit.roorkee@gmail.com'
FROM = user_email
last = open('variable.txt', 'r')
p = last.readlines()
p = (int(p[0]))
nom = p
def send_mail(email, message_html,message_text):
	global nom
	global FROM
	global server
	#### maiking the mail ##########
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Indian Institute of Technology, Roorkee (IIT - Roorkee)'
	nom += 1 
	msg['From'] = 'Apurva Singhal'
	msg['To'] = email
	part1 = MIMEText(message_text, 'plain')
	part2 = MIMEText(message_html, 'html')
	msg.attach(part1)
	msg.attach(part2)
	try:
		server.sendmail(FROM, [str(email)], msg.as_string())
	except:
		print('Failed to send messages')
	print (str(nom)+ '--> ' + email)
	f = open('done.csv','a')
	f.write('\n'+email)




#### Emails import ######
# emails = [['vaibhavmay89+1@gmail.com', 'paper 1', 'journal A'],['vaibhavmay89+2@gmail.com', 'paper 2', 'journal A'],['vaibhavmay89+3@gmail.com', 'paper 3', 'journal A'],['vaibhavmay89+4@gmail.com', 'paper 4', 'journal A']]
emails = []
with open('final data.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		emails.append(list(row))



##### HTML 	import  ##########
html = open('emailer1.html', encoding = 'utf8')
c = html.readlines()
a = ''
for line in c: 
	a += line + '\n'

html = open('mailer.txt', encoding = 'utf8')
c = html.readlines()
text = ''
for line in c: 
	text += line + '\n'


message_template_text = text

message_template_html = a



#######################


###########Logging into gmail ################

# gmail_user = 'apurvasinghaliitr@gmail.com'
# gmail_pwd = 'apurvahere'
# FROM = 'apurvasinghaliitr@gmail.com'

gmail_user = user_email
gmail_pwd = 'apurvahere'
FROM = user_email

# Prepare actual message
#message = '\From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM, ', '.join(TO), SUBJECT, TEXT)
try:
    #server = smtplib.SMTP(SERVER) 
    server = smtplib.SMTP('smtp.gmail.com', 587) #or port 465 doesn't seem to work!
    print ('Finding Google servers')
    server.ehlo()
    print ('Found server.... setting up secure connection')
    server.starttls()
    print ('Connection Established.. Logging in ')
    server.ehlo()
    server.login(gmail_user, gmail_pwd)
    print ('Logged in as '+ gmail_user)
    
    
except:
    print ('Failed to log in')

for i in range(p,p+95) :

	temp_text = message_template_text.replace('{{Article}}',emails[i][1])
	temp_text = temp_text.replace('{{Journal}}',emails[i][2])
	temp_html = message_template_html.replace('{{Article}}',emails[i][1])
	temp_html = temp_html.replace('{{Journal}}',emails[i][2])
	send_mail(emails[i][0],temp_html,temp_text)
	with open('variable.txt', 'w') as f: 
		f.write(str(i+1))
		f.close()


server.close()




