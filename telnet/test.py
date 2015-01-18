import telnetlib 
import time 


# askiitians.com',30,'aspmx5.googlemail.com']

session = telnetlib.Telnet('aspmx5.googlemail.com','25',15)
print(session.read_some())
session.write(('HELO hi\r\n').encode('ascii'))
print(session.read_very_lazy())
session.write(('HELO hi').encode('ascii'))
print(str(session.read_very_lazy()).encode('ascii'))