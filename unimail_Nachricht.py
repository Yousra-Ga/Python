import imaplib

mail = imaplib.IMAP4_SSL("unimail.tu-dortmund.de")
mail.login("yousra.gamani@tu-dortmund.de","YouyouMoham0!Abu")

mail.select("inbox")
result,data = mail.search(None,'UNSEEN')
result,data = mail.fetch()
