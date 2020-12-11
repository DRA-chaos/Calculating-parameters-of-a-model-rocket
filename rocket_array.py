import math
from statistics import mean
mass=0.06 #average mass during boost
m=0.03 #mass during coast
g=9.8
Area=0.0078 #assuming a radius of 5cm
Cd=0.75 #for an avergae rocket
#Wind resistance force= 0.5x density x Cd x Area x v^2
k=0.5*1.22*0.75*Area
altarray=[]
Thrust=6
#Impulse=7
Impulse=[5,6,7,8,9,10]
for i in range(1,6):
    
    t=Impulse[i]/Thrust

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
    y=y1+yc
    altarray.append(y)

avg_altitude= mean(altarray)

qa=math.sqrt(m*9.8/k)
qb=math.sqrt(9.8*k/m)
ta=math.atan(vel/qa)/qb
print("The array of altitudes corresponding to impulses ranging from 5 to 10 \n" , altarray)
print(" \n the average altitude : " , avg_altitude) # This corresponds to the average peak altitute (sum of y1 and coasting distance yc)
#print(q)
#print (x)
#print(vel)
print (" The altitude at burnout \n\n" , y1  , " \n\n Burnout velocity \n" , vel , "\n\ncoasting distance \n\n" , yc)
print("\n\n coasting time \n\n", ta)
