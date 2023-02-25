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

        case "-/+":
            # check if number
            if display[-1].isdigit():
                # find negate location
                i = len(display)-1 
                while i >= 0:
                    # find the seperator for the first numeber
                    # avoid the case of 3.3 -> 3.-3
                    if not display[i].isdigit() and display[i] != '.':
                        i -= 1
                        break
                    i -= 1
                    
                    # No ops, only the one number
                    if i == -1:
                        return '-'+display

                # Make sure not just an empty list
                if i != -1:
                    # move index back to detected non-digit
                    i += 1
                    # replace or delete depending
                    if display[i] == '-':
                        return display[:i] + '+' + display[i+1:]
                    elif display[i] == '+':
                        return display[:i] + '-' + display[i+1:]
                    else:
                        return display[:i+1] + '-' + display[i+1:]
                else:
                    return display[1:]


        case ".":
            if display[-1].isdigit() and '.' not in display.replace('*',' ')\
                .replace('/',' ').replace('+',' ').replace('-',' ').split()[-1]:
                    display += '.'

        case "=":
            try:
                display = str(eval(display))
            except ZeroDivisionError:
                display = "ERROR"

    # convert to scientific notation
    # if len(display) > 10:
    #     if '.' in display:
    #         display = "{:e}".format(float(display))
    #     else:
    #         display = "{:e}".format(int(display))
    

    return display
