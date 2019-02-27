import smtplib
from config import Mail_config

def send_mail(r: dict):
	sent_from = Mail_config.EMAIL_USER  
	to = [r['user']]  
	subject = 'Price changed!'  

	email_text = """
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, r['message'])

	try:  
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(Mail_config.EMAIL_USER, Mail_config.EMAIL_PASSWORD)
	    server.sendmail(sent_from, to, email_text)
	    server.close()

	    return 'Email sent!'
	except(e):  
	    return 'Something went wrong... {}'.format(e)