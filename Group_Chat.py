# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:46:10 2016

@author: Shenghao
"""

import tkinter
import tkinter.messagebox
import pickle
import time


class Group_Chat:
    def __init__(self, me):
        self.main_window = tkinter.Tk()
        self.topframe = tkinter.Frame(self.main_window)
        self.cellphone = tkinter.Button(self.topframe,
                                   text='Back to Cellphone')
        self.message = tkinter.Button(self.topframe,
                                 text='Message')
        self.cellphone.pack(side='right')
        self.message.pack()
        self.topframe.grid(column=1,row=0)
        self.main_window.title('Group chat'+': '+me)
        self.running =True
        self.__toward = ''
        self.messageshowing = False
        self.__me = me
        self.messageframe = tkinter.Frame(self.main_window)
        self.listframe = tkinter.Frame(self.main_window)
        self.frame0 = tkinter.Frame(self.messageframe)
        self.frame1 = tkinter.Frame(self.messageframe)
        self.frame2 = tkinter.Frame(self.messageframe)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.frame3)
        self.frame5 = tkinter.Frame(self.messageframe)
        self.createname = tkinter.Entry(self.frame4,
                                        width=11)
        self.create_button = tkinter.Button(self.frame4,
                                            width=4,
                                            text='Create',
                                            command=self.create)
        self.messagelist = tkinter.Listbox(self.frame3, height=21, width=19)
        self.messagelist.bind('<Double-Button-1>', self.select)
        self.text = tkinter.Text(self.frame1,
                                 width=42,
                                 height=20)
        self.add_text = tkinter.Entry(self.frame5,
                                      width=32)
        self.delete_button = tkinter.Button(self.frame0,
                                            width=4,
                                            text='Delete',
                                            command=self.delete)
        self.deletegroup_button = tkinter.Button(self.frame0,
                                                width=8,
                                                text='Delete Group',
                                                command=self.deletegroup)
        self.buttontext = tkinter.StringVar()
        self.buttontext.set('Members')
        self.membershowing = False
        self.showall_button = tkinter.Button(self.frame0,
                                             width=6,
                                             textvariable=self.buttontext,
                                             command=self.show__member)
        self.sending_text = tkinter.Entry(self.frame2,
                                          width=25)
        self.send_button = tkinter.Button(self.frame2,
                                          width=5,
                                          text='Send',
                                          command=self.send)
        self.add_button = tkinter.Button(self.frame0,
                                         width=3,
                                         text='Add',
                                         command=self.add)
        self.add_text.pack()
        self.showall_button.pack(side='left')
        self.add_button.pack(side='left')
        self.delete_button.pack(side='left')
        self.deletegroup_button.pack(side='left')
        self.createname.pack(side='left')
        self.create_button.pack(side='left')
        self.frame4.pack(side='top')
        self.add_text.pack(side='left')
        self.delete_button.pack(side='left')
        self.text.pack()
        self.sending_text.pack(side='left')
        self.send_button.pack(side='left')
        self.messagelist.pack(side='top')
        self.frame3.grid(row=1, column=0)
        self.frame5.pack()
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.messageframe.grid(row=1, column=1)
        self.message_update()

    def quit(self):
        self.running = False

    def show__member(self):
        if self.membershowing:
            self.membershowing = False
            self.buttontext.set('Members')
            self.show_text()
        else:
            if self.messageshowing:
                self.membershowing = True
                self.buttontext.set('Messages')
                self.text.delete(0.0, tkinter.END)
                self.text.insert(tkinter.END, 'Group: ' + self.__toward + '\n\n')
                infile = open('groupchat.dat', 'rb')
                ch = pickle.load(infile)
                infile.close()
                for i in range(len(ch[self.__toward][0])):
                    self.text.insert(tkinter.END, ch[self.__toward][0][i]+'\n')
            else:
                tkinter.messagebox.showinfo('Information',
                                            'Please choose a group first.')

    def message_update(self):
        try:
            infile = open('groupchat.dat', 'rb')
            ch = pickle.load(infile)
            infile.close()
        except:
            ch = {}
        ch = sorted(ch.items(), key=lambda d: d[1][1][-1][1], reverse=True)
        self.messagelist.delete(0, tkinter.END)
        for i in range(len(ch)):
            if self.__me in ch[i][1][0]:
                self.messagelist.insert(tkinter.END, ch[i][0]+'('+str(len(ch[i][1][0]))+')')
        if self.messageshowing and not self.membershowing:
            self.show_text()
        if self.running:
            self.main_window.after(500, self.message_update)

    def send(self):
        if self.messageshowing:
            infile = open('groupchat.dat', 'rb')
            dic = pickle.load(infile)
            infile.close()
            dic[self.__toward][1].append([self.__me, time.time(), self.sending_text.get()])
            infile = open('groupchat.dat', 'wb')
            pickle.dump(dic, infile)
            infile.close()
        else:
            tkinter.messagebox.showinfo('Information',
                                        'Please choose a group first.')
        self.sending_text.delete(0, tkinter.END)

    def select(self, event):
        self.membershowing = False
        self.buttontext.set('Members')
        for i in self.messagelist.curselection():
            self.__toward = self.messagelist.get(i)
        if self.__toward != '':
            k = -1
            while self.__toward[k] != '(' and abs(k) < len(self.__toward):
                k -= 1
            self.__toward = self.__toward[:k]
            self.messageshowing = True

    def create(self):
        try:
            infile = open('groupchat.dat', 'rb')
            ch = pickle.load(infile)
            infile.close()
        except:
            ch = {}
        temp = self.createname.get()
        b = False
        if temp in ch.keys():
            b = True
        if b:
            tkinter.messagebox.showinfo('Information',
                                        'This group already exists.')
        else:
            ch[temp] = [[self.__me], [['', time.time(), '']]]
            infile = open('groupchat.dat', 'wb')
            pickle.dump(ch, infile)
            infile.close()
            self.__toward = temp
            self.messageshowing = True

    def add(self):
        if self.messageshowing:
            status = True
            adding = self.add_text.get()
            if not (adding.isdigit()):
                status = False
                try:
                    infile = open('contact.dat', 'rb')
                    dic = pickle.load(infile)
                    infile.close()
                    if adding in dic.keys():
                        status = True
                        adding = dic[adding]
                    else:
                        tkinter.messagebox.showinfo('Information',
                                                    'This contact does not exist.')
                except:
                    tkinter.messagebox.showinfo('Information',
                                                'This contact does not exist.')
            if status:
                infile = open('groupchat.dat', 'rb')
                ch = pickle.load(infile)
                infile.close()
                if adding in ch[self.__toward][0]:
                    tkinter.messagebox.showinfo('Information',
                                                        'This contact is already in the group.')
                else:
                    ch[self.__toward][0].append(adding)
                infile = open('groupchat.dat', 'wb')
                pickle.dump(ch, infile)
                infile.close()
                if self.membershowing:
                    self.text.delete(0.0, tkinter.END)
                    for i in range(len(ch[self.__toward][0])):
                        self.text.insert(tkinter.END, ch[self.__toward][0][i]+'\n')
        else:
            tkinter.messagebox.showinfo('Information',
                                        'Please select or create a group first.')


    def show_text(self):
        infile = open('groupchat.dat', 'rb')
        ch = pickle.load(infile)
        infile.close()
        try:
            infile = open('contact.dat', 'rb')
            dic = pickle.load(infile)
            infile.close()
        except:
            dic = {}
        if self.__toward not in ch.keys():
            return
        self.messageshowing = True
        self.text.delete(0.0, tkinter.END)
        self.text.insert(tkinter.END, 'Group: ' + self.__toward + '\n\n')
        for j in range(1, len(ch[self.__toward][1])):
            if ch[self.__toward][1][j][0] == self.__me:
                self.text.insert(tkinter.END, 'Me' + ' ' +
                                 time.strftime('%Y-%m-%d %X', time.localtime(ch[self.__toward][1][j][1]))
                                 + ':' + '\n')
                self.text.insert(tkinter.END, ch[self.__toward][1][j][2] + '\n')
            else:
                self.text.insert(tkinter.END, ch[self.__toward][1][j][0] + ' ' +
                                 time.strftime('%Y-%m-%d %X', time.localtime(ch[self.__toward][1][j][1]))
                                 + ':' + '\n')
                self.text.insert(tkinter.END, ch[self.__toward][1][j][2] + '\n')

    def delete(self):
        if self.messageshowing:
            status = True
            adding = self.add_text.get()
            if not (adding.isdigit()):
                status = False
                try:
                    infile = open('contact.dat', 'rb')
                    dic = pickle.load(infile)
                    infile.close()
                    if adding in dic.keys():
                        status = True
                        adding = dic[adding]
                    else:
                        tkinter.messagebox.showinfo('Information',
                                                    'This contact does not exist.')
                except:
                    tkinter.messagebox.showinfo('Information',
                                                'This contact does not exist.')
            infile = open('groupchat.dat', 'rb')
            ch = pickle.load(infile)
            infile.close()
            if adding in ch[self.__toward][0]:
                if self.__me == adding:
                    del ch[self.__toward][0][ch[self.__toward][0].index(adding)]
                    self.messageshowing = False
                    self.text.delete(0.0, tkinter.END)
                elif self.__me == ch[self.__toward][0][0]:
                    del ch[self.__toward][0][ch[self.__toward][0].index(adding)]
                    if self.membershowing:
                        self.text.delete(0.0, tkinter.END)
                        for i in range(len(ch[self.__toward][0])):
                            self.text.insert(tkinter.END, ch[self.__toward][0][i]+'\n')
                else:
                    tkinter.messagebox.showinfo('Information',
                                                'You do not have the access to this action.')
            else:
                tkinter.messagebox.showinfo('Information',
                                            'The contact does not exist in the group.')
            infile = open('groupchat.dat', 'wb')
            pickle.dump(ch, infile)
            infile.close()

    def deletegroup(self):
        if self.messageshowing:
            infile = open('groupchat.dat', 'rb')
            ch = pickle.load(infile)
            infile.close()
            if self.__me == ch[self.__toward][0][0]:
                del ch[self.__toward]
                self.messageshowing = False
                self.text.delete(0.0, tkinter.END)
                self.membershowing = False
                self.buttontext.set('Members')
                infile = open('groupchat.dat', 'wb')
                pickle.dump(ch, infile)
                infile.close()
            else:
                tkinter.messagebox.showinfo('Information',
                                            'You do not have the access to this action.'+'\n'
                                            + 'If you want to quit the group, please delete yourself.')