import numpy as np
import time
import matplotlib.pyplot as plt

def check_surroundings(map,y,x):

    if y+1 >= map.shape[0]:
        U = 0
    else:
        U = y+1

    if y-1 < 0:
        D = map.shape[0]-1
    else:
        D = y-1

    if x+1 >= map.shape[1]:
        R = 0
    else:
        R = x+1

    if x-1 < 0:
        L = map.shape[1]-1
    else:
        L = x-1

    neighbors = map[U,L] + map[U,x] + map[U,R] + map[y,L] + map[y,R] + map[D,L] + map[D,x] + map[D,R]

    if map[y,x] == 1:
        if neighbors <= 1:
            return 0
        elif neighbors >= 2 and neighbors <= 3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0


def update_GoL(map):

    temp = np.zeros(map.shape)

    for y in range(map.shape[0]):
        for x in range(map.shape[1]):
            temp[y,x] = check_surroundings(map,y,x)

    return temp

def run_GoL(map, duration = 0):

    t = 0

    figure, ax = plt.subplots(figsize=(10,10))
    ax = plt.imshow(map,cmap='binary')
    plt.axis("off")
    plt.tight_layout()

    for y in np.arange(-1,map.shape[0]):
        plt.axhline(y+0.5,color='gray',alpha=0.4)
    for x in np.arange(-1,map.shape[1]):
        plt.axvline(x+0.5,color='gray',alpha=0.4)

    while t <= duration:
        map = update_GoL(map)
        ax.set_data(map)

        if duration == 0:
            t = 0
        else:
            t+=1

        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.1)



