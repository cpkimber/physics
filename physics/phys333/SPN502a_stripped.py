#This works under both python2.7 and python3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
pi=np.pi
idstr='By R. Sonnenfeld, New Mexico Tech Physics (Sept. 2017)'
suptitle='Griffith''s Figure 3.18'
title='Cameron Kimber!!'
res=1001
a=1.0
V0=1


def Coeff(n):
#Clearly the coefficient isn't 1.  Go ahead and fix this
     coeff=2*V0/n
     return coeff

def main():
     print("SPN5-2a, 2017: "+ title)
     print("=======  ======= =========")
     print(" ")
     print("This template has been stripped down.  Fill in the right math.")
     x=np.arange(0,1,0.025) #Unlike range, arange allows non-integers, and
     #step sizes
     y=x
     X,Y=np.meshgrid(x,y)  #meshgrid turns linear coordinates into a 2-D array
     VV=0*X  #Initialize the voltage to be the right size.
     for n in range(1,103,2):  #We need a number of terms in the Fourier series
         VV=(2*V0/pi) * np.arctan(np.sin(np.pi * Y/a)/ np.sinh(np.pi * X/a))

#The following just handles the plotting.  You don't have to mess with this.
     fig=plt.figure()
     ax=fig.gca(projection='3d')
     ax.view_init(30,45)
     surf=ax.plot_wireframe(X,Y,VV)
     plt.xlabel('$y/a$',fontsize=18)
     plt.ylabel('$V/V_0$',fontsize=18)
     plt.suptitle(suptitle,fontsize=16)
     plt.title(title,fontsize=12)
     plt.savefig('SPN5-2mesh.png')
     plt.show()

main()



