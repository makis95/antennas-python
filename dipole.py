import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits.mplot3d.axes3d as axes3d
  
# setting the axes
# projection as polar

  
# setting the length of 
# axis of cardioid
a=3
  
# creating an array
# containing the radian values
theta = np.arange(0, (2 * np.pi), 0.01)
   
# plotting the pattern
F = a*(np.sin(theta))**2
print(F)
plt.axes(projection = 'polar')
plt.figure(figsize=(30, 30)) 
plt.polar(theta,F,'-k') 

### display the polar plot

plt.show()


#theta, phi =  np.arange(0, (2 * np.pi), 0.1), np.arange(0, (2 * np.pi), 0.1)
#THETA, PHI = np.meshgrid(theta, phi)
#R = np.sin(THETA)**2
#X = R * np.sin(PHI) * np.cos(THETA)
#Y = R * np.sin(PHI) * np.sin(THETA)
#Z = R * np.cos(PHI)
#fig = plt.figure(figsize = (8, 8))
#ax = plt.axes(projection = '3d')
#plot = ax.plot_surface(
#    X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
#    linewidth=0, antialiased=False, alpha=0.5)
#
#plt.show()
#


#NF = -10*np.log10(F)
#
#plt.semilogy(theta , NF)
#
##plt.ylim(NF)
##  
##plt.xlim(theta)
#  
## Provide the title for the semilogy plot
#plt.title('db')
#  
## Give x axis label for the semilogy plot
#plt.xlabel('degrees')
#  
## Give y axis label for the semilogy plot
#plt.ylabel('Normalized Radiation pattern')
#  
## Display the semilogy plot
#plt.show()