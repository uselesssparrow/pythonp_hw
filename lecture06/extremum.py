import math
def gip(x):
    return 1/x
def Parabola(x):
    return x**2

def Line(x):
    return 2*x

def Extremum(a, b, *, func,dx):
    func_now=func_prev=func(a)
    x=a
    delta_prev=0
    while(x<=b):
        x+=dx 
        func_now=func(x)
        delta_now=func_now-func_prev
        if(delta_prev>0 and delta_now<0):
            return [x-dx,'max']
        if(delta_prev<0 and delta_now>0):
            return [x-dx,'min']
        delta_prev=delta_now
        func_prev=func_now
    return [None,None]
result = Extremum(-1,1, func=gip, dx=0.001)
print(result[1],result[0])
result = Extremum(-2, 2, func=Parabola,dx=0.001)
print(result[1],result[0]) # должно быть 0

result = Extremum(-20, -10, func=Parabola,dx=0.001)
print(result[1],result[0]) # должно быть None

result = Extremum(-20, 20, func=Line,dx=0.001)
print(result[1],result[0]) # должно быть None