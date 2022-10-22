import tkinter as tk
import math
Num = []
def delete():
   calc.delete(0, tk.END)
def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, tk.END)
    calc.insert(0, value)
def make(digit):
   return tk.Button(win, text = f'{digit}',bd = 5,  command = lambda : add_digit(f'{digit}'))
def singoper(a):
    v  = float(calc.get())
    u = v**0.5
    calc.delete(0, tk.END)
    if a == 1:
       calc.insert(0, u )
    if a == 2:
      calc.insert(0, math.sin(v*math.pi/180) )
    if a == 3:
      calc.insert(0, math.cos(v*math.pi/180) )

win = tk.Tk()
win.geometry("240x280")
win.resizable(False, False)
def oper(a):
   v = float(calc.get())
   Num.append(a)
   Num.append(v)
   calc.delete(0, tk.END)
def ravno():
   global Num
   u = float(calc.get())
   w = Num[0]
   e = float(Num[1])
   
   calc.delete(0, tk.END)
   if w == 1:
      calc.insert(0, u + e )
   if w == 2:
      calc.insert(0, e - u )
   if w == 4:
      calc.insert(0, u * e )
   if w == 3:
      calc.insert(0, e/u )
   if w == 5:
      t = e ** u 
      calc.insert(0, t)
   Num = []
def insert():
   r = len(calc.get())
   calc.delete(r-1, r)

calc = tk.Entry(win, justify=tk.RIGHT)
calc.grid(row = 0, column = 0, columnspan=3)
make('1').grid(row = 1, column = 0, stick = 'wens', padx = 5, pady = 5)
make('2').grid(row = 1, column = 1, stick = 'wens', padx = 5, pady = 5)
make('3').grid(row = 1, column = 2, stick = 'wens', padx = 5, pady = 5)
make('4').grid(row = 2, column = 0, stick = 'wens', padx = 5, pady = 5)
make('5').grid(row = 2, column = 1, stick = 'wens', padx = 5, pady = 5)
make('6').grid(row = 2, column = 2, stick = 'wens', padx = 5, pady = 5)
make('7').grid(row = 3, column = 0, stick = 'wens', padx = 5, pady = 5)
make('8').grid(row = 3, column = 1, stick = 'wens', padx = 5, pady = 5)
make('9').grid(row = 3, column = 2, stick = 'wens', padx = 5, pady = 5)
make('0').grid(row = 4, column = 0, stick = 'wens', padx = 5, pady = 5)
make('.').grid(row = 4, column = 1, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = 'CE',bd = 5,  command = lambda: delete()).grid(row = 1, column = 4, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = '√',bd = 5,  command = lambda: singoper(1)).grid(row = 2, column = 4, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = '+',bd = 5,  command = lambda: oper(1)).grid(row = 1, column = 3, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = '**',bd = 5,  command = lambda: oper(5)).grid(row = 4, column = 2, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = '-',bd = 5,  command = lambda: oper(2)).grid(row = 2, column = 3, stick = 'wens', padx = 5, pady = 5)  
tk.Button(win, text = '/',bd = 5,  command = lambda: oper(3)).grid(row = 3, column = 3, stick = 'wens', padx = 5, pady = 5)  
tk.Button(win, text = '*',bd = 5,  command = lambda: oper(4)).grid(row = 4, column = 3, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = 'sin',bd = 5,  command = lambda: singoper(2)).grid(row = 3, column = 4, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = 'cos',bd = 5,  command = lambda: singoper(3)).grid(row = 4, column = 4, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = '=',bd = 5,  command = ravno).grid(row = 5, column = 4, stick = 'wens', padx = 5, pady = 5)
tk.Button(win, text = 'Backspace',bd = 5,  command = lambda: insert()).grid(row = 2, column = 4, stick = 'wens', padx = 5, pady = 5)
calc = tk.Entry(win, justify=tk.RIGHT)
calc.grid(row = 0, column = 0, columnspan=3)





win.mainloop()