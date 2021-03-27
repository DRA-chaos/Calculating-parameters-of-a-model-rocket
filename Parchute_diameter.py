import math
Cd=0.75
mass=0.06
#Area=0.0078
v=3
#fd=0.5*1.22*0.75*Area*v*v
fg=mass*9.8
pi=3.14159265

Area= (2*mass*9.8)/(1.22*0.75*v*v)
D=math.sqrt((4*Area)/pi)
print(" Diameter of the chute is " , D)
