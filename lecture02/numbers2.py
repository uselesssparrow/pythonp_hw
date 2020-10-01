st_in=input("Введите целое число от 0 до 99: ")

if not str.isdigit(st_in):
    print("Введено не целое число или буквы")
    exit()   
    
st_in=int(st_in)

if (st_in<0) or (st_in>99): #проверка диапазона
    print("Введено число не в диапазоне от 0 до 99")
    exit()
    
num=''

if (st_in//10==9):
    num+='девяносто'
elif (st_in//10==8):
    num+='восемьдесят'
elif (st_in//10==7):
    num+='семьдесят'
elif (st_in//10==6):
    num+='шестьдесят'
elif (st_in//10==5):
    num+='пятьдесят'
elif (st_in//10==4):
    num+='сорок'
elif (st_in//10==3):
    num+='тридцать'
elif (st_in//10==2):
    num+='двадцать'    

if (st_in%10==9):
    num+=' девять'
elif (st_in%10==8):
    num+=' восемь'
elif (st_in%10==7):
    num+=' семь'
elif (st_in%10==6):
    num+=' шесть'
elif (st_in%10==5):
    num+=' пять'
elif (st_in%10==4):
    num+=' четырe'
elif (st_in%10==3):
    num+=' три'
elif (st_in%10==2):
    num+=' два'
elif (st_in%10==1):
    num+=' один'

if (st_in==19):
        num='девятнадцать'
elif (st_in==18):
        num='восемнадцать'
elif (st_in==17):
        num='семнадцать'
elif (st_in==16):
        num='шестнадцать'
elif (st_in==15):
        num='пятнадцать'
elif (st_in==14):
        num='четырнадцать'
elif (st_in==13):
        num='тринадцать'
elif (st_in==12):
        num='двенадцать'
elif (st_in==11):
        num='одиннадцать'
elif (st_in==10):
        num='десять'
    
if(st_in==0):
    num='ноль'
    
print(num)
