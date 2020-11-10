import random
s=input('Введите число вида NdM, N-число кубиков, M-число граней: ')
if (s.count('d')!=1):
    print('Неправильный формат строки')
    exit(1)
N_str=s[:s.index('d')]
M_str=s[s.index('d')+1:]
try:
    N=int(N_str)
    M=int(M_str)
except ValueError:
    print('Неправильный формат чисел')
    exit(2)
sum_number=[0 for _ in range(0,M*N+1)]
variants=[]
k=0
while(k<M**N):
    result=[random.randint(1,M) for _ in range(1,N+1)]
    if result not in variants:
        k+=1
        variants.append(result)
        sum_number[sum(result)]+=1
for i in range(N,M*N+1):
    print(f'{i}={100*sum_number[i]/(M**N):.3}%')