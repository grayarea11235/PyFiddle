import wx

class MainApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((640, 480))
        self.SetTitle('Template Application')
        self.Centre()


    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = MainApp(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
