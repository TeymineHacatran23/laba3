import math
a=2
b=3.4
h=0.05
for i in range(int((b-a)/h)+1):
    x=a+i*h
    y=math.sin(x**3)**2+math.log(x**2)**3-math.cos(x**3)**2/(x**2+x**3)
    print(f"{x:.2f}|{y:.4f}")
