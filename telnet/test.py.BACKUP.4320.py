<<<<<<< HEAD
# serverlist.append(['askiitians.com',30,'aspmx2.googlemail.com'])

import telnetlib 
host = 'aspmx2.googlemail.com'
timeout = 5
session = telnetlib.Telnet(host, 25, timeout)
session.open(host,port ='25',timeout = timeout)
session.write("\r\n")
print(session.read_until("fadsgsadg",10))
session.write("helo hi"+b"\r")
print(session.read_until('kvjvk',10))
session.write(('MAIL FROM:vaibhavmay89@gmail.com').encode('ascii') + b"\r")
frommail= session.read_until(b"/r/n/r/n#>", timeout-1 )
session.write(('RCPT TO:info@askiitians.com').encode('ascii') + b"\r")
check= session.read_until(b"/r/n/r/n#>", timeout-1 )
session.close()
=======
import telnetlib 
import time 


# askiitians.com',30,'aspmx5.googlemail.com']

session = telnetlib.Telnet('aspmx5.googlemail.com','25',15)
print(session.read_some())
session.write(('HELO hi\r\n').encode('ascii'))
print(session.read_very_lazy())
session.write(('HELO hi').encode('ascii'))
print(str(session.read_very_lazy()).encode('ascii'))
>>>>>>> b0db39e7e69bbe86205ca81fb88e31d9b0cee35e
