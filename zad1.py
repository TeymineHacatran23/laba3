import math
x=0.01
num=2*math.log(x**2)+3*math.log(x**3)
dem=math.exp(2+2**x)+math.exp(3+3**x)
y=num/dem
print(f"{y:.5f}")