# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:14:10 2016

@author: Shenghao
"""

import tkinter

class Cellphone_GUI:
    def __init__(self, main_window):
        self.frame0 = tkinter.Frame(main_window)
        self.frame1 = tkinter.Frame(main_window)
        self.frame2 = tkinter.Frame(main_window)
        self.frame3 = tkinter.Frame(main_window)
        self.frame4 = tkinter.Frame(main_window)
        self.frame5 = tkinter.Frame(main_window)
        self.frame6 = tkinter.Frame(main_window)
        self.space0 = tkinter.Frame(main_window, height=10)
        self.space1 = tkinter.Frame(main_window, height=10)
        self.space2 = tkinter.Frame(main_window, height=10)
        self.space3 = tkinter.Frame(main_window, height=10)
        self.space4 = tkinter.Frame(main_window, height=10)
        self.space5 = tkinter.Frame(main_window, height=10)
        self.__number = tkinter.StringVar()
        self.__txt = tkinter.StringVar()
        self.entry1 = tkinter.Label(self.frame0,
                                    textvariable=self.__txt,
                                    width=20,
                                    highlightbackground='white',
                                    height=1)
        self.entry2 = tkinter.Label(self.frame0,
                                    textvariable=self.__number,
                                    width=20,
                                    height=1)
        self.call = tkinter.Button(self.frame1,
                                   text='Call',
                                   width=7,
                                   command=self.calling)
        self.endcall = tkinter.Button(self.frame1,
                                      text='End',
                                      width=7,
                                      command=self.ending)
        self.num1 = tkinter.Button(self.frame2,
                                   text='1',
                                   width=4,
                                   command=self.n1)
        self.num2 = tkinter.Button(self.frame2,
                                   text='2',
                                   width=4,
                                   command=self.n2)
        self.num3 = tkinter.Button(self.frame2,
                                   text='3',
                                   width=4,
                                   command=self.n3)
        self.num4 = tkinter.Button(self.frame3,
                                   text='4',
                                   width=4,
                                   command=self.n4)
        self.num5 = tkinter.Button(self.frame3,
                                   text='5',
                                   width=4,
                                   command=self.n5)
        self.num6 = tkinter.Button(self.frame3,
                                   text='6',
                                   width=4,
                                   command=self.n6)
        self.num7 = tkinter.Button(self.frame4,
                                   text='7',
                                   width=4,
                                   command=self.n7)
        self.num8 = tkinter.Button(self.frame4,
                                   text='8',
                                   width=4,
                                   command=self.n8)
        self.num9 = tkinter.Button(self.frame4,
                                   text='9',
                                   width=4,
                                   command=self.n9)
        self.num0 = tkinter.Button(self.frame5,
                                   text='0',
                                   width=4,
                                   command=self.n0)
        self.num = ''
        self.status = False
        self.entry1.pack()
        self.entry2.pack()
        self.call.pack(side='left')
        self.endcall.pack(side='left')
        self.num1.pack(side='left')
        self.num2.pack(side='left')
        self.num3.pack(side='left')
        self.num4.pack(side='left')
        self.num5.pack(side='left')
        self.num6.pack(side='left')
        self.num7.pack(side='left')
        self.num8.pack(side='left')
        self.num9.pack(side='left')
        self.num0.pack(side='left')
        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

    def n1(self):
        self.num += '1'
        self.__number.set(self.num)

    def n2(self):
        self.num += '2'
        self.__number.set(self.num)

    def n3(self):
        self.num += '3'
        self.__number.set(self.num)

    def n4(self):
        self.num += '4'
        self.__number.set(self.num)

    def n5(self):
        self.num += '5'
        self.__number.set(self.num)

    def n6(self):
        self.num += '6'
        self.__number.set(self.num)

    def n7(self):
        self.num += '7'
        self.__number.set(self.num)

    def n8(self):
        self.num += '8'
        self.__number.set(self.num)

    def n9(self):
        self.num += '9'
        self.__number.set(self.num)

    def n0(self):
        self.num += '0'
        self.__number.set(self.num)

    def calling(self):
        import pickle
        self.__txt.set('Calling...')
        try:
            infile = open('contact.dat', 'rb')
            dic = pickle.load(infile)
            infile.close()
        except:
            dic = dict()
        c = 0
        a = []
        for i in dic.keys():
            if dic[i] == self.num:
                a.append(i)
                c += 1
        str = ''
        if c > 0:
            for i in range(len(a)):

                str += a[i] + '/'
            str = str[:-1] + ' '
        self.__number.set(str + self.num)
        self.status = True

    def ending(self):
        self.status = False
        self.num = 0
        self.__number.set('')
        self.__txt.set('')
