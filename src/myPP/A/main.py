import wx, sys
from myPP.B.helper import get_message

def show_message_box():
    message = get_message()
    msg=f"{message} \nsys.argv:{sys.argv}"
    app = wx.App(False)
    wx.MessageBox(msg, f"MyPP Message", wx.OK | wx.ICON_INFORMATION)
    app.MainLoop()

if __name__ == "__main__":
    print('main.py has been called')
    show_message_box()