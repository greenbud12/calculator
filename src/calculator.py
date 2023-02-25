#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: calculator.py
Description: A simple calculator program with a graphical user interface.
Author: Bailey Bakerson
Date: 2023-02-24
"""

import PySimpleGUI as sg
import logic as l

# pretty colors and sizing
bg  = {'size':(6,2) , 'font':('Ariel', 26), 'button_color':("#39aa14","#222222")}
bg2 = {'size':(13,2), 'font':('Ariel', 26), 'button_color':("#39aa14","#222222")}
bg3  = {'size':(6,2) , 'font':('Ariel', 26), 'button_color':("#39aa14","#333333")}
bg4  = {'size':(13,2), 'font':('Ariel', 26), 'button_color':("#39aa14","#111111"), 'focus':True}

# PySimpleGUI layout
layout = [
    [sg.Text('0', size=(20,1), justification='right', background_color='#111111', text_color='#39aa14', 
        font=('Digital',43), key="-OUT-")],
    [sg.Button('7',**bg) , sg.Button('8',**bg), sg.Button('9',**bg), sg.Button('C',**bg3), sg.Button('DEL',**bg3)],
    [sg.Button('4',**bg) , sg.Button('5',**bg), sg.Button('6',**bg), sg.Button("/",**bg3), sg.Button("-",**bg3)],
    [sg.Button('1',**bg) , sg.Button('2',**bg), sg.Button('3',**bg), sg.Button("*",**bg3), sg.Button("+",**bg3)],    
    [sg.Button('0',**bg2), sg.Button('.',**bg), sg.Button('=',**bg4)]
]

# create the PySimpleGUI window
window = sg.Window('Calculator', layout=layout, background_color="black",  return_keyboard_events=True)

# init loop of window
display = '0'
charSet = '1234567890=-/+*.'
while True:
    event, values = window.read()

    # stop is closing
    if sg.WINDOW_CLOSED or event is None:
            break
    
    # delete key
    elif event == 'DEL':
        if len(display) != 1:
            display = display[:-1]
        else:
            display = '0'

    # clear key
    elif event == 'C':
        display = '0'

    # all other keys
    elif event in charSet:
        display = l.update_display(display, event)
    
    # update display
    window['-OUT-'].update(display)          

window.close()