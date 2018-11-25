#This works under both python2.7 and python3

import matplotlib.pyplot as plt
import numpy as np
pi=np.pi
idstr='By R. Sonnenfeld, New Mexico Tech Physics (Sept. 2017) -- Free for educational use only.'
suptitle='Griffith''s Figure 3.19'
title='by. Cameron Kimer!!!'
res=1001
a=1.0
V0=1


def Coeff(n):
#This should calculate the n-th coefficient of the fourier series
#Obviously not 1.
     if n%2 == 0:
       coeff = 0
     else:
       coeff=4*V0/(pi*n)
     return coeff


def main():
     print("SPN5-2, 2017: "+ title)
     print("====== ======= =========")
     print(" ")
     print("This template has been stripped down.  Fill in the right math.")
     x,dx=np.linspace(0,a,res,retstep=True)
     wave=0*x
     fig=plt.figure()
     special_ns=[1,5,10,100] #These are the 4 special n's that Griffiths plots
     for n in range(1,105):
         #build up your wave one term at a time
         # nth_term=something <-- put math here
         nth_term= Coeff(n)*np.sin(n*pi*x/a)
         wave=wave+nth_term
         if n in special_ns:  #This is a clever way
         #to only plot the four terms that Griffith's does
            plt.plot(x,wave,label='Sum of '+str(n)+' terms')
     plt.xlabel('$y/a$',fontsize=18)
     plt.ylabel('$V/V_0$',fontsize=18)
     plt.suptitle(suptitle,fontsize=16)
     plt.title(title,fontsize=12)
     plt.legend(loc='best')
     plt.savefig('SPN5-2s.png')
     plt.show()

main()

