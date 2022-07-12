#!python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config
import retention
import dau_decr

def dau_real_from_new_arr(days, dau_real_from_new):
  dau_arr = [0]*days
  for i in range(0, days):
    if i in dau_real_from_new:
      dau_arr[i] = dau_real_from_new[i]
    else:
      dau_arr[i] = None
  return dau_arr

def dau_calc(ret_arr):
  dau_n = [0] * config.days
  for d in range(1, config.days):
    for dd in range(0, d):
      dau_n[d] += config.dnu * ret_arr[dd]
  return dau_n


def main():
  ret = retention.ret_fit(config.ret_real)
  x = range(config.days)
  fig, ax1 = plt.subplots()
  ax1.set_xlabel('Age')
  ax2 = ax1.twinx()
  # real retention rate
  ax1.plot(x, ret.ret_arr(config.days), 'o', color="red", markersize=3)
  # fitting retention rate
  ax1.plot(x, ret.fitting(config.days), '-', color='g')
  ax1.set_ylabel('Retention Rate', color='g')

  # simulation dau curve
  sim_dau = dau_calc(ret.fitting(config.days))
  ax2.plot(range(0, config.days), sim_dau, color="b")
  ax2.plot(range(0, config.days), dau_real_from_new_arr(config.days, config.dau_real_from_new), 'o', color="y")

  ax2.set_ylabel('DAU', color='b')

  ax1.set_ylim(ymin=0)
  ax1.set_xlim(xmin=0)
  ax2.set_ylim(ymin=0)
  ax2.set_xlim(xmin=0)


  plt.title("DAU Predict (DNU={},Func={})".format(config.dnu, ret.fun_name))
  plt.grid()
  plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()

