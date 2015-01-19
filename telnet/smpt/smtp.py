import smtplib


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



print(smtp_check('vaibhavmay89@gmail.com','alt2.gmail-smtp-in.l.google.com'))


