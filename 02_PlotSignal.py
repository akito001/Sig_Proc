from matplotlib import pyplot as plt
from matplotlib import style

x = [1,2,3,4,5,6]
y = [7,5,6,7,8,9]

x2 = [1,2,3,4,5,6]
y2 = [3,6,5,7,8,6]

#algoritma
style.use('dark _background')
plt.plot(x,y,label = 'LIne one')
plt.plot(x2,y2,label = 'LIne two')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Simple Chart')

plt.legend()
plt.show()