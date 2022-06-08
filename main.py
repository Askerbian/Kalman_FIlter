import matplotlib.pyplot as plt
from kalman_updated import Kalman_1D
import numpy as np
from math import sin,radians
from random import randint
lv=[]
real=[]
for _ in range(1000):
      value = randint(-10,10)
      sin1= 5*sin(radians(_))+value
      sin2 = 5 * sin(radians(_))
      lv.append(sin1)
      real.append((sin2))

print(lv)
kalm=Kalman_1D()
l=[]
for i in range(1000):

  y=kalm.predict(lv[i])
  l.append(y)
plt.plot(real)
plt.plot(lv)
plt.plot(l)
plt.show()
