# Дао Ань Туан, ИУ7-24Б

import tkinter as tk
import logic as lg
from tkinter import messagebox as msg
# from tkinter import ttk


root = tk.Tk()
root.title('Calculator')
root.geometry('600x600')

menubar = tk.Menu(root)


def entryCalculation():
    try:
        current_val = enterZone.get()
        res = lg.calculate(enterZone.get())
        #state = numsys.get()
        '''if state == 'DEC':
            enterZone.delete(0, tk.END)
            enterZone.insert(tk.END, str(res))
        else:
            binNum = lg.toBinary(res)
            enterZone.delete(0, tk.END)
            enterZone.insert(tk.END, str(binNum))'''
        enterZone.delete(0, tk.END)
        enterZone.insert(tk.END, str(res))
        if not res:
            enterZone.delete(0, tk.END)
            enterZone.insert(tk.END, str(current_val))
    except ValueError:
        msg.showerror('ValueError', 'Please type the right numerical expression')


#click = 0
def personalInfo():
    msg.showinfo('About project', 
                 'Author: Dao Anh Tuan\nThe following program was made to calculate floating point numbers in the binary numerical system')

def insertOperator(operator):
    value = enterZone.get()
    length = len(value)
    if ('+' in value or '*' in value or '-' in value) and value[0] not in '*-+' \
    and value[-1] not in ' *-+':
        entryCalculation()
    if length > 0:
        if value[length-1] not in '+*-':
            enterZone.insert(tk.END, operator)
    else: pass



def key_handler(event):
    if event.char in '+-*':
        insertOperator(event.char)
    elif event.char == '=':
        entryCalculation()

root.bind('<Key>', key_handler)

    

def insert_number(num):
    #current_system = numsys.get()
    #if current_system == 'BIN' and num > 1:
    if not (0 <= num <= 1):
        msg.showwarning('Invalid Input', 'Only 0 and 1 are allowed in binary mode')
        return
    enterZone.insert(tk.END, str(num))

def restrict_nums(event):
    RESTRICT = 'qwertyuiopasdfghjklzxcvbnm23456789'
    #current_system = numsys.get()
    state = None
    #if current_system == 'BIN':
    if event.char.lower() in RESTRICT:
        state = 'break'
    return state


file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Menu', menu = file)
file.add_command(label='About project', command=personalInfo)
root.config(menu = menubar)

font = ('Arial', 20)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.columnconfigure(0, weight=1)

topFrame = tk.Frame(root, bg='blue')
topFrame.grid(row=0, column=0, sticky='nsew')
bottomFrame = tk.Frame(root, bg='lightblue')
bottomFrame.grid(row=1, column=0, sticky='nsew')
enterZone = tk.Entry(topFrame, bg='white', font=font, justify='left')
enterZone.pack(fill='both', expand=True) 
enterZone.bind('<Key>', restrict_nums)


bottomFrame.rowconfigure(0, weight=1)
bottomFrame.rowconfigure(1, weight=1)
bottomFrame.rowconfigure(2, weight=1)
bottomFrame.rowconfigure(3, weight=1)

bottomFrame.columnconfigure(0, weight=1)
bottomFrame.columnconfigure(1, weight=1)
bottomFrame.columnconfigure(2, weight=1)
bottomFrame.columnconfigure(3, weight=1)
bottomFrame.columnconfigure(4, weight=1)


buttons = []
k = 0
for row in range(2):
    for col in range(5):
        btn = tk.Button(bottomFrame, text=f'{k}', command=lambda num=k: insert_number(num))
        btn.grid(row=row, column=col, sticky='nsew')
        buttons.append(btn)
        k += 1


multBtn = tk.Button(bottomFrame, text='x', font=font, command=lambda: insertOperator('*'))
additionBtn = tk.Button(bottomFrame, text='+', font=font, command=lambda: insertOperator('+'))
decrementBtn = tk.Button(bottomFrame, text='-', font=font, command=lambda: insertOperator('-'))
equalBtn = tk.Button(bottomFrame, text='=', font=font, command=entryCalculation)
clearBtn = tk.Button(bottomFrame, text='CE', font=font, command=lambda: enterZone.delete(0, tk.END))
delSymbolBtn = tk.Button(bottomFrame, text='<', font=font, command=lambda: enterZone.delete(len(enterZone.get())-1, tk.END))
dotBtn = tk.Button(bottomFrame, text='.', font=font, command=lambda: enterZone.insert(tk.END, '.'))


'''
numsys = tk.StringVar()
numSysselection = ttk.Combobox(bottomFrame, textvariable=numsys)
numSysselection.set('DEC')
numSysselection['values'] = ('BIN', 'DEC')
'''

multBtn.grid(row=2, column=0, sticky='nsew')
additionBtn.grid(row=2, column=1, sticky='nsew')
decrementBtn.grid(row=2, column=2, sticky='nsew')
equalBtn.grid(row=2, column=3, sticky='nsew')
clearBtn.grid(row=2, column=4, sticky='nsew')
delSymbolBtn.grid(row=3, column=0, sticky='nsew')
dotBtn.grid(row=3, column=1, sticky='nsew')
#numSysselection.grid(row=3, column=2)



root.mainloop()