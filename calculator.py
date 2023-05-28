import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.configure(bg='#14213d')

frm1 = tk.Frame(master=window, bg='grey')
frm1.pack(fill=tk.BOTH, expand=True)

lbl1 = tk.Label(master=frm1, text='0', bg='#14213d', fg='#FFFFFF', width=10, height=2, anchor='e')
lbl1.config(font=('Courier', 24))
lbl1.pack(side='right', fill=tk.X, expand=True)

frm2 = tk.Frame(master=window, width=300, height=50, bg='light grey')
frm2.pack(expand=True, fill=tk.BOTH)

frm2.columnconfigure([0, 1, 2, 3], weight=1)
frm2.rowconfigure([0, 1, 2, 3], weight=1)

bracket = 'open'

ls = ['AC', '( )', '%', '÷',
      '7', '8', '9', 'X',
      '4', '5', '6', '-',
      '1', '2', '3', '+',
      '0', ',', '⌫', '=']

def write_number(x):
    global bracket
    try:
        if x in [str(s) for s in range(0, 10)] and lbl1['text']=='0':
            lbl1['text']=x
        elif x == '( )' and bracket == 'open':
            lbl1['text']+='('
            bracket = 'close'
        elif x == '( )' and bracket == 'close':
            lbl1['text']+=')'
            bracket = 'open'
        elif x == '⌫':
            lbl1['text'] = lbl1['text'][:len(lbl1['text'])-1]
        elif x == 'AC':
            lbl1['text'] = '0'
        elif x == '=':
            expression = ''
            for char in lbl1['text']:
                if char == '÷':
                    expression += '/'
                elif char == 'X':
                    expression += '*'
                else:
                    expression += char
            lbl1['text'] = str(eval(expression))
        else:
            lbl1['text']+=x
    except:
        lbl1['text'] = 'Error'

btn_list = []

for i, v in enumerate(ls):
    action = lambda x = v: write_number(x)
    btn = tk.Button(text=v, master=frm2, width=4, height=2, command=action, bg='#14213D', fg='#E5E5E5')
    btn.config(font=('Courier', 14))
    btn.grid(column=i%4, row=int(i/4), sticky='nsew')
    btn_list.append(btn)

lbl1['text'] = '0'
window.mainloop()
