from random import random
from math import exp

class Neuron:

  def __init__(self):
    self.w = [random() for i in range(2)]
    #self.w = [random() for i in range(3)]
    self.b = random()
    self.alpha = 0.15

  def set_x(self, x):
    self.x = x
  
  def set_y(self, y):
    self.y = y

  def print_me(self):
    print("Neuron:")
    for i in range(len(self.w)):
      print('w[{i}]={w}'.format(i=i, w=self.w[i]))
    print('b={b}'.format(b=self.b))

  def sum(self):
    sum = 0
    for i in range(len(self.x)):
      sum += self.x[i] * self.w[i]
    return sum
  
  def sigmoid(self, x):
    return 1 / (1 + exp(-x))

  def d_sigmoid(self, x):
    return self.sigmoid(x) * (1 - self.sigmoid(x))

  def error2(self, received, expected):
    return ((expected - received)**2) / 2

  def delta(self):
    z = self.sum() + self.b
    y = self.sigmoid(z)
    dy = self.d_sigmoid(z)
    y0 = self.y

    return (y0 - y) * (-dy)

  def gradient(self):
    d = self.delta()
    return [d*x for x in self.x]

  def update(self):
    gradient = self.gradient()

    for i in range(len(self.w)):
      self.w[i] -= gradient[i] * self.alpha
    
    self.b -= self.delta() * self.alpha

  def calc_y(self):
    return self.sigmoid(self.sum() + self.b)