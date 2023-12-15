import pandas as pd 
import numpy as np 
import smtplib 
import time
import datetime
df=pd.read_csv('pay.csv')
def email(receiver_email,name):
    user='sendergmail'
    password='*****'
  
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    s.starttls()
    
    s.login(user,password)
 
    message = f"your payment is due ,please send your bills {name} "
 
    s.sendmail(user, f"{receiver_email}", message)

    # terminating the session
    s.quit()
        
today=datetime.datetime.now()
today=time.strftime("%d-%m-%Y")
today=today.split('-')
print(today)

if today[0]=='01':#updates status to pending in first day of month
   df.loc[:,'status']='pending'
   df.loc[:,'email sent']='not sent'#updates email status on 1st date of every month 
   
df.to_csv('pay.csv',index=False)#saved changes in csv file

for index,item in df.iterrows():
    print(type(item))
    if int(today[0])>3 and item['status']=='pending':
        if item['email status']!='sent':
            print("hello")
            new_item=item['email']
            x=item['name']
            df.loc[index,['email status']]='sent'
            email(new_item,x)
df.to_csv('pay.csv',index=False)
