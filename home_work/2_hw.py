#задача 1
def task_1():
    a : int = 1
    b : float = 1.1500
    c : str = 'hello, world!'
    d : list = [1, 2, 3, 5, 8, 13, 21]
    e : bool = True
    print (a, 'относится к типу', type(a))
    print (b, 'относится к типу', type(b))
    print (c, 'относится к типу', type(c))
    print (d, 'относится к типу', type(d))
    print (e, 'относится к типу', type(e))

task_1()

#задача 2
def task_2():
    a : list = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3],'- первые 3 значения списка')
    print(a, '- это последовательность Фибоначчи')

task_2()

#задача 3
def task_3():
    x = float(input ('введите x:'))
    return(x**2)

print(task_3())