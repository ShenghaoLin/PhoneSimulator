# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:30:27 2016

@author: Shenghao
"""

import pickle
import tkinter
import tkinter.messagebox

fname = 'contact.dat'


class Contact_GUI:
    def __init__(self,main_window):
        try:
            infile = open(fname, 'rb')
            infile.close()
        except:
            infile = open(fname, 'wb')
            d = dict()
            pickle.dump(d, infile)
            infile.close()
        finally:
            self.frame1 = tkinter.Frame(main_window)
            self.frame2 = tkinter.Frame(main_window)
            self.frame3 = tkinter.Frame(main_window)
            self.frame0 = tkinter.Frame(main_window)
            self.space0 = tkinter.Frame(main_window, height=20)
            self.space1 = tkinter.Frame(main_window, height=20)
            self.space2 = tkinter.Frame(main_window, height=20)
            self.space3 = tkinter.Frame(main_window, height=20)
            self.space4 = tkinter.Frame(main_window, height=20)
            self.label0 = tkinter.Label(self.frame0, text='Contact')
            self.label1 = tkinter.Label(self.frame1, text='    Name: ')
            self.label2 = tkinter.Label(self.frame2, text='Number: ')
            self.__name = tkinter.StringVar()
            self.entry1 = tkinter.Entry(self.frame1, textvariable=self.__name, width=20)
            self.__number = tkinter.StringVar()
            self.entry2 = tkinter.Entry(self.frame2, textvariable=self.__number, width=20)
            self.command1 = tkinter.Button(self.frame1, text='Delete', command=self.delete1)
            self.command3 = tkinter.Button(self.frame3, text='Add', command=self.add)
            self.command2 = tkinter.Button(self.frame1, text='Search', command=self.search1)
            self.command4 = tkinter.Button(self.frame2, text='Delete', command=self.delete2)
            self.command5 = tkinter.Button(self.frame2, text='Search', command=self.search2)
            self.command6 = tkinter.Button(self.frame3, text='Change', command=self.change)
            self.command7 = tkinter.Button(self.frame3, text='Show All', command=self.show_all)
            self.command8 = tkinter.Button(self.frame1, text='Fuzzy Search',
                                           command=self.fuzzy1)
            self.command9 = tkinter.Button(self.frame2, text='Fuzzy search',
                                           command=self.fuzzy2)
            self.label0.pack(side='top')
            self.label1.pack(side='left')
            self.entry1.pack(side='left')
            self.command1.pack(side='left')
            self.command2.pack(side='left')
            self.command8.pack(side='left')
            self.label2.pack(side='left')
            self.entry2.pack(side='left')
            self.command4.pack(side='left')
            self.command5.pack(side='left')
            self.command9.pack(side='left')
            self.command3.pack(side='left')
            self.command6.pack(side='left')
            self.command7.pack(side='left')
            self.space0.pack()
            self.frame0.pack()
            self.space1.pack()
            self.frame1.pack()
            self.space2.pack()
            self.frame2.pack()
            self.space3.pack()
            self.frame3.pack()
            self.space4.pack()

    def search1(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        name = self.entry1.get()
        if name in dic.keys():
            self.__number.set(dic[name])
        else:
            tkinter.messagebox.showinfo('Information',
                                        'The name does not exist in contacts.')
        infile.close()

    def search2(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        number = self.entry2.get()
        s = 0
        c = []
        for i in dic.keys():
            if dic[i] == number:
                s += 1
                c.append(i)
        if s == 0:
            tkinter.messagebox.showinfo('Information',
                                        'The number does not exist in contacts.')
        if s == 1:
            self.__name.set(c[0])
        if s > 1:
            st = ''
            for i in c:
                st = st + '\n' + i
            tkinter.messagebox.showinfo('Information',
                                        'The number exists in more than one contact:' + st)

    def add(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        name = self.entry1.get()
        number = self.entry2.get()
        if name in dic.keys():
            tkinter.messagebox.showinfo('Information',
                                        'The name exists in contacts.\n' + \
                                        'Name: ' + name + '\n' + \
                                        'Number: ' + dic[name] + '\n' + \
                                        'Try Change button.')
        else:
            temp = True
            for i in dic.keys():
                if number in dic[i]:
                    tkinter.messagebox.showinfo('Information',
                                                'The Number already existed in the following contact: '+ \
                                                '\n'+i)
                    temp = False
                    break
            if temp:
                dic[name] = number
                tkinter.messagebox.showinfo('Information',
                                            'Add successfully.')
        infile = open(fname, 'wb')
        pickle.dump(dic, infile)
        infile.close()

    def change(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        name = self.entry1.get()
        number = self.entry2.get()
        if name not in dic.keys():
            tkinter.messagebox.showinfo('Information',
                                        'The name does not exist in contacts.\n' + \
                                        'Try Add button.')
        else:
            dic[name] = number
            tkinter.messagebox.showinfo('Information',
                                        'Change successfully.')
        infile = open(fname, 'wb')
        pickle.dump(dic, infile)
        infile.close()

    def delete1(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        name = self.entry1.get()
        if name in dic.keys():
            dic.pop(name)
            tkinter.messagebox.showinfo('Information',
                                        'Delete successfully.')
        else:
            tkinter.messagebox.showinfo('Information',
                                        'This name does not exist in contacts.')
        infile = open(fname, 'wb')
        pickle.dump(dic, infile)
        infile.close()

    def delete2(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        number = self.entry2.get()
        k = False
        s = 0
        c = []
        for i in dic.keys():
            if dic[i] == number:
                c.append(i)
                k = True
                s = s + 1
        for i in c:
            dic.pop(i)
        st = ''
        for i in c:
            st = st + i + '\n'
        if k == False:
            tkinter.messagebox.showinfo('Information',
                                        'This number does not exist in contacts.')
        else:
            tkinter.messagebox.showinfo('Information',
                                        ('Delete %d contact(s) successfully' % s) + \
                                        '\n' + st)
        infile = open(fname, 'wb')
        pickle.dump(dic, infile)
        infile.close()

    def show_all(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        infile = open('Contacts.txt', 'w')
        for i in dic.keys():
            infile.write('Name: ' + i + '\n')
            infile.write('Number: ' + dic[i] + '\n\n')
        infile.close()
        tkinter.messagebox.showinfo('Information',
                                    'All contacts are imported to Contacts.txt.')

    def fuzzy1(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        name = self.__name.get()
        s = 0
        c = ''
        for i in dic.keys():
            if name in i:
                c = c + '\n' + 'Name: ' + i + '\n' + 'Number: ' + dic[i] + '\n'
                s += 1
        if s == 0:
            tkinter.messagebox.showinfo('Information',
                                        'No result.')
        else:
            tkinter.messagebox.showinfo('Information',
                                        'Searching result:\n' + c)

    def fuzzy2(self):
        infile = open(fname, 'rb')
        dic = pickle.load(infile)
        infile.close()
        number = self.__number.get()
        s = 0
        c = ''
        for i in dic.keys():
            if number in dic[i]:
                c = c + '\n' + 'Name: ' + i + '\n' + 'Number: ' + dic[i] + '\n'
                s += 1
        if s == 0:
            tkinter.messagebox.showinfo('Information',
                                        'No result.')
        else:
            tkinter.messagebox.showinfo('Information',
                                        'Searching result:\n' + c)