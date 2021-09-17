import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.random.randn(1000, 100)#1000個のデータ

node_num = 100#各隠れ層のノード（ニューロン）の数
hidden_layer_size = 5#隠れ層が5層
activations = {}

for i in range(hidden_layer_size):
    if i !=0:
        x = activations[i-1]

    #w = np.random.randn(node_num, node_num) * 1
    w = np.random.randn(node_num, node_num) * 0.01


    z = np.dot(x, w)
    a = sigmoid(z)#シグモイド関数
    activations[i] = a

for i,a in activations.items():
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()