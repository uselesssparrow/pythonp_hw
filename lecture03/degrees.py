#ввод, определение ед.измерения
s=input('Введите температуру в градусах цельсия или фаренгейта: ')
deg_type=s[-1]
#корректность ед.измерения
if (deg_type!='C') and (deg_type!='F') and (deg_type!='c') and (deg_type!='f'):
    print('Не указаны единицы измерения в конце')
    exit(1)
#отбрасывание ед.измерения    
s=s[:-1]
s_abs=s
#если есть минус то убрать
if s_abs[0]=='-':
    s_abs=s_abs[1:]

if s_abs.find('.')==0 or s_abs.find('.')==len(s_abs)-1:
    print('Точка не может стоять в конце или в начале')
    exit(3)
#если точки нет, то все ли остальные символы цифры    
if s_abs.find('.')==-1:
    if (s_abs.isdigit())==0:
        print("Введено не число ")
        exit(2)
#если точки есть, то все ли остальные символы цифры 
if s_abs.find('.')!=-1:
    sdot=s_abs[:s_abs.find('.')]+s_abs[s_abs.find('.')+1:len(s_abs)]
    if sdot.isdigit()==0:
        print("Введено не число")
        exit(2)
#вычисление и вывод        
deg=float(s)
if deg_type=='C' or deg_type=='c':
    deg=deg*9/5+32
    print(f"{deg}F")
else: 
    deg=5/9*(deg-32)
    print(f"{deg}C")
