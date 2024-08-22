import math
def divi(a,b):
    x=((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    y=((b[0]*a[1])-(b[1]*a[0]))/((b[0]**2)+(b[1]**2))
    return x,y

def suma(a,b):
    x=a[0]+b[0]
    y=a[1]+b[1]
    return x,y

def multi(a,b):
    x=((a[0]*b[0])-(a[1]*b[1]))
    y=((a[0]*b[1])+(a[1]*b[0]))
    return x,y

def resta(a,b):
    x=a[0]-b[0]
    y=a[1]-b[1] 
    return x,y

def modulo(a):
    x=math.sqrt((a[0]**2)+a[1]**2)
    return x

def conjugado(a):
    x=a[0]
    y=a[1]*-1
    return x,y

def polar(a):
    x=math.sqrt((a[0]**2)+a[1]**2)
    y=math.atan(a[1]/a[0])
    return x,y

def cartesiano(a):
    x=a[0]*math.cos(a[1])
    y=a[0]*math.sin(a[1])
    return x,y

def fase(a):
    x=math.atan2(a[1},a[0])
    return x
                 
