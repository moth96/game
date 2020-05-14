import math
import random
import matplotlib.pyplot as plt
import time

b = ['position_x','position_y','velocity_x','velocity_y','mass']
def force(b1,b2,b3):
    G = 5000
    d12 = ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2)**0.5
    total_force12 = G * b1[4] * b2[4] / (d12**2)
    f12_x = total_force12 * (b2[0] - b1[0])/d12
    f12_y = total_force12 * (b2[1] - b1[1])/d12
    
    d13 = ((b1[0] - b3[0])**2 + (b1[1] - b3[1])**2)**0.5
    total_force13 = G * b1[4] * b3[4] / (d13**2)
    f13_x = total_force13 * (b3[0] - b1[0])/d13
    f13_y = total_force13 * (b3[1] - b1[1])/d13
    
    f_x = f12_x + f13_x
    f_y = f12_y + f13_y
    f = [f_x,f_y]
    return f
    
def acceleration(b,f):
    a_x = f[0]/b[4]
    a_y = f[1]/b[4]
    acc = [a_x,a_y]
    return acc
    
def update_velocity(b,acc,t):
    velocity_x = b[2] + acc[0] * t
    velocity_y = b[3] + acc[1] * t
    b[2] = velocity_x
    b[3] = velocity_y
    
def update_position(b,t):
    position_x = b[0] + b[2] * t
    position_y = b[1] + b[3] * t
    b[0] = position_x
    b[1] = position_y
    '''
    # 限制区域
    if ((b[0] > 5) or (b[0] < -5)):
        b[2] = -b[2]
    if ((b[1] > 5) or (b[1] < -5)):
        b[3] = -b[3]
    '''

def get_random():
    x = []
    x.append(random.uniform(-20,20))
    x.append(random.uniform(-20,20))
    x.append(random.uniform(-20,20))
    x.append(random.uniform(-20,20))
    x.append(random.uniform(1,2))
    return x
    
def get_str(b):
    x = str(round(b[0],2))
    y = str(round(b[1],2))
    vx = str(round(b[2],2))
    vy = str(round(b[3],2))
    m = str(round(b[4],2))
    str1 = x +" "+ y +" "+ vx +" "+ vy +" "+ m
    return str1
    
plt.ion()
plt.figure(1) 
b1 = get_random()
b2 = get_random()
b3 = get_random()
t = 0.001
c1x = []
c1y = []
c2x = []
c2y = []
c3x = []
c3y = []
while True:
    f1 = force(b1,b2,b3)
    a1 = acceleration(b1,f1)
    update_velocity(b1,a1,t)
    update_position(b1,t)
    f2 = force(b2,b1,b3)
    a2 = acceleration(b2,f2)
    update_velocity(b2,a2,t)
    update_position(b2,t)
    f3 = force(b3,b1,b2)
    a3 = acceleration(b3,f3)
    update_velocity(b3,a3,t)
    update_position(b3,t)
    c1x.append(b1[0])
    c1y.append(b1[1])
    c2x.append(b2[0])
    c2y.append(b2[1])
    c3x.append(b3[0])
    c3y.append(b3[1])
    str1 = get_str(b1)
    str2 = get_str(b2)
    str3 = get_str(b3)
    if len(c1x) >= 10000:
        c1x.remove(c1x[0])
        c1y.remove(c1y[0])
        c2x.remove(c2x[0])
        c2y.remove(c2y[0])
        c3x.remove(c3x[0])
        c3y.remove(c3y[0])
    plt.cla()
    plt.title('Three Body')
    plt.plot(c1x,c1y,'r')
    plt.plot(c2x,c2y,'b')
    plt.plot(c3x,c3y,'g')
    #plt.legend()
    plt.pause(0.001)
    