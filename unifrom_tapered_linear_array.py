import numpy as np
import matplotlib.pyplot as plt


c= 3e8
f = 28e9
wave_len = c/f
dx = wave_len/2
theta0 = 0
theta0 = np.deg2rad(theta0)
K = 64

k0 =2*np.pi/wave_len

#theta values from -90 to 90 degrees
theta = np.arange(-np.pi/2, (np.pi)/2, 0.01)
phi = np.arange(0, (np.pi), 0.01)

#define the variables u and u0
u = np.sin(theta)
u0 = np.sin(theta0)



S_u = np.exp(1j*(K-1)*k0*dx*(u-u0))*(np.sin(K*k0*dx*(u-u0)/2)/(K*np.sin(k0*dx*(u-u0)/2)))
S_u1 = np.abs(S_u)

#Normalized Radiation Pattern for a uniform tapered linear array
F1 = (np.sin(K*k0*dx*(u-u0)/2)/(K*np.sin(k0*dx*(u-u0)/2)))
F = F1**2




#Directiviy and Half Power Beam Width
HPBW1 = 0.8858*wave_len / (K*dx*np.cos(theta0))
print('Half Power Beam Width is at '+str(np.rad2deg(HPBW1))+' degrees')

D = 10*np.log10(K)
print('Directivity is '+str(D)+' dB')


#plot  Radiation Pattern
plt.figure(figsize=(30, 30)) 
plt.axes(projection = 'polar')
plt.polar(theta,S_u1,'-k') 
plt.title(' Radiation Pattern of a '+str(K)+
          ' omnidirectional element phased array at '+str(f/1e9)+
          ' GHz at '+str(np.rad2deg(theta0))+' degrees')
plt.show()



#Normalized Radiation Pattern in dB
plt.figure(figsize=(30, 30)) 
NF = 10*np.log10(F)
plt.grid(True, which ="both")
plt.semilogy(np.rad2deg(theta),F)


# Provide the title for the semilogy plot
plt.title('Normalized Radiation Pattern of a '+str(K)+
          ' omnidirectional element phased array at '+str(f/1e9)+
          ' GHz at '+str(np.rad2deg(theta0))+' degrees')
  
# Give x axis label for the semilogy plot
plt.xlabel('degrees')
# Give y axis label for the semilogy plot
plt.ylabel('Normalized Radiation pattern in db')
plt.show()

