import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.ion()

def singular_input(left,right):
    input = ""
    for i in np.arange(0,left):
        input += "0"
    input += "1"
    for i in np.arange(0,right):
        input += "0"
    return input

def ECA(input, timesteps, rule, figx = 8, figy =12, grid=False):

    if isinstance(input,str):
        input = np.array([int(c) for c in input])

    history = np.zeros((timesteps,len(input)))

    history[0] = input

    for t in range(1,history.shape[0]):
        for i in range(0,history.shape[1]):
            history[t,i] = update_ECA(history,t,i,rule)

    plt.figure(figsize=(figx,figy))
    if grid:
        for y in np.arange(-1,history.shape[0]):
            plt.axhline(y+0.5,color='gray',alpha=0.4)
        for x in np.arange(-1,history.shape[1]):
            plt.axvline(x+0.5,color='gray',alpha=0.4)
    plt.imshow(history,cmap='binary')
    plt.axis('off')
    plt.tight_layout()

def update_ECA(history,t,i,rule):

    r = bin(rule)[2:].zfill(8)

    if i-1 < 0:
        a = history[t - 1, -1]
    else:
        a = history[t - 1, i - 1]

    b = history [t-1,i]

    if i+1 >= history.shape[1]:
        c = history [t-1,0]
    else:
        c = history [t-1,i+1]

    if a == 1 and b == 1 and c == 1:
        return int(r[0])
    if a == 1 and b == 1 and c == 0:
        return int(r[1])
    if a == 1 and b == 0 and c == 1:
        return int(r[2])
    if a == 1 and b == 0 and c == 0:
        return int(r[3])
    if a == 0 and b == 1 and c == 1:
        return int(r[4])
    if a == 0 and b == 1 and c == 0:
        return int(r[5])
    if a == 0 and b == 0 and c == 1:
        return int(r[6])
    if a == 0 and b == 0 and c == 0:
        return int(r[7])

    print("No rule")
    return 0

