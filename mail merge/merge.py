import os 


current = os.getcwd()

os.chdir('D:/secrets/emailcredentials')

f = open('vaibhav.txt','r')
cred = f.readlines()
for i in range (0,len(cred)):
	cred[i]=cred[i].replace('\n','')

me = cred[0]
password = cred[1]

f = open('data.csv','r')

rough = f.readlines()

for i in range(0,len(rough)):
	rough[i] = rough[i].replace('\n','')

heads = rough[0].split('\t')

mailing_list = []

for i in range(1,len(rough)):
	mailing_list.append(rough[i].split('\t'))

print mailing_list



import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# # me == my email address
# # you == recipient's email address
# me = "my@email.com"
# you = "your@email.com"




# # Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Abey tera kaam ho gaya !"
msg['From'] = me


# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# # Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# # Attach parts into message container.
# # According to RFC 2046, the last part of a multipart message, in this case
# # the HTML message, is best and preferred.


# # html = 'html version'
# # text = 'TEST VERSION'
subject = "BACKUP REPORT"
print 'SMTPING' 
# message = createhtmlmail(html, text, subject, 'Vaibhav Singhal <vaibhav.singhal@askiitians.com>')
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
print 'connected'
server.login(me, password)
print ('logged in ')
for i in mailing_list:
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Abey tera kaam ho gaya ! Take 3"
	msg['From'] = me
	msg['To'] = i[1]
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
	html = """\
	<html>
	  <head></head>
	  <body>
	   <p><strong>{{name}}</strong><br /><strong> 8 Sue Circle</strong><br /><strong> Smithtown, CA 08067</strong><br /><strong> 909-555-5555</strong><br /><strong> john.donaldson@emailexample.com</strong></p>
	<p>Date</p>
	<p>George Gilhooley<br /> XYZ Company<br /> 87 Delaware Road<br /> Hatfield, CA 08065</p>
	<p>Dear <strong>Mr. Gilhooley,</strong></p>
	<p>I am writing to apply for the programmer position advertised in the <em>Times Union</em>. As requested, I am enclosing a completed job application, my certification, my resume, and three references.</p>
	<p>The opportunity presented in this listing is very interesting, and I believe that my strong technical experience and education will make me a very competitive candidate for this position. The key strengths that I possess for success in this position include:</p>
	<ul>
	<li>I have successfully designed, developed, and supported live use applications</li>
	<li>I strive for continued excellence</li>
	<li>I provide exceptional contributions to customer service for all customers</li>
	</ul>
	<p>With a BS degree in Computer Programming, I have a full understanding of the full life cycle of a software development project. I also have experience in learning and excelling at new technologies as needed.</p>
	<div id="adsense2" class="adsense-slot adsense ads-half">&nbsp;</div>
	<p>Please see my resume for additional information on my experience.</p>
	<p>I can be reached anytime via email at john.donaldson@emailexample.com or my cell phone, 909-555-5555.</p>
	<p>Thank you for your time and consideration. I look forward to speaking with you about this employment opportunity.</p>
	<p>Sincerely,</p>
	<p><em>Signature </em>(for hard copy letter)</p>
	<p>John Donaldson</p>
	  </body>
	</html>
	"""
	for ii in range(0,len(heads)-1):
		html = html.replace("{{"+heads[ii]+"}}",i[ii])

	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	msg.attach(part1)
	msg.attach(part2)
	print i[1]
	server.sendmail('sender@host.com', i[1], msg.as_string())

# # Send the message via local SMTP server.
# s = smtplib.SMTP('localhost')
# # sendmail function takes 3 arguments: sender's address, recipient's address
# # and message to send - here it is sent as one string.
# s.sendmail(me, you, msg.as_string())
# s.quit()