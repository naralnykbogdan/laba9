import numpy as np
import random
import timeit 
while True:
 vvod=input('Як вводити?Якщо рандомно-1,якщо з клавіатури-будь-яка кнопка')  #
 metod=input('Яким методом?бульбашковим-1,вибору-2,вставками - будь-яка')
 sortirovka=input('ЯК сортувати?Якщо по зростанню-1,по спаданню-будь-яка')
 def bubl_up(s): #функція для бульбашкового методу, для сортування по зростанню 
    global count #заводим 2 лічильника і робим їх глобальними щоб їх можна було визвати в майбутньому для оцінки роботи   и оценки работы
    global obmen
    count=0
    obmen=0
    for i in range(1,n): #бульбашковйи алгоритм
        for j in range(n-1,i-1,-1):
            count+=1
            if (A[j-1]>A[j]):
                obmen+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def bubl_down(s):#функція для бульбашкового методу, для сортування по спаданню
    global count
    global obmen
    count=0
    obmen=0
    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            count+=1
            if (A[j-1]<A[j]):
                obmen+=1
                A[j],A[j-1]=A[j-1],A[j]
    print(A)
 def select_up(s):#функція дял алгоритму сортування методу вибору, для сортування по зростанню
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):#алгоритм вибору
        min=i
        for j in range(i+1,n):
            count_se+=1
            if A[j]<A[min]:
                obmen_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def select_down(s):#функція для алгоритму сортування методу вибору для сортування по спаданню
    global count_se
    global obmen_se
    count_se=0
    obmen_se=0
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            count_se+=1
            if A[j]>A[min]:
                obmen_se+=1
                min=j
        A[i],A[min]=A[min],A[i]
    print(A)
 def insertion_up(s):#функція для алгоритму сортування методу вставки, для сортування по зростанню
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):#алгоритм вставки
        j=i-1
        key=A[i]
        while j>=0 and A[j]>key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
 def insertion_down(s):#функція ял алгоритму сортування методу вставки, дял сортування по спаданнюзаводим функцию для алгоритма сортировки метода вставки,для сортировки по убыванию
    global count_ins
    global obmen_ins
    count_ins=0
    obmen_ins=0
    for i in range(1,n):
        j=i-1
        key=A[i]
        while j>=0 and A[j]<key:
            count_ins+=2
            obmen_ins+=1
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
        
 if vvod=='1': 
  x=int(input('Введіть к-ть цифр'))
  A=np.zeros(x,dtype=int) #Додаємо масив і наповнюєм його рандомними значеннями
  for i in range(x):
   A[i]=random.randint(0,100000)
  print(A)
  n=len(A)
  s=x
 else:#якщо значення vvod !=1,то ми заповнюємо наш масив самі, до 30 значень
   x=int(input('Введіть к-ть цифр'))
   while x>30:
      x=int(input('Введіть к-ть до 30'))
   A=np.zeros(x,dtype=int)
   for i in range(x):
    A[i]=int(input('Введіть число '))
   print(A)
   n=len(A)
   s=x
 def xarakteristika_bubl(countner): #Заводим функции для оценки работы каждого из методов
    print('К-ть порівнювань для бульбашкового методу',countner)
    print('К-ть обмінів дял бульбашкового методу',obmen)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)#Додаємо змінній t значення часу за який працював кожний алгоритм
    print('Програма виконувалась',t)
 def xarakteristika_select(countner):
    print('К-ть порывнювань методу вибору',countner)
    print('К-ть обмінів методу вибору',obmen_se)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Програма виконувалась',t)
 def xarakteristika_ins(countner):
    print('К-ть порівнювань методу вставками',countner)
    print('К-ть обмінів метоу вставками',obmen_ins)
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Программа выполнялась',t)
 if metod=='1': #В залежності від вибраних значень вивиодим наші функції
  if sortirovka=='1':
    bubl_up(s)
    xarakteristika_bubl(countner=count)
  else:
    bubl_down(s)
    xarakteristika_bubl(countner=count)
 elif metod=='2':
     if sortirovka=='1':
         select_up(s)
         xarakteristika_select(countner=count_se)
     else:
         select_down(s)
         xarakteristika_select(countner=count_se)
 else:
    if sortirovka=='1':
        insertion_up(s)
        xarakteristika_ins(countner=count_ins)
    else:
        insertion_down(s)
        xarakteristika_ins(countner=count_ins)
 result = input('Повторити програму? Якщо так - 1, якщо ні - інше: ') #зациклюєм нашу програму
 if result == '1':
   continue
 else:
   break
