import imaplib, email
import os 
import subprocess

password = os.environ.get("MAIL_PASSWORD")

mail = imaplib.IMAP4_SSL("unimail.tu-dortmund.de")
mail.login("smyogama",password)
mail.select("inbox")
status,data = mail.search(None,'UNSEEN')
#print(f"write{status,data}")
for num in data[0].split():

    status, msg_data = mail.fetch(num ,"(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])
    print(msg["subject"])
    title= "Unimail Nachricht"
    message= msg["subject"]

    subprocess.run(["notify-send", title, message])
mail.logout()

