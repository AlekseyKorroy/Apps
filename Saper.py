from random import randint
import tkinter as tk
Num = []
Nem = []
buttons =[]
r = 20
l = 15
q = 0
q1 = 0
q2 = 0
flag1 = False
def flag():
    global flag1
    if flag1 == True:
       flag1 = False
    else:
        flag1 = True
    print(flag1)

for _ in range (100):
    Num.append(0)
for i in range (100):
    Nem.append(i)
for _ in range(r):
    a = randint(0, len(Nem)-1)
    b = Nem[a]
    Nem.remove(b)
    Num[b] = 'bomb'
def function(i):
    global q
    global q1
    global q2
    if flag1:
        buttons[i]['text'] = -8
        q1+=1
        if Num[i] == 'bomb':
            q2+=1
        return 0
    else:
       buttons[i]['text'] = tuxt(i)
       q+=1
       print(q)
       if q == 70:
        print("You win!")
    if Num[i] == 'bomb':
        print(f"Результат:{q}, Флажков отмечено:{q1}, Правильно отмечено:{q2}")
        exit()
    
    
    
def tuxt(i):
    count = 0
    if Num[i] == 'bomb':
        return -6
    if i%10 != 9:
       if Num[i+1] == 'bomb':
        count+=1
    if i%10 != 0:
       if Num[i-1] == 'bomb':
          count+=1
    if i<90:
      if Num[i+10] == 'bomb':
        count+=1
    if i%10 != 0 and i<90:
     if Num[i+9] == 'bomb':
        count+=1
    if i%10 != 9 and i < 90:
     if Num[i+11] == 'bomb':
        count+=1
    if i % 10 != 0 and i > 9:

     if Num[i-11] == 'bomb':
        count+=1
    if i > 9:
      if Num[i-10] == 'bomb':
        count+=1
    if i > 9 and i%10 != 9:
      if Num[i-9] == 'bomb':
        count+=1
    return count
win = tk.Tk()
for i in range(10):
    for j in range(10):
        k = j + 10*i
        betton = tk.Button(win, text = "",bd = 5,  command = lambda k = j + 10 * i: function(k))
        betton.grid(row = i, column = j, stick = 'wens')
        buttons.append(betton)
for _ in range(l):
    i = randint(0, len(Nem)-1)
    r = Nem[i]
    Nem.remove(r)
    function(r)
flag = tk.Button(win, text = 'flag', bd = 5, command = flag )
flag.grid(row = 10, column = 10, stick = 'wens')
win.mainloop()

