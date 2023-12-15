# Automatic-Payment-Indicator
PROJECT DESCRIPTION:
Modules used -smtplib,pandas,time,datetime

PROJECT DESCRIPTION 
This programme can automatically remind people for payment every month, if they had not paid their dues till 3rd day of month it will automatically sent email.
First ,pandas is used to read csv file.The csv file has names of person concerned,payment date,payment status,receiver's email,and email status.
On every 1 day of month this programme reset payment status and email status to 'pending' and 'not sent' respectively.
The programme will check todays date if it is greater than 3,it will further check the payment status and email status ,if it is 'pending' and 'not sent' .
If all conditions are met ,it will automatically send email to concerned person.
And thereafter it will update email status to 'sent'.
If defaulter pays to owner he can manually update payment date and status in csv file.
We can put this programme on task scheduler.
Moreover,instead of or in addition to mail we can use sms apis to sent sms as well.
It can be useful for persons who are concerned with regular payments such as landlords.

