#!python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config

class ret_fit:
  real_ret = {}
  fun_name = "hyperbolic"
  params = []
  covariance = []
  
  def __init__(self, ret_dict):
    self.real_ret = ret_dict
    self.params, self.covariance = curve_fit(ret_fit.tarfun, list(ret_dict.keys()), list(ret_dict.values()))
    print(self.params)
    print(self.covariance)

  def tarfun(x, a, b, c):
    return a/np.power(x, b)+c

  def fitting(self, day_num):
    yf = [1.0]
    yf+=[ret_fit.tarfun(i, *self.params) for i in range(1, day_num)]
    return yf

  def fitting_day(self, day):
    if day == 0: return 1.0
    return ret_fit.tarfun(day, *self.params)

  def ret_arr(self, days):
    ret_arr = [0]*days
    for i in range(0, days):
      if i in self.real_ret:
        ret_arr[i] = self.real_ret[i]
      else:
        ret_arr[i] = None
    return ret_arr
  

def test():
  x = range(0, config.days)

  fig, ax1 = plt.subplots()
  real = ret_fit(config.ret_real)
  # real retention rate
  ax1.plot(x, real.ret_arr(config.days), 'o', color="red", markersize=3)
  # fitting retention rate
  ax1.plot(x, real.fitting(config.days), '-', color='y')

  target = ret_fit(config.ret_target)
  # target retention rate
  ax1.plot(x, target.ret_arr(config.days), 'o', color="g", markersize=3)
  # fitting retention rate
  ax1.plot(x, target.fitting(config.days), '-', color='b')

  ax1.set_ylim(ymin=0)
  ax1.set_xlim(xmin=0)

  ax1.set_xlabel('Age')
  ax1.set_ylabel('Retention Rate', color='g')

  plt.title("Retention Fitting (Func={})".format(ret_fit.fun_name))
  plt.grid()
  plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    test()