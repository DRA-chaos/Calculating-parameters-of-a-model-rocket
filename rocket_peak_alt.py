
import math 
mass=0.05398
m=0.04
g=9.8
Area=0.000483
Cd=0.75 #for an avergae rocket
#Wind resistance force= 0.5x density x Cd x Area x v^2
k=0.5*1.22*0.75*Area

Thrust=6
Impulse=7
t=Impulse/Thrust

q=math.sqrt((Thrust-9.8*mass)/k)

x=(2*k*q)/mass
vel=q*((1-math.exp(-x*t))/(1+ math.exp(-x*t)))
w_res=k*(vel*vel)

#Let y1 denote the altitude at burnout
a= Thrust-(mass*9.8) - (k*vel*vel)
b=Thrust - (mass*9.8)

y1=(-mass/(2*k))*math.log(a/b)

#yc denotes the coasting distance
c=(m*9.8) + (k*vel*vel)

yc= (m/(2*k))*math.log(c/(m*9.8))

qa=math.sqrt(m*9.8/k)
qb=math.sqrt(9.8*k/m)
ta=math.atan(vel/qa)/qb
print(q)
print (x)
print(vel)
print (" The altitude at burnout \n\n" , y1  , " \n\n Burnout velocity \n" , vel , "\n\ncoasting distance \n\n" , yc)
