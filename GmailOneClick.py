import smtplib

server = smtplib.SMTP('smtp@gmail.com', 587)
server.starttls()
server.login('abhishekphd14@gmail.com','abhi49@#')
server.sendmail('abhishekphd14@gmail.com',  'nikhil80908@gmail.com',  "It's my gmail for you made by python")

print("Your mail has been sent")

# You can't use this code for sending automate males on those accounts which are secured by this tech \ 
# coz google wants to fight with spam mail which are bombarded in your mail so yeahhh
