import wx
class OmataPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="FEEDBACK", pos=(20, 30))
        self.logger = wx.TextCtrl(self, pos=(20,50), size=(300,300), style=wx.TE_MULTILINE )


  

app = wx.App(False)
frame = wx.Frame(None)
panel = OmataPanel(frame)
frame.Show()
app.MainLoop()
