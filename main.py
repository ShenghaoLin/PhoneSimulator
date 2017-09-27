# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:14:10 2016

@author: Shenghao
"""

import tkinter
from Cellphone import Cellphone_GUI
from Contact import Contact_GUI
from Message import Message_GUI
from Group_Chat import Group_Chat


def main():
    def event0(event=None):
        global UI
        global t
        UI.quit()
        UI.main_window.after(500, UI.main_window.destroy)
        t = 1

    def event1(event=None):
        global UI
        global t
        UI.quit()
        UI.main_window.after(500, UI.main_window.destroy)
        t = 2

    def message_UI():
        global t
        global UI
        try:
            UI.destroy()
        except:
            pass
        t = 0
        UI = Message_GUI(num)
        UI.cellphone.bind('<Button-1>', event0)
        UI.group_chat.bind('<Button-1>', event1)
        UI.main_window.mainloop()
        if t == 1:
            cellphone_UI()
        if t == 2:
            group_chat_UI()

    def group_chat_UI():
        global UI
        global t
        t = 0
        UI = Group_Chat(num)
        UI.cellphone.bind('<Button-1>', event0)
        UI.message.bind('<Button-1>', event1)
        UI.main_window.mainloop()
        if t == 1:
            cellphone_UI()
        if t == 2:
            message_UI()

    def cellphone_UI():
        global UI
        try:
            UI.destroy()
        except:
            pass
        UI = tkinter.Tk()
        UI.title('Cellphone' + ': ' + num)
        topframe = tkinter.Frame(UI)
        contact = tkinter.Button(topframe,
                                 text='Contact',
                                 width=7,
                                 command=contact_UI)
        message = tkinter.Button(topframe,
                                 text='Message',
                                 width=7,
                                 command=message_UI)
        contact.pack(side='left')
        message.pack(side='left')
        topframe.pack()
        Cellphone_GUI(UI)
        UI.mainloop()

    def contact_UI():
        global UI
        try:
            UI.destroy()
        except:
            pass
        UI = tkinter.Tk()
        UI.title('Contacts' + ': ' + num)
        space = tkinter.Frame(UI,
                              height=10)
        topframe = tkinter.Frame(UI)
        cellphone = tkinter.Button(topframe,
                                   text='Back to Cellphone',
                                   command=cellphone_UI)
        cellphone.pack()
        space.pack(side='top')
        topframe.pack()
        Contact_GUI(UI)
        UI.mainloop()

    num = input('Please input your phone number: ')
    cellphone_UI()


main()
