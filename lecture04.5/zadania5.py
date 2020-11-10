import random, copy
a=6
n=10
num=[]
for i in range(0,n):
    num.append(random.randint(-a,a))
print(f"Исходный список: {num}")
######################
print('1.Дан список целых чисел. Исключить из него a) максимальный b)минимальный элемент. Если таких элементов несколько исключаются все')
min=max=num[0]
num1=[]
for i in range(0,n):
    if num[i]<min:
        min=num[i]
    if num[i]>max:
        max=num[i]
for i in range(0,n):
    if(num[i]!=max and num[i]!=min):
        num1.append(num[i])
print(num1) 
######################
print('2. Дан список целых чисел, в котором есть нулевые элементы. Исключить нулевые элементы.')
num2=[]
for i in range(0,n):
    if(num[i]!=0):
        num2.append(num[i])
print(num2)
######################
print('3. Дан список X целых чисел и целое число b. Исключить из списка элементы, равные b.')
b=random.randint(-a,a)
print(f'b={b}')
num3=[]
for i in range(0,n):
    if(num[i]!=b):
        num3.append(num[i])
print(num3)
######################
print('4. Дан список целых чисел и числа A1, A2 и A3. Включить эти числа в список, расположив их после второго элемента.')
A1=random.randint(-a,a)
print(f'A1={A1}')
A2=random.randint(-a,a)
print(f'A2={A2}')
A3=random.randint(-a,a)
print(f'A3={A3}')
num4=copy.copy(num)
num4+=['','','']
for i in range(n+2,4,-1):
    num4[i]=num4[i-3]
num4[2]=A1
num4[3]=A2
num4[4]=A3
print(num4)
######################
max=num[0]
num5=[]
print('5. Вывести все элементы списка, стоящие до максимального элемента')
for i in range(0,n):
    if num[i]>max:
        max=num[i]
id=num.index(max)
for i in range(0,id):
    num5.append(num[i])
print(num5)
######################
print('6. Дан список чисел и число A. Вычислить сумму тех отрицательных элементов списка, значения которых больше, чем A. Подсчитать также количество таких элементов.')
A=random.randint(-a,a)
print(f'A={A}')
k=0
s=0
for i in range(0,n):
    if(num[i]<0 and num[i]>A):
        k+=1
        s+=num[i]
print(f'Число таких элементов: {k}, а их сумма: {s}')
######################
print('7. Дан список из чисел. Вычислить среднее арифметическое положительных элементов этого списка и среднее арифметическое отрицательных элементов этого списка')
k_otr=0
k_pol=0
s_otr=0
s_pol=0
for i in range(0,n):
    if (num[i]<0):
        k_otr+=1
        s_otr+=num[i]
    if (num[i]>0):
        k_pol+=1
        s_pol+=num[i]
s_otr=s_otr/k_otr
s_pol=s_pol/k_pol
print(f'Cреднее арифметическое положительных элементов: {s_pol:.3f}. Cреднее арифметическое отрицательных элементов: {s_otr:.3f}')
######################
print('8. Исключить из списка элементы, расположенные между максимальным и минимальным.(первыми)')
num8=copy.copy(num)
kmin=0
kmax=0
for i in range(0,n):
    if num[i]<min:
        min=num[i]
    if num[i]>max:
        max=num[i]
kmin=num.index(min)
kmax=num.index(max)
if(kmin<kmax):
    for i in range (kmin+1, kmax):
        num8.remove(num[i])
if(kmin>kmax):
    for i in range (kmax+1, kmin):
        num8.remove(num[i])
print(num8)