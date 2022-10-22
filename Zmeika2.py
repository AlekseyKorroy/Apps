import pygame
from random import randint

# Инициализируем pygame
pygame.init()

# Создаем экран и буковки
screen = pygame.display.set_mode((500, 500))
Nam = [500, 300, 200, 150, 100, 50]
e = int(input("Введите уровень сложности от 1 до 6: "))
Num = []
count = 1
eyex = 10
eyey = 10
eye2x = 35
eye2y = 10
for x in range(0, 10):
    Num.append(25 + 50 * x)
Nem = Num.copy()
status = None  # обозначает куда двигается на данный момент змейка
# Координаты центра яблочка
Applex = Num[randint(0, 9)]
Appley = Nem[randint(0, 9)]
# Список координатов центров квадратиков змейки
Squarex = [25]
Squarey = [25]
def gg():
   for q in range(1, len(Squarex)):
            if Squarex[0]==Squarex[q]:
                if Squarey[0]==Squarey[q]:
                     print("Вы проиграли")
                     print(f"{count}")
                     exit(0)

# Проверка яблочка
def apple_check(a, b, u, v):
    global count
    global Applex
    global Appley
    if a == Applex and b == Appley:
        Squarex.append(v)
        Squarey.append(u)
        count += 1
        Applex = Num[randint(0, 9)]
        Appley = Nem[randint(0, 9)]


# Двигаем хвост
def move_tail(count):
    for k in range(count - 1, 0, -1):
        Squarex[k] = Squarex[k - 1]
        Squarey[k] = Squarey[k - 1]


def move(a):
    global eye2x
    global eye2y
    global eyex
    global eyey
    # Запоминаем координаты хвоста
    v = Squarex[-1]
    u = Squarey[-1]
    # Двигаем остальное
    move_tail(count)
    # Двигаем голову и проверяем на стенку
    if a == "to_left":
        Squarex[0] -= 50
        eyex-=50
        eye2x-=50
        gg()
        if Squarex[0] == -25:
            print("Вы проиграли")
            print(f"{count}")
            exit(0)
    if a == "to_right":
        Squarex[0] += 50
        eyex+=50
        eye2x+=50
        gg()
        if Squarex[0] == 525:
            print("Вы проиграли")
            print(f"{count}")
            exit(0)
    if a == "to_down":
        Squarey[0] += 50
        eyey+=50
        eye2y+=50
        gg()
        if Squarey[0] == 525:
            print("Вы проиграли")
            print(f"{count}")
            exit(0)
    if a == "to_up":
        Squarey[0] -= 50
        eyey-=50
        eye2y-=50
        gg()
        if Squarey[0] == -25:
            print("Вы проиграли")
            print(f"{count}")
            exit(0)
    
    # Проверка на яблоко
    apple_check(Squarex[0], Squarey[0], u, v)


# Функция рисования змейки
def Draw_Snake(count, Squarex, Squarey):
    # Рисуем синюю голову
    pygame.draw.rect(screen, color=(0, 0, 255),
                     rect=(Squarex[0] - 25, Squarey[0] - 25, 50, 50), border_radius=1)
    # Рисуем зеленое тело
    for J in range(1, count):
         pygame.draw.rect(screen, color=(255 , 255 , 0 ),
                         rect=(Squarex[J] - 25, Squarey[J] - 25, 50, 50), border_radius=1)
        


Draw_Snake(count, Squarex, Squarey)
while True:
    # Заливаем экран серо-синим цветом
    screen.fill((67, 97, 94))
    #screen.fill((255, 0, 0))
    # Определяем время задержки
    pygame.time.delay(Nam[e-1])

    # цикл для обработки событий
    for event in pygame.event.get():
        # если произошло событие - нажатие клавиши
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and status != "to_right":
                status = "to_left"
            # если была нажата стрелка вправо
            if event.key == pygame.K_RIGHT and status != "to_left":
                status = "to_right"
            # если была нажата стрелка вниз
            if event.key == pygame.K_DOWN and status != "to_up":
                status = "to_down"
            # если была нажата стрелка вверх
            if event.key == pygame.K_UP and status != "to_down":
                status = "to_up"

        # Делаем крестик
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    move(status)

    # выводим мяч на экран и обновляем дисплей
    Draw_Snake(count, Squarex, Squarey)
    pygame.draw.circle(screen, color=(255, 0, 0), center=(Applex, Appley), radius=20)
    pygame.draw.circle(screen, color=(255, 255, 255), center=(eyex, eyey), radius=10)
    pygame.draw.circle(screen, color=(255, 255, 255), center=(eye2x, eye2y), radius=10)
    pygame.draw.circle(screen, color=(0, 0, 0), center=(eyex, eyey), radius=4)
    pygame.draw.circle(screen, color=(0, 0, 0), center=(eye2x, eye2y), radius=4)
    pygame.display.update()
