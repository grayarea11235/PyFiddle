from __future__ import print_function

import pickle
import os.path
import pprint
import cmd2

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from prettytable import PrettyTable

from tkinter import *

# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtPrintSupport import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = [ 'https://www.googleapis.com/auth/drive.metadata.readonly', ]
global service
global cwd

class FileObject:
    pass


class GDriveFS:
    pass


# Get the file files details from a object
def gd_get_file_details(service, parent_id, file_name):
    results = service.files().list(
        q="""
        'root' in parents and trashed=false and
        name = '{0}'
        """.format(file_name),
        fields="files").execute()

    files = results['files']
    ret_file = files[0]

    print(ret_file.get('name'))
    print(ret_file.get('description'))
    print(ret_file.get('fileExtension'))
    print(ret_file.get('size'))

    return results['files']


# Return a list of objects in a 'path'
def gd_ls(location, service):
    # Take the location apart
    split_location = list(filter(lambda a: a != '', location.split('/')))

    # We start with root and look for the first item
    print(len(split_location))
    if len(split_location) == 0:
        # We are just getting root
        results = service.files().list(
            q="'root' in parents and trashed=false",
            fields="files").execute()

    return results

        #pp = pprint.PrettyPrinter(indent=2)
        #pp.pprint(results)



    # # Path is relative to gd root
    # results = service.files().list(
    #     q="mimeType='application/vnd.google-apps.folder' and 'root' in parents and trashed=false",
    #     fields="files").execute()

    # items = results.get('files', [])
    

def init_service():
    """
    Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=5555)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    return service
    

def main():
    service = init_service()
    
    # Call the Drive v3 API
    results = service.files().list(
#        pageSize=100,
#       q="mimeType = 'application/vnd.google-apps.folder'",
#       q="mimeType='application/vnd.google-apps.folder' and 'root' in parents and trashed=false",

        #         mimeType='application/vnd.google-apps.folder' and

        # 0Bw4jP0ph1yloZWJkNnJyWXIxYTg - root/Pets
        #
        # 1AoxncDPoVJOlL8pw6ejdG1A8oO0XOJ9j - root/Courses
        # 1Ot0WC7GZ3zyeXJ4hFVDscDxeItdyLRN0 - root/Courses/MachineLearning
        q="""
        '0Bw4jP0ph1yloZWJkNnJyWXIxYTg' in parents and
        trashed=false
        """,
        fields="files").execute()
#    fields="nextPageToken, files(id, name, kind)").execute()

    items = results.get('files', [])

#    pp = pprint.PrettyPrinter(indent=2)
#    pp.pprint(items[0])


    if not items:
        print('No files found.')
    else:
        #print('Files:')

        x = PrettyTable()
        x.field_names = [ "File name", "ID", "mimeType", "Size", ]
        
        for item in items:
            print(u'{0} {1} {2}'.format(item['name'], item['parents'], item['id']))

#             parents = service.parents().list(fileId=file_id).execute()
            name = item['name']
            size = 0
            if 'size' in item:
                size = item['size']
            id = item['id']
            mimeType = item['mimeType']

            x.align["File name"] = "l"
            x.align["ID"] = "l"
            x.align["mimeType"] = "l"
            x.align["Size"] = "l"
            
            x.add_row([name, id, mimeType, size])

#            print(u'{0}\t\t{1}'.format(name, mimeType))
            
        print(x)
            
            # if item['mimeType'] == 'application/vnd.google-apps.folder' || :
            #     print(u'{0}'.format(item['name']))
            # else:
            #     if item['mimeType'] == 'application/vnd.google-apps.document':
            #         print(u'{0}'.format(item['name']))
            #     else:
            #         print(u'{0} - {1}'.format(item['name'], item['size']))
            # # print(u'{0} ({1}) ({2})'.format(item['name'], item['id'], item['kind']))

    gd_ls('/', service)
    gd_ls('/Devel/', service)
    gd_ls('/Devel/C', service)
    # gd_ls('/Devel/cpp/', service)
    # gd_ls('/aaa', service)
    

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item {0}: "{1}"'.format(index, value))
    gd_get_file_details(service, 'root', value)


def simple_gui():
    cwed = 'root'

    res = gd_ls('/', service)
    files = res['files']
    
    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(files)

    for f in files:
        print(f['name'])

    # Simple little app
    mw = Tk()
    mw.geometry("800x600") 
    
    back = Frame(master=mw, width=800, height=600, bg='black')
    back.pack()
    
    filesListbox = Listbox(back, width=100, height=15)
    filesListbox.bind('<<ListboxSelect>>', onselect)
#    filesListbox.grid(sticky=W)

    for f in files:
        filesListbox.insert(END, f['name'])

    detailsListbox = Listbox(back, width=100, height=15)
#    detailsListbox.grid(sticky=E)

    filesListbox.pack()
    detailsListbox.pack()
        
    mainloop()

class CmdLineApp(cmd2.Cmd):
    def __init__(self):
        self.cwd = '/'

    def do_pwd(self, args):
        pass
    
#
# Main
#
if __name__ == '__main__':
    #main()

    service = init_service()
    simple_gui()

    # import sys
    # c = CmdLineApp()
    # sys.exit(c.cmdloop())
