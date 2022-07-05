#!python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config

ret_real = {
  1: 0.423,
  2: 0.270,
  3: 0.216,
  4: 0.183,
  5: 0.160,
  6: 0.144,
  7: 0.132,
  14: 0.089,
  30: 0.053,
}

def ret(n):
  if n in ret_real:
    return ret_real[n]
  return None


def ret_real_arr(day_num):
  y = [1.0]
  y += [ret(x) for x in range(1,day_num)]
  return y


ret_target = {
  1: 0.45,
  7: 0.17,
  30: 0.08,
}

def ret_target_arr(days):
  ret_arr = [0]*days
  for i in range(0, days):
    if i in ret_target:
      ret_arr[i] = ret_target[i]
    else:
      ret_arr[i] = None
  return ret_arr


fun_name = "hyperbolic"
def tarfun(x, a, b, c):
  return a/np.power(x, b)+c


#fun_name = "exponent"
#def tarfun(x, a, b, c):
#  return a * np.power(math.e, -1*b*x)+c

#def ret_fitting_day(day):
#  params, covariance = curve_fit(tarfun, list(ret_real.keys()), list(ret_real.values()))
#  print(params, covariance)
#  return tarfun(day, params[0], params[1], params[2])


def ret_fitting(day_num):
  params, covariance = curve_fit(tarfun, list(ret_real.keys()), list(ret_real.values()))
  print(params)
  print(covariance)
  yf = [1.0]
  yf+=[tarfun(i, params[0], params[1], params[2]) for i in range(1, day_num)]
  return yf


def ret_target_fitting(day_num):
  params, covariance = curve_fit(tarfun, list(ret_target.keys()), list(ret_target.values()))
  print(params)
  print(covariance)
  yf = [1.0]
  yf+=[tarfun(i, params[0], params[1], params[2]) for i in range(1, day_num)]
  return yf


def main():
  x = range(0, config.days)

  fig, ax1 = plt.subplots()
  # real retention rate
  ax1.plot(x, ret_real_arr(config.days), 'o', color="red", markersize=3)
  # fitting retention rate
  ax1.plot(x, ret_fitting(config.days), '-', color='y')

  # target retention rate
  ax1.plot(x, ret_target_arr(config.days), 'o', color="g", markersize=3)
  # fitting retention rate
  ax1.plot(x, ret_target_fitting(config.days), '-', color='b')

  ax1.set_ylim(ymin=0)
  ax1.set_xlim(xmin=0)

  ax1.set_xlabel('Age')
  ax1.set_ylabel('Retention Rate', color='g')

  plt.title("Retention Fitting (Func={})".format(fun_name))
  plt.grid()
  plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    main()