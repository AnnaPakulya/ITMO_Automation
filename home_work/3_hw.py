#задача 2
def task_2():
    a = float(input('введите a:'))
    b = float(input('введите b:'))
    if a > b:
        print(a)
    else:
        print(b)

task_2()

#задача 3
def task_3():
    c = float(input('введите c:'))
    d = float(input('введите d:'))
    if abs(c - d) == 135:
        print('yes')
    else:
        print('no')

task_3()

#задание 4
def task_4():
    e = int(input ('введите число от 1 от 12:'))
    if e <= 2 or e == 12:
        print('зима')
    elif 3 <= e <= 5:
        print('весна')
    elif 6 <= e <= 8:
        print('лето')
    else:
        print('осень')

task_4()

#задание 5
def task_5():
    f = int(input ('введите f: '))
    g = int(input ('введите g: '))
    h = int(input ('введите h: '))
    if f > 10 and g > 10 and h > 10:
        print('yes')
    else:
        print('no')

task_5()

#задание 6
def task_6():
    i = int(input ('введите i: '))
    j = int(input ('введите j: '))
    k = int(input ('введите k: '))
    l = int(input ('введите l: '))
    m = int(input ('введите m: '))
    positive_count = 0
    if i > 0:
        positive_count += 1
    if j > 0:
        positive_count += 1
    if k > 0:
        positive_count += 1
    if l > 0:
        positive_count += 1
    if m > 0:
        positive_count += 1
    print('количество положительных чисел: ', positive_count)

task_6()