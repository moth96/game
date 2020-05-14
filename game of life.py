import matplotlib.pyplot  as plt
import random

mesh_range = 11
current_life = [[] for i in range(mesh_range)]
new_life = [[] for i in range(mesh_range)]

def random_initialization(current_life,mesh_range):
    for i in range(mesh_range):
        for j in range(mesh_range):
            current_life[i].append(random.randint(0,1))

def count_condition(current_life,mesh_range,point):
    if point[0] == 0:
        if point[1] == 0:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]+1] + current_life[point[0]+1][point[1]+1]
        elif point[1] == mesh_range - 1:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]-1] + current_life[point[0]+1][point[1]-1]
        else:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]-1] + current_life[point[0]+1][point[1]-1] + current_life[point[0]][point[1]+1] + current_life[point[0]+1][point[1]+1]
    elif point[0] == mesh_range - 1:
        if point[1] == 0:
            condition = current_life[point[0]-1][point[1]] + current_life[point[0]][point[1]+1] + current_life[point[0]-1][point[1]+1]
        elif point[1] == mesh_range - 1:
            condition = current_life[point[0]-1][point[1]] + current_life[point[0]][point[1]-1] + current_life[point[0]-1][point[1]-1]
        else:
            condition = current_life[point[0]-1][point[1]] + current_life[point[0]][point[1]-1] + current_life[point[0]-1][point[1]-1] + current_life[point[0]][point[1]+1] + current_life[point[0]-1][point[1]+1]
    else:
        if point[1] == 0:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]+1] + current_life[point[0]+1][point[1]+1] + current_life[point[0]-1][point[1]] + current_life[point[0]-1][point[1]+1]
        elif point[1] == mesh_range - 1:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]-1] + current_life[point[0]+1][point[1]-1] + current_life[point[0]-1][point[1]] + current_life[point[0]-1][point[1]-1]
        else:
            condition = current_life[point[0]+1][point[1]] + current_life[point[0]][point[1]+1] + current_life[point[0]+1][point[1]+1] + current_life[point[0]-1][point[1]] + current_life[point[0]-1][point[1]+1] + current_life[point[0]][point[1]-1] + current_life[point[0]+1][point[1]-1] + current_life[point[0]-1][point[1]-1]
    return condition
    
def update(current_life,mesh_range,point):
    condition = count_condition(current_life,mesh_range,point)
    if condition == 3:
        new_life[point[0]][point[1]] = 1
    elif condition == 2:
        pass
    else:
        new_life[point[0]][point[1]] = 0
    
    
    
random_initialization(current_life,mesh_range)
random_initialization(new_life,mesh_range)

k = 0
plt.ion()
plt.figure(1)
while True:
    for i in range(mesh_range):
        for j in range(mesh_range):
            update(current_life,mesh_range,[i,j])
    current_life = new_life[:][:]
    k = k + 1
    print(k)
    #plt.set_tittle("k")
    plt.imshow(current_life,cmap = plt.cm.gray)
    plt.show()
    plt.pause(0.01)



