#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: logic.py
Description: Logic for the calculator program.
Author: Bailey Bakerson
Date: 2023-02-24
"""

def update_display(display, event):
    
    # performs operations if 0-9
    if event.isdigit():
        if display == '0':
            return event
        return display + event

    # performs ops for +-*/=.
    match event:
        case "+":
            if display[-1].isdigit():
                display += '+'
        case "-":
            if display[-1].isdigit():
                display += '-'
        case "*":
            if display[-1].isdigit():
                display += '*'
        case "/":
            if display[-1].isdigit():
                display += '/'

        case ".":
            if display[-1].isdigit() and '.' not in display.replace('*',' ')\
                .replace('/',' ').replace('+',' ').replace('-',' ').split()[-1]:
                    display += '.'

        case "=":
            try:
                display = str(eval(display))
            except ZeroDivisionError:
                display = "ERROR"

    return display
