s=input("Введите целое число больше 1: ")
#проверка на корректность ввода
try:
    s=float(s)
except ValueError:
    print("Введено не число")
    exit(1)
    
if(int(s)!=s):
    print("Введено не целое число")
    exit(2)

s=int(s)
    
if(s<2):
    print("Введено число меньше 2")
    exit(3)

num=[]
prime=[]
#создание списка чисел от 2 до s
for n in range(2,s+1):
    num.append(n)
#нахождение простых чисел
n=0
while(n<len(num)):
    prime.append(num[n])
    n+=1
    i=2
    while(prime[len(prime)-1]*i<=s):
        if(prime[len(prime)-1]*i in num):
            num.remove(prime[len(prime)-1]*i)
        i+=1
#запись в файл
f = open('prime.txt', 'w')
for k in range(len(prime)):
    f.write(str(prime[k])+'\n')
f.close()
print(f"Простые числа до {s} были записаны в файл prime.txt")