import wx
import os


class MyTree(wx.TreeCtrl):
    def __init__(self, parent, id, position, size, style):
        wx.TreeCtrl.__init__(self, parent, id, position, size, style)

        self.refresh_tree()
    

    def refresh_tree(self):
        self.DeleteAllItems()

        root = self.AddRoot('Stuff')
        #self.SetPyData(root, ('key', 'value'))
        self.mods = self.AppendItem(root, 'Modules')

        modules = os.sys.modules
        for module in modules:
            new_item = self.AppendItem(self.mods, module)

            dir_result = dir(module)
            for dir_entry in dir_result:
                self.AppendItem(new_item, dir_entry)


class MainApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        #fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        # Create a splitter window
        self.splitter = wx.SplitterWindow(self, -1)

        # Create the left panel
        leftPanel = wx.Panel(self.splitter, -1)
        
        # Create a box sizer that will contain the left panel contents
        leftBox = wx.BoxSizer(wx.VERTICAL)

        # Create our tree and put it into the left panel
        self.tree = MyTree(leftPanel, 1, wx.DefaultPosition, (-1, -1),
                wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS)

        # Add the tree to the box sizer
        leftBox.Add(self.tree, 1, wx.EXPAND)

        # Bind the OnSelChanged method to the tree
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)

        # Set the size of the right panel to that required by the tree
        leftPanel.SetSizer(leftBox)

        # Create the right panel
        rightPanel = wx.Panel(self.splitter, -1)

        # Create the right box sizer that will contain the panel's contents
        rightBox = wx.BoxSizer(wx.VERTICAL)
        
        # Create a widget to display static text and store it in the right
        # panel
        self.display = wx.StaticText(rightPanel, -1, '', (10, 10),
                style=wx.ALIGN_LEFT)
        # Add the display widget to the right panel
        rightBox.Add(self.display, -1, wx.EXPAND)

        # Set the size of the right panel to that required by the
        # display widget
        rightPanel.SetSizer(rightBox)
        # Put the left and right panes into the split window
        self.splitter.SplitVertically(leftPanel, rightPanel)

        self.SetSize((800, 600))
        self.SetTitle('Object Explorer')
        
        # Create the window in the centre of the screen
        self.Centre()


    def OnSelChanged(self, event):
        '''Method called when selected item is changed.'''
        # Get the selected item object
        item =  event.GetItem()
        item_text = self.tree.GetItemText(item)

        mod = __import__(item_text)
        document = mod.__doc__

        #print(document)

        # Display the selected item text in the text widget
        self.display.SetLabel(document)


    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = MainApp(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
