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
