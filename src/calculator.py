import PySimpleGUI as sg
import logic as l

# pretty colors and sizing
bw  = {'size':(6,2) , 'font':('Ariel', 26), 'button_color':("#39aa14","#222222")}
bw2 = {'size':(13,2), 'font':('Ariel', 26), 'button_color':("#39aa14","#222222")}
bt  = {'size':(6,2) , 'font':('Ariel', 26), 'button_color':("#39aa14","#333333")}
bo  = {'size':(13,2), 'font':('Ariel', 26), 'button_color':("#39aa14","#111111"), 'focus':True}

# PySimpleGUI layout
layout = [
    [sg.Text('0', size=(20,1), justification='right', background_color='#111111', text_color='#39aa14', 
        font=('Digital',43), key="-OUT-")],
    [sg.Button('7',**bw) , sg.Button('8',**bw), sg.Button('9',**bw), sg.Button('C',**bt), sg.Button('DEL',**bt) ],
    [sg.Button('4',**bw) , sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("/",**bt), sg.Button("-",**bt)],
    [sg.Button('1',**bw) , sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("*",**bt), sg.Button("+",**bt)],    
    [sg.Button('0',**bw2), sg.Button('.',**bw), sg.Button('=',**bo)]
]

# create the PySimpleGUI window
window = sg.Window('Calculator', layout=layout, background_color="black",  return_keyboard_events=True)

# init loop of window
display = '0'
charSet = '1234567890=-/+*.'
while True:
    event, values = window.read()
    # print("VAL:",values)
    # print("EVENT:",event)

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