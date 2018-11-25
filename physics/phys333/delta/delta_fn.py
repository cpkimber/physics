# # Dirac Delta function approximations

import numpy as np
import matplotlib.pyplot as plt

def deltagauss(x,b,sigma):
    arg=(-x**2/(2*sigma**2))
    num=np.exp(arg)
    den=sigma*np.sqrt(2*np.pi)
    delta=num/den
    return delta

def plotdeltagauss():
   x=np.linspace(-2,2,200)
   y1=deltagauss(x,0,1)
   y2=deltagauss(x,0,0.3)
   y3=deltagauss(x,0,0.1)
   plt.plot(x,y1,x,y2,x,y3)
   plt.legend(('$\sigma=1$','$\sigma=0.3$','$\sigma=0.1$'))
   plt.xlabel('X'); plt.ylabel('Y')
   plt.title('Gaussian-based Dirac $\delta$ function')
   plt.savefig('kimberDeltaGaussian.png')
   plt.show()

plotdeltagauss()

def lorentzian(x, epsilon):
    return(epsilon/(x**2 + epsilon**2))

def plotlorenztian():
   x=np.linspace(-2,2,200)
   y1=lorentzian(x,1)
   y2=lorentzian(x,0.3)
   y3=lorentzian(x,0.1)
   plt.plot(x,y1,x,y2,x,y3)
   plt.legend(('$\epsilon=1$','$\epsilon=0.3$','$\epsilon=0.1$'))
   plt.xlabel('X'); plt.ylabel('Y')
   plt.title('Lorenzian')
   plt.savefig('kimberlorentzian.png')
   plt.show()

plotlorenztian()

def sinc(x, a, b):
    return((1/np.pi) * (np.sin(a * (x - b)))/(x - b))

def plotsinc():
   x=np.linspace(-.25,.25,200)
   y1=sinc(x, 10, 0)
   y2=sinc(x, 100 , 0)
   y3=sinc(x, 1000000000, 0)
   plt.plot(x,y1,x,y2,x,y3)
   plt.legend(('a = 10','a = 100','a = 1000000000'))
   plt.xlabel('X'); plt.ylabel('Y')
   plt.title('Sinc')
   plt.savefig('kimbersinc.png')
   plt.show()

plotsinc()
