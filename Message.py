# -*- coding: utf-8 -*-
"""
Created on Tue March 1 13:13:01 2016

@author: Shenghao
"""

import tkinter
import pickle
import tkinter.messagebox
import time


class Message_GUI:
    def __init__(self, me):
        try:
            infile = open('message.dat', 'rb')
            self.oldmessage = pickle.load(infile)
            infile.close()
        except:
            self.oldmessage = {}
        self.main_window = tkinter.Tk()
        self.main_window.title('Message: '+me)
        self.topframe = tkinter.Frame(self.main_window)
        self.cellphone = tkinter.Button(self.topframe,
                                        text='Back to Cellphone')
        self.group_chat = tkinter.Button(self.topframe,
                                         text='Group Chat')
        self.cellphone.pack(side='right')
        self.group_chat.pack()
        self.topframe.grid(column=1, row=0)
        self.running = True
        self.newmessage = True
        self.__toward = ''
        self.messageshowing = False
        self.__me = me
        self.messageframe = tkinter.Frame(self.main_window)
        self.frame0 = tkinter.Frame(self.messageframe)
        self.frame1 = tkinter.Frame(self.messageframe)
        self.frame2 = tkinter.Frame(self.messageframe)
        self.frame3 = tkinter.Frame(self.main_window)
        self.messagelist = tkinter.Listbox(self.frame3, height=21)
        self.messagelist.bind('<Double-Button-1>', self.select)
        self.make_list()
        self.text = tkinter.Text(self.frame1,
                                 width=42,
                                 height=20)
        self.toward = tkinter.Entry(self.frame0,
                                    width=17)
        self.delete_button = tkinter.Button(self.frame0,
                                            width=5,
                                            text='Delete',
                                            command=self.delete)
        self.sending_text = tkinter.Entry(self.frame2,
                                          width=25)
        self.send_button = tkinter.Button(self.frame2,
                                          width=5,
                                          text='Send',
                                          command=self.send)
        self.toward_button = tkinter.Button(self.frame0,
                                            width=5,
                                            text='Toward',
                                            command=self.to)
        self.toward_button.pack(side='left')
        self.toward.pack(side='left')
        self.delete_button.pack(side='left')
        self.text.pack()
        self.sending_text.pack(side='left')
        self.send_button.pack(side='left')
        self.messagelist.pack(side='top')
        self.frame3.grid(row=1, column=0)
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.messageframe.grid(row=1, column=1)
        self.message_update()

    def make_list(self):
        try:
            infile1 = open('message.dat', 'rb')
            dic1 = pickle.load(infile1)
            infile1.close()
        except:
            dic1 = {}
        try:
            infile2 = open('contact.dat', 'rb')
            dic2 = pickle.load(infile2)
            infile2.close()
        except:
            dic2 = {}
        self.messagelist.delete(0, tkinter.END)
        dic = sorted(dic1.items(), key=lambda d: d[1][-1][1], reverse=True)
        for i in range(len(dic)):
            if self.__me in dic[i][0]:
                temp = self.ds(dic[i][0], self.__me)
                if temp.startswith('--') or temp.endswith('--'):
                    temp = temp.replace('--', '')
                    tt = True
                    for j in dic2.keys():
                        if dic2[j] == temp:
                            self.messagelist.insert(tkinter.END, j + '(' + temp + ')')
                            tt = False
                            break
                    if tt:
                        self.messagelist.insert(tkinter.END, temp)

    def select(self, event=None):
        for i in self.messagelist.curselection():
            self.__toward = self.messagelist.get(i)
        temp = ''
        if self.__toward.isdigit():
            self.status = False
        else:
            self.status = True
        for i in range(len(self.__toward)):
            if self.__toward[i].isdigit():
                temp += self.__toward[i]
        self.toward.delete(0, tkinter.END)
        self.toward.insert(tkinter.END, self.__toward)
        self.__toward = temp
        if self.status:
            infile = open('contact.dat', 'rb')
            dic = pickle.load(infile)
            infile.close()
            for i in dic.keys():
                if dic[i] == self.__toward:
                    self.__name = i
                    break
        self.show_text()

    def send(self):
        if self.__toward == '':
            tkinter.messagebox.showinfo('Information',
                                        'Please enter the number first!')
        else:
            try:
                infile = open('message.dat', 'rb')
                con = pickle.load(infile)
                infile.close()
            except:
                con = dict()
            current = time.time()
            self.newmessage = False
            if (self.__me + '--' + self.__toward in con.keys()) or (self.__toward + '--' + self.__me in con.keys()):
                if self.__me + '--' + self.__toward in con.keys():
                    k = self.__me + '--' + self.__toward
                else:
                    k = self.__toward + '--' + self.__me
                temp = self.sending_text.get()
                self.sending_text.delete(0, last=tkinter.END)
                con[k].append([self.__me, current, temp])
                infile = open('message.dat', 'wb')
                pickle.dump(con, infile)
                infile.close()
                self.show_text()
                self.make_list()
            else:
                con[self.__me + '--' + self.__toward] = []
                temp = self.sending_text.get()
                self.sending_text.delete(0, last=tkinter.END)
                con[self.__me + '--' + self.__toward].append([self.__me, current, temp])
                infile = open('message.dat', 'wb')
                pickle.dump(con, infile)
                infile.close()
                self.show_text()
                self.make_list()

    def to(self):
        self.status = False
        self.__name = ''
        self.__toward = self.toward.get()
        if self.__toward.isdigit():
            try:
                infile = open('contact.dat', 'rb')
                dic = pickle.load(infile)
                infile.close()
                for i in dic.keys():
                    if self.__toward == dic[i]:
                        self.status = True
                        self.__name = i
                        self.toward.delete(0, tkinter.END)
                        self.toward.insert(tkinter.END, i + '(' + self.__toward + ')')
                        break
                self.show_text()
            except:
                pass
        else:
            try:
                infile = open('contact.dat', 'rb')
                dic = pickle.load(infile)
                infile.close()
                if self.__toward in dic.keys():
                    self.status = True
                    self.toward.delete(0, tkinter.END)
                    self.toward.insert(tkinter.END, self.__toward + '(' + dic[self.__toward] + ')')
                    self.__name = self.__toward
                    self.__toward = dic[self.__toward]
                    self.show_text()
                else:
                    tkinter.messagebox.showinfo('Information',
                                                'This contact does not exist.')
            except:
                tkinter.messagebox.showinfo('Information',
                                            'This contact does not exist.')

    def show_text(self):
        try:
            infile = open('message.dat', 'rb')
            con = pickle.load(infile)
            infile.close()
        except:
            con = dict()
        self.messageshowing = True
        self.text.delete(1.0, tkinter.END)
        if (self.__me + '--' + self.__toward in con.keys()) or (self.__toward + '--' + self.__me in con.keys()):
            if self.__me + '--' + self.__toward in con.keys():
                k = self.__me + '--' + self.__toward
            else:
                k = self.__toward + '--' + self.__me
            for i in range(len(con[k])):
                if con[k][i][0] == self.__me:
                    self.text.insert(tkinter.END, 'Me' + ' ' +
                                     time.strftime('%Y-%m-%d %X', time.localtime(con[k][i][1])) + ': ' + '\n')
                    self.text.insert(tkinter.END, con[k][i][2] + '\n\n')
                if con[k][i][0] == self.__toward:
                    if self.status:
                        self.text.insert(tkinter.END, self.__name + ' ' +
                                         time.strftime('%Y-%m-%d %X', time.localtime(con[k][i][1])) + ': ' + '\n')
                        self.text.insert(tkinter.END, con[k][i][2] + '\n\n')
                    else:
                        self.text.insert(tkinter.END, self.__toward + ' ' +
                                         time.strftime('%Y-%m-%d %X', time.localtime(con[k][i][1])) + ': ' + '\n')
                        self.text.insert(tkinter.END, con[k][i][2] + '\n\n')

    def message_update(self):
        if self.running:
            self.update()
            self.main_window.after(500, self.message_update)

    def update(self):
        try:
            infile2 = open('contact.dat', 'rb')
            con = pickle.load(infile2)
            infile2.close()
        except:
            con = {}
        try:
            infile = open('message.dat', 'rb')
            temp = pickle.load(infile)
            infile.close()
        except:
            temp = {}
        if self.newmessage:
            if temp != self.oldmessage:
                for i in temp.keys():
                    if i in self.oldmessage.keys():
                        if temp[i] != self.oldmessage[i] and temp[i][-1][0] != self.__toward and self.__me in i:
                            if self.ds(i, self.__me).startswith('--') or self.ds(i, self.__me).endswith('--'):
                                num = temp[i][-1][0]
                                for j in con.keys():
                                    if con[j] == num:
                                        num = j
                                        break
                                tkinter.messagebox.showinfo('Information',
                                                            'You have a new message from ' + num)
                    else:
                        if (self.__me in i) and \
                                (self.ds(i, self.__me).startswith('--') or self.ds(i, self.__me).endswith('--')):
                            num = temp[i][-1][0]
                            for j in con.keys():
                                if con[j] == num:
                                    num = j
                                    break
                            tkinter.messagebox.showinfo('Information',
                                                        'You have a new message from ' + num)
                self.oldmessage = temp
        else:
            self.newmessage = True
            self.oldmessage = temp
        self.make_list()
        if self.messageshowing:
            self.show_text()

    def delete(self):
        try:
            infile = open('message.dat', 'rb')
            dic = pickle.load(infile)
            infile.close()
        except:
            dic = {}
        if self.messageshowing == False:
            tkinter.messagebox.showinfo('Information',
                                        'Please select a contact first!')
        else:
            if (self.__me + '--' + self.__toward in dic.keys()) or (self.__toward + '--' + self.__me in dic.keys()):
                if self.__me + '--' + self.__toward in dic.keys():
                    k = self.__me + '--' + self.__toward
                else:
                    k = self.__toward + '--' + self.__me
                del dic[k]
            infile = open('message.dat', 'wb')
            pickle.dump(dic, infile)
            infile.close()
        self.messageshowing = False
        self.text.delete(0.0, tkinter.END)
        self.toward.delete(0, tkinter.END)
        self.newmessage = False

    def quit(self):
        self.running = False

    def ds(self, a, b):
        k = 0
        i = 0
        s = 0
        e = 0
        j = False
        while k < len(a):
            if a[k] == b[i]:
                if i == 0:
                    s = k
                if i == len(b)-1:
                    e = k
                    j = True
                    break
                i += 1
            else:
                i = 0
            k += 1
        if j:
            if s == 0:
                return a[(e+1):]
            else:
                return a[:s]
        else:
            return a
