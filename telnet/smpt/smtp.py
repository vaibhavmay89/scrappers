import smtplib

msg = """
<html>
<head>
<title>iit guru</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

</head>
<body bgcolor="#FFFFFF" style="margin:auto">
<!-- Save for Web Slices (referralcandy mailer.psd) -->
<table id="Table_01" border="0" cellpadding="0" cellspacing="0" align="center" style="border:1px solid #1c542b">
	  <tr>
          <td align="left" valign="top" style="border-bottom:4px solid #f47408"><a target="_blank" href="http://www.askiitians.com/?utm_source=mailer&utm_medium=email&utm_term=view&utm_campaign=Paid.logo"><img src="http://cdn.askiitians.com/resources/images/logo.png" alt="askIITians.com" title="askIITians" style="max-width:325px;width:100%;border:0;padding:2%;display:block"/></a>
        </td>
        </tr>
         <tr> <td style="font-family:CalibriVerdana, Geneva, sans-serif; font-size:22px; color:#333; padding:0 0 0 0; text-align:center"><b>Are you preparing for JEE Main / JEE Advanced <br> / Madical / SAT II</h2>
</b>
<hr>
</td>
	</tr>
    
    <tr>
		<td><p style="font-family:open Verdana, Geneva, sans-serif;text-align:center; font-size:35px; font-weight:bold">Meet the Gurus in Kuwait on</p></td></tr>
        <tr>
		<td>
        <table border="0" cellspacing="0" cellpadding="0" style="max-width:599px; margin:auto; width:100%;table-layout:fixed; background-color:#FFC; text-align:center" > 
    <tr>
    <td style="display:inline-block; text-align:left;width:58%;">
   <p style="font-family:Calibri; font-size:12px; text-align:left; color:black; padding:10px; margin:5px; "><b>Date: 15th Jan 2015(Thursday)</b><br>
Time: 6 PM<br>
Venue 1: United Indian School,<br> Jleeb Al Shuoyokh, Kuwait<br>
<b>Date: 17th Jan 2015(Saturday)</b><br>
Time: 6 PM<br>
Venue 2: Carmel School, Khaitan, Kuwait<br>
<b>Date: 22nd Jan 2015(Thursday)</b><br>
Time: 6 PM<br>
Venue 3:Fahaheel Al Wataniah  DPS School</p><br></td>
    <td style="display:inline-block;padding-bottom:15px">
      <p style="font-family:Calibri; font-size:16px; text-align:center; color:black; padding:0; margin:5px; font-weight:bold; ">Interested ?<br> 
Book your seat for seminar</p><br>
<a href="#" style="text-decoration:none; font-family:Calibri; font-size:18px; font-weight:bold;background-color:#F60; padding:10px;border-radius:5px; color:#FFF; text-transform: uppercase;margin:auto;display:table; margin:auto">Meet our Experts</a>
</td>
    </tr>
    </table>
  </td></tr>
  
       <tr>
		<td>
        <table border="0" cellspacing="0" cellpadding="0" style="text-align:center;max-width:599px; margin:auto; width:100%;table-layout:fixed; background-color:#f1f2f2" > 
    <tr>
    <td style="display:table-cell; margin:0; width:119px; vertical-align:top; padding:0 0;border-bottom: 1px solid #000;border-top: 1px solid #000;">
    <img src="images/aditya.jpg" width="119" height="142" alt="aditya">
    
    </td>
    <td style="display:table-cell; margin:0; text-align:left; vertical-align:top;border-bottom: 1px solid #000;border-top: 1px solid #000;">
       <p style="font-family:Calibri; font-size:12px; text-align:justify;color:black; padding:10px; margin:5px; ">
<b>Aditya Singhal</b><br>
<b>B.Tech from IIT Delhi-2005</b><br>
Aditya Singhal is one of the promoter Director of Transweb Educational Services Pvt Ltd. He earned his B.Tech Degree from prestigious IIT Delhi in year 2005. He has a vast experience in the field of education and technology. He is one of the pioneers in the field of Online Education in India.
</p>

</td>
    </tr>
    <tr>
    <td style="display:table-cell; margin:0; width:119px; vertical-align:top; padding:0 0;border-bottom: 1px solid #000; background-color:#FFF">
    <img src="images/Nishant.jpg" width="119" height="142" alt="aditya">
    
    </td>
    <td style="display:table-cell; margin:0; text-align:left; vertical-align:top;border-bottom: 1px solid #000; background-color:#FFF">
       <p style="font-family:Calibri; font-size:12px; text-align:justify;color:black; padding:10px; margin:5px; "><b>Nishant Sinha</b><br>
         <b>B.Tech from IIT Delhi-2005</b><br>
Nishant Sinha is one of the prometer Director of Transweb Educational Services Pvt Ltd. He earned his B.Tech degree from Indian Institute of Technology- IIT Delhi in year 2003. He carries a vast experience in the field of education and strategy. He is one of the pioneer in the field of online education in India.
</p>

</td>
    </tr>
    <tr>
    <td style="display:table-cell; margin:0; width:119px; vertical-align:top; padding:0 0;border-bottom: 1px solid #000;">
    <img src="images/Amit.jpg" width="119" height="142" alt="aditya">
    
    </td>
    <td style="display:table-cell; margin:0; text-align:left; vertical-align:top;border-bottom: 1px solid #000;">
       <p style="font-family:Calibri; font-size:12px; text-align:justify;color:black; padding:10px; margin:5px; ">
<b>Amit Shekhar</b><br>
<b>B.Tech from IIT Kharagpur - 2008</b><br>
An IIT Kharagpur alumni, Mr. Amit Shekhar, has a rare passion for technology and a good command over the education sector, especially in terms of engineering exam preparation. His depth of knowledge about recent engineering developments and new products in the market is enviable. He left top investment bank to join TransWeb Educational Service Pvt. Ltd.</p>

</td>
    </tr>
    <tr>
    <td style="display:table-cell; margin:0; width:119px; vertical-align:top; padding:0 0;border-bottom: 1px solid #000; background-color:#FFF">
    <img src="images/Subrat.jpg" width="119" height="142" alt="aditya">
    
    </td>
    <td style="display:table-cell; margin:0; text-align:left; vertical-align:top;border-bottom: 1px solid #000; background-color:#FFF">
       <p style="font-family:Calibri; font-size:12px; text-align:justify;color:black; padding:10px; margin:5px; ">
<b>Subrat Sagar</b><br>
<b>
MBA from Symbiosis Pune- 2010</b><br>
A Symbiosis Alumni, Mr Subrat Sagar has a vast experience in education sector. He specializes in career guidance and has counseled more than 50000 students till date. Known for his power to establish an immediate connect with the students because of his sense of humor, and ability to speak at the level of audience. Subrat Sagar is driven by a deep desire to contribute to the education sector.
</p>

</td>
    </tr>
    </table>
    
  </td></tr>  
  </tr>
  
  <tr>
  <td><img src="images/top.jpg" width="599" style="max-width:599px;width:100%;display:block"></td>
  </tr>
  <tr>
  <td><img src="images/top_2.jpg" width="599" style="max-width:599px;width:100%;display:block"></td>
  </tr>
  <tr>
  <td><img src="images/top_3.jpg" width="599"style="max-width:599px;width:100%;display:block"></td>
  </tr>
  <tr>
  <td><img src="images/top_4.jpg" width="599"style="max-width:599px;width:100%;display:block"></td>
  </tr>
  <tr>
  <td><img src="images/top_5.jpg" width="599"style="max-width:599px;width:100%;display:block"></td>
  </tr>
  <tr>
  <td style="background-color:#06C"> <p style="font-family:Calibri; font-size:24px; color:#FFF; font-weight:bold; text-align:center">askIITians Courses</p></td>
  </tr>
  <tr> 
    <td style="background:#FFC">
    <table border="0" cellspacing="0" cellpadding="0" style="max-width:599px; margin:15px auto;width:100%; text-align:center;table-layout:fixed";> 
    <tr>
    <td style="display:inline-block; margin:0 " ><p style="font-family:Calibri; font-size:12px; text-align:Center;color:black; padding:5px; margin:5px; font-weight:bold">Foundation Courses<br>
for Grade 6th to <br> Grade 10th</p>
</td>
    <td style="display:inline-block; margin:0 "><p style="font-family:Calibri; font-size:12px; text-align:Center;color:black; padding:5px; margin:5px; font-weight:bold">1 Year & 2<br> years Engineering Entrance <br>
Exam preparation <br>
Cousres for grade <br>
12th/12th pass <br>
and Grade 11th</p></td>
    <td style="display:inline-block; margin:0"><p style="font-family:Calibri; font-size:12px; text-align:Center;color:black; padding:5px; margin:5px;font-weight:bold">1 Year & 2 years <br>Medical Entrance Exam<br> 
preparation Cousres for <br>
grade 12th/12th pass <br>
and Grade 11th </p></td>
 <td style="display:inline-block; margin:0 "><p  style="font-family:Calibri; font-size:12px; text-align:Center;color:black; padding:5px; margin:5px; font-weight:bold" >1 Year & 2 years <br>Medical Entrance Exam <br>
preparation Cousres for <br>
grade 12th/12th pass <br>
and Grade 11th</p> </td>
    </tr>
    </table>
    </td>
    </tr>
  
  
  
         
  <tr>
      <td style="padding:0">
      <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color:#666; font-family:Arial, Helvetica, sans-serif; font-size:12px; color:#fff; line-height:18px;border-bottom:5px solid #ED8103;">
<tr>
<td width="" style="padding:10px 20px;">Contact Us<br />
Ph no.- 1800 2000 838<br />
Email at - <a href="mailto:info@askiitians.com" target="_blank" style="color:#fff;">info@askiitians.com</a></td>
<td width="">&nbsp;</td>
<td width="" align="center" valign="top" style="padding-top:10px;">
<table width="50%" border="0" cellspacing="0" cellpadding="0">
<tr>
<td colspan="4" style="padding:5px;color:#fff;font-size:12px;">Stay connected</td>
</tr>
<tr>
<td align="center" valign="bottom" style="padding-right:5px;"><a href="https://www.facebook.com/askiitians?utm_source=mailer&utm_medium=email&utm_term=view&utm_campaign=Paid.facebook" target="_blank"><img src="http://cdn.askiitians.com/Images/flyer/facebook.png" alt="F" title="facebook" border="0" style="width:20px; height:20px;font-size:12px; color:#fff;" /></a></td>
<td align="center" valign="bottom" style="padding-right:5px;"><a href="https://twitter.com/askiitians_user?utm_source=mailer&utm_medium=email&utm_term=view&utm_campaign=Paid.twitter" target="_blank"><img src="http://cdn.askiitians.com/Images/flyer/twitter.png" alt="T" title="twitter" border="0" style="width:20px; height:20px;font-size:12px; color:#fff;" /></a></td>
<td align="center" valign="bottom" style="padding-right:5px;"><a href="https://plus.google.com/110203723110153822350/posts?utm_source=mailer&utm_medium=email&utm_term=view&utm_campaign=Paid.google" target="_blank"><img src="http://cdn.askiitians.com/Images/flyer/gplus.png" alt="G+" title="google plus" border="0" style="width:20px; height:20px;font-size:12px; color:#fff;" /></a></td>
<td align="center" valign="bottom" style="padding-right:5px;"><a href="http://www.pinterest.com/askiitians/?utm_source=mailer&utm_medium=email&utm_term=view&utm_campaign=Paid.pinterest" target="_blank"><img src="http://cdn.askiitians.com/Images/flyer/pinterest.png" alt="P" title="Pinterest" border="0" style="width:20px; height:20px;font-size:12px; color:#fff;" /></a></td>
</tr>
</table></td>
</tr>
</table></td>
      </tr>
      
        
</table>

<!-- End Save for Web Slices -->
</body>
</html>





"""
def smtp_check(email,mxserver):
	smtp = smtplib.SMTP(timeout=10)
	smtp.connect(mxserver)
	try:
		status = smtp.helo()
		mail_to = smtp.mail('vaibhav.singhal@askiitians.com')
		rcpt = smtp.rcpt(email)
		smtp.sendmail('vaibhavmay89@gmail.com', 'vaibhav.singhal@askiitians.com', msg)
	except:
		return('No handshake')
	return([status[0],mail_to[0],rcpt])



print(smtp_check('vaibhavmay89@gmail.com','alt2.gmail-smtp-in.l.google.com'))


