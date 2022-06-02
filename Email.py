import smtplib, ssl

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "siobaldonna24@gmail.com"
receiver_email = input("Receiving Address: ")
subject = input("Subject: ")
message = input("Message: ")

mail = f'Subject: {subject}\n\n{message}'

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, "Unbreakable24")
    server.sendmail(sender_email, receiver_email, mail)