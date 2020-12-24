import smtplib
#Connect to Gmail
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()

    #Encrypt traffic
    smtp.starttls()
    smtp.ehlo()

    
    smtp.login()
