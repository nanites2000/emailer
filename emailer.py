import csv
import smtplib

week1 = ('A','B','C','D','E')
week2 = ('F','G','H')
week3 = ('I','J','K','L','M','N','O','P','Q')
week4 = ('R','S','T','U','V','W','X','Y','Z')

week_letters = week3


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('', '') #put in google api login and token

with open('ward12thcsv.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    readlist = list(reader)

    for row in readlist:
        print(row['Last'][0])
        if row['Last'][0] in week_letters:
            if '@' in row['Email']:
                print('Sent to ' + row['Email'])
                # print('Email to ' + row['Email'])
                message = 'To: ' + row['Email'] +'\n' \
                        'Subject: The ' + row['Last'] +" family gets to help clean this week\n" \
                     "It is that time again, the church needs cleaning and the first letter in your last name gets your family a turn to help this week." \
                      "\n See you there at 8:00 AM on this Saturday morning."
                smtpObj.sendmail('', row['Email'],message) #enter the login email here again
smtpObj.quit()