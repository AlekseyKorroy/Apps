from random import randint
import tkinter as tk
bombs = []#хранит расположение бомбочек
open_and_bombs = []#Хранит клетки, чтобы выбрать клетки открытые в начале и куда поставить бомбы
buttons =[]
activate = [False for i in range(100)]
bombs_count = 20
open_buttons = 15
q = 0#Сколько мест открыли
q1 = 0#Сколько флажков поставили
q2 = 0#Сколько правильно поставили
flag1 = False
def flag():#меняет значение флажка
    global flag1
    if flag1 == True:
       flag1 = False
    else:
        flag1 = True
    print(flag1)

for _ in range (100):
    bombs.append(0)
for i in range (100):
    open_and_bombs.append(i)
print(open_and_bombs)
for _ in range(bombs_count):#Выбираем места бомбочкам
    a = randint(0, len(open_and_bombs)-1)
    b = open_and_bombs[a]
    open_and_bombs.remove(b)
    bombs[b] = 'bomb'
def function(i):#Принимает номер клетки и работает с ним
    global q
    global q1
    global q2
    global activate
    if flag1:
        buttons[i]['text'] = -8
        q1+=1
        if bombs[i] == 'bomb':
            q2+=1
        return 0
    else:
       buttons[i]['text'] = tuxt(i)
       if activate[i] == False:
        q+=1
        activate[i] = True
       print(q)
       if q == 70:
        print("You win!")
    if bombs[i] == 'bomb':
        print(f"Результат:{q}, Флажков отмечено:{q1}, Правильно отмечено:{q2}")
        exit()
    
    
    
def tuxt(i):#считает сколько бомб в окрестности клетки
    count = 0
    if bombs[i] == 'bomb':
        return -6
    if i%10 != 9:
       if bombs[i+1] == 'bomb':
        count+=1
    if i%10 != 0:
       if bombs[i-1] == 'bomb':
          count+=1
    if i<90:
      if bombs[i+10] == 'bomb':
        count+=1
    if i%10 != 0 and i<90:
     if bombs[i+9] == 'bomb':
        count+=1
    if i%10 != 9 and i < 90:
     if bombs[i+11] == 'bomb':
        count+=1
    if i % 10 != 0 and i > 9:

     if bombs[i-11] == 'bomb':
        count+=1
    if i > 9:
      if bombs[i-10] == 'bomb':
        count+=1
    if i > 9 and i%10 != 9:
      if bombs[i-9] == 'bomb':
        count+=1
    return count
win = tk.Tk()
for i in range(10):#Создаем кнопки
    for j in range(10):
        k = j + 10*i
        betton = tk.Button(win, text = "",bd = 5,  command = lambda k = j + 10 * i: function(k))
        betton.grid(row = i, column = j, stick = 'wens')
        buttons.append(betton)
for _ in range(open_buttons):
    i = randint(0, len(open_and_bombs)-1)
    w = open_and_bombs[i]
    open_and_bombs.remove(w)
    function(w)
flag = tk.Button(win, text = 'flag', bd = 5, command = flag )
flag.grid(row = 10, column = 10, stick = 'wens')
win.mainloop()
