import csv

def deltaV(i):
    global raw, bias
    tmp0 = raw[i-1].split(',')
    tmp1 = raw[i].split(',')
    return (float(tmp1[0]) - float(tmp0[0])) * (float(tmp1[2]) - bias)

data_x = []
data_y = []

import matplotlib.pyplot as plt

f = open("武汉-红安西.csv")
raw = f.readlines()
n = len(raw)
spd = 0
bias = 0

for i in range(500,1500):
    tmp = raw[i].split(',')
    bias += float(tmp[2])
bias /= 1000
bias += 0.026
print('bias = ', bias)

for i in range(6000,n):
    spd += deltaV(i)
    tmp1 = raw[i].split(',')
    data_x.append(float(tmp1[0]))
    data_y.append(spd*(3.6))

fig, nx = plt.subplots()
line, = nx.plot([], [], 'b-',color="blue")  # 空线条
nx.set_xlim(15, 1360)
nx.set_ylim(-15, 250)
line.set_data(data_x,data_y)
plt.show()

