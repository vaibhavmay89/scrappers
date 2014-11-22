import mechanize
import csv


def reg(NAME = 'test',email = 'test@bikaner24.com',mobile = '+91-81308734',grade = 6,password = '1234567',URL = 'http://www.askiitians.com/myaccount.aspx'):

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22")]
	br.open(URL)
	br.select_form(nr =0)
	br.form['txtfirstname'] = NAME 
	#br.form['spnCountryName'] = '+91'
	br.form['txtMobile'] = mobile
	br.form['txtemailid'] = email
	br.form['txtregpassword'] = password
	br.form['txtconfirmpassword'] = password
	#br.form['drpGrade'] = ['*', '6', '7', '8', '9', '10', '11', '12', '12th pass']
	br.set_value(list(str(grade)), name='drpGrade')
	#br.form['drpGrade'] = ['6',]
	
	br.submit(nr=1)

	print "SELECT * FROM dbo.fn_GetUserDetails('"+email+"')\n"

data = []

with open('data.csv', 'r') as f:
    reader = csv.reader(f,delimiter = ',')
    for row in reader:
        data.append(row)
##name,email,mobile,grade,password,url
print data
for lead in data:
	print lead[0]

	reg(lead[0],lead[1],lead[2],lead[3],lead[4],lead[5])


#Test3,test35566@gmail.com,8130386175,6,maxxishe45re,http://www.askiitians.com/myaccount.aspx