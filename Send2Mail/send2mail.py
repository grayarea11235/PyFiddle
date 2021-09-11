# Utility to send notes, urls, files etc to a email.
# Just using SMTP

import argparse
import ssl
import smtplib
import config
import base64

from email.mime.text import MIMEText

# Command format
#   send2mail -f <file>
#   send2mail -s <string>
#   send2mail -l <link>
#
# Email subject : send2mail has sent you a file/text/link from <machine>(<IP Address>) at <datetime>


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    #return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    return message


def process_cmd_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="send sgtring to email")

    args = parser.parse_args()

    type = 'invalid'
    data = None
    print(args.string)
    if args.string != None:
        type = 'string'
        data = args.string

    return type, data


def send_email(msg):
    context = ssl.create_default_context()
    print(context)

    with smtplib.SMTP_SSL("smtp.gmail.com", config.port, context=context) as server:
        server.login(config.user_name, config.password)
        print(server)
        server.sendmail(config.user_name, config.user_name, msg=msg.as_string())


def main():
    print(config.user_name)
    type, data = process_cmd_line()
    print("{} {}".format(type, data))
    
    msg = None
    if type == 'string':
        msg = create_message('ciaran.dunn@gmail.com', 'ciaran.dunn@gmail.com', 'String message from send2email', data)
        print(msg)
    
    if msg:
        send_email(msg)


if __name__ == '__main__':
    main()
