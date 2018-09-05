import matplotlib.pylab as plt
import numpy as np

x=np.linspace(-1, 1,200)
h=x[1]-x[0]

#Primer puntito
def fun(x1,n):
	f=((x**2)-1)**n
	return f


def factorial(n):
    if n == 0:
        return 1
    else:
	l= n * factorial(n-1)
        return l

def polinomio0(x,n1):
	p=(1.0/((2.0**n1)*factorial(n1)))*(fun(x,n1))
	return p

p0=np.array(polinomio0(x,0))
p1=np.array(polinomio0(x,1))
p2=np.array(polinomio0(x,2))

print p1

plt.plot(x,p0, color="green")
plt.plot(x,p1, color="blue")
plt.plot(x,p2, color="red")
plt.show()

def derivada(x2):
	d=(fun(x2+h/2)-fun(x2-h/2))/h
	return d






