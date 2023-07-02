import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject

    # Add body to the email
    email_message.attach(MIMEText(message, 'plain'))

    # Create SMTP session for sending the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Convert the multipart message to a string
    email_text = email_message.as_string()

    # Send the email
    smtp_server.sendmail(sender_email, receiver_email, email_text)
    smtp_server.quit()

# Example usage
sender_email = 'aakritigoyal14@gmail.com'
sender_password = 'usuetzyrwvmnvurz'
receiver_email = 'keshavbiyani23@gmail.com'
subject = 'Hello from Aakriti!'
message = "I hope you are well , Let's meet soon ."

send_email(sender_email, sender_password, receiver_email, subject, message)
