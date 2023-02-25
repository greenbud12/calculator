def update_display(display, event):
    
    if event.isdigit():
        if display == '0':
            return event
        return display + event

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

        case "+/-":
            if display[-1].isdigit():
                display += '+'
                print("HIUIUH")

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
