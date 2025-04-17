import wx
from myPP.B.helper import get_message

def show_message_box():
    app = wx.App(False)
    message = get_message()
    wx.MessageBox(message, "MyPP Message", wx.OK | wx.ICON_INFORMATION)
    app.MainLoop()

if __name__ == "__main__":
    show_message_box()