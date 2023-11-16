import smtplib

my_email = "test@gmail.com"
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="test2@gmail.com", msg="Subject:Hey\n\nBody.")
