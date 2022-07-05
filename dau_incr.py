#!python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from dau_decr import init_dau
import config
import retention
import dau_decr

# reg_date > 20220617
dau_real_from_new = {
  1:  13047,
  2:  19701,
  3:  22959,
  4:  25712,
  5:  28293,
  6:  30630,
  7:  31668,
  8:  33180,
  9:  35518,
  10: 36995,
  11: 38213,
  12: 37728,
  13: 39389,
  14: 39480,
  15: 41528,
  16: 43716,
}

def dau_real_from_new_arr(days):
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
  ret_arr = retention.ret_fitting(1000)
  x = range(config.days)
  fig, ax1 = plt.subplots()
  ax1.set_xlabel('Age')
  ax2 = ax1.twinx()
  # real retention rate
  ax1.plot(x, retention.ret_real_arr(config.days), 'o', color="red", markersize=3)
  # fitting retention rate
  ax1.plot(x, ret_arr[:config.days], '-', color='g')
  ax1.set_ylabel('Retention Rate', color='g')

  # simulation dau curve
  sim_dau = dau_calc(ret_arr)
  ax2.plot(range(0, config.days), sim_dau, color="b")
  ax2.plot(range(0, config.days), dau_real_from_new_arr(config.days), 'o', color="y")

  ax2.set_ylabel('DAU', color='b')

  ax1.set_ylim(ymin=0)
  ax1.set_xlim(xmin=0)
  ax2.set_ylim(ymin=0)
  ax2.set_xlim(xmin=0)


  plt.title("DAU Predict (DNU={},Func={})".format(config.dnu, retention.fun_name))
  plt.grid()
  plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()

