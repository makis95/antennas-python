import numpy as np
import matplotlib.pyplot as plt

c= 3e8
f = 28e9
wave_len = c/f
dx = wave_len/2
theta0 = 0
theta0 = np.deg2rad(theta0)
K = 16

k0 =2*np.pi/wave_len

#theta = np.arange(-np.pi/2, (np.pi)/2, np.pi/(K))
theta1 = np.arange(-np.pi/2, (np.pi)/2, 0.01)

u = np.sin(theta1)
u0 = np.sin(theta0)


#x-axis coordinate of element
xk = (K)*[0] 
for k in range(K):
    xk[k]= (k)*dx
    

xk = np.array(xk)


#cosine taper parameters
m = 2
h = 2

ak_magn = h + (1-h)*np.cos(np.pi*xk/(K*dx))**m
ak = ak_magn*np.exp(-1j*k0*dx*u0)

z = np.exp(1j*k0*dx*u)



#Array factor or signal computation
S = []
for k in range(K):
    S.append(ak[k]*z**(k))
S = np.array(S)
S_u = np.sum(S,axis=0)



#Normalized Radiation Pattern for a square cosine tapered linear array
s = np.abs(S_u)
s_max = max(s)
S_sq =s**2
F = S_sq/s_max**2


#Directiviy and Half Power Beam Width
#HPBW = 40/np.cos(np.rad2deg(theta0))
#print('Half Power Beam Width is at '+str(np.rad2deg(HPBW))+' degrees with cosine taper')

D = np.sum(ak_magn)**2/np.sum(ak_magn**2)
D_db = 10*np.log10(D)
n_tap =  np.sum(ak_magn)**2/(K*np.sum(ak_magn**2))
print('Directivity is '+str(D_db)+' dB')


#plot  Radiation Pattern
plt.figure(figsize=(30, 30)) 
plt.axes(projection = 'polar')
plt.polar(theta1,s,'-k') 
plt.show()




plt.figure(figsize=(30, 30)) 
plt.grid(True, which ="both")
#plt.semilogy(np.rad2deg(THETA_),F_)
plt.semilogy(np.rad2deg(theta1),F)
  
# Provide the title for the semilogy plot
plt.title('Normalized Radiation Pattern of a '+str(K)+
          ' omnidirectional element phased array at '+str(f/1e9)+
          ' GHz at '+str(np.rad2deg(theta0))+' degrees with cosine taper')
# Give x axis label for the semilogy plot
plt.xlabel('degrees')
  
# Give y axis label for the semilogy plot
plt.ylabel('Normalized Radiation pattern in db')
#  


plt.show()
