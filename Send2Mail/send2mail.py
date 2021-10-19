#!/usr/bin/env python3

# Utility to send notes, urls, files etc to a email.
# Just using SMTP

import os
import argparse
import ssl
import smtplib
import config
import base64
import mimetypes
import email.encoders

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio

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

    return message


def create_message_with_attachment(
    sender, to, subject, message_text, file):
    """Create a message for an email.

    Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.
        file: The path to the file to be attached.

    Returns:
        An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg = MIMEText(message_text)
    message.attach(msg)

    content_type, encoding = mimetypes.guess_type(file)

    print("content_type = {} encoding = {}".format(content_type, encoding))

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    
    main_type, sub_type = content_type.split('/', 1)
    
    if main_type == 'text':
        fp = open(file, 'rt')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        email.encoders.encode_base64(msg)
        fp.close()
    
    filename = os.path.basename(file)
    
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

    #return base64.urlsafe_b64encode(message.as_bytes()).decode()
    return message


def process_cmd_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="send string to email")
    parser.add_argument("-f", "--file", help="send file to email")

    args = parser.parse_args()

    type = 'invalid'
    data = None
    print(args.string)
    if args.string != None:
        type = 'string'
        data = args.string
    if args.file != None:
        type = 'file'
        data = args.file

    return type, data


def send_email(msg):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", config.port, context=context) as server:
        server.login(config.user_name, config.password)
        
        print('Sending email...')
        server.sendmail(config.user_name, config.user_name, msg=msg.as_string())
        print('Message sent')

def main():
    print(config.user_name)
    type, data = process_cmd_line()
    print("{} {}".format(type, data))
    
    msg = None
    if type == 'string':
        msg = create_message('ciaran.dunn@gmail.com', 'ciaran.dunn@gmail.com', 'String message from send2email', data)
        print(msg)
    if type == 'file':
        print('Sending file! {}'.format(data))
        msg = create_message_with_attachment(
            'ciaran.dunn@gmail.com', 'ciaran.dunn@gmail.com', 
            'File message from send2mail. Name is '.format(data), 'Find attached a file named'.format(data), 
            data)
    
    if msg:
        send_email(msg)


if __name__ == '__main__':
    main()
