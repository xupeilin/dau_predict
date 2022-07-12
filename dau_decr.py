#!/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config
import retention


def stock_dau_real_arr(days, stock_dau_real):
  dau_arr = [0]*days
  for i in range(0, days):
    if i in stock_dau_real:
      dau_arr[i] = stock_dau_real[i]
    else:
      dau_arr[i] = None
  return dau_arr


def dau_sum(dau_age=dict()):
  total_dau = 0
  for age, dau in dau_age.items():
    total_dau += dau
  return int(total_dau)

def calc_stock_dau(ret, days, init_dau):
#  print("ret_arr len:", len(ret_arr), ret_arr)

  dau_mat = [{}]*(days)
  dau_mat[0] = init_dau
  #  print("x[:days]", x[:days])
  for i in range(1, days):
    dau_mat[i] = {}
    #  print("dau_mat", i, len(dau_mat[i-1]))
    for age, dau in dau_mat[i-1].items():
      ret_dau = dau * ret.fitting_day(age+1)/ret.fitting_day(age)
      dau_mat[i][age+1] = ret_dau
      #print("retdau calu ", age, dau, ret_dau, ret_arr[age],ret_arr[age+1]/ret_arr[age])

  dau_arr = [0]*(days)
  for i in range(0, days):
    dau_arr[i] = dau_sum(dau_mat[i])
    #  print("dau", i, dau_arr[i], ret_arr[i])
  return dau_arr

def main():
  ret = retention.ret_fit(config.ret_real)
  dau_arr = calc_stock_dau(ret, config.days, config.init_dau)
  dau_arr2 = stock_dau_real_arr(config.days, config.stock_dau_real)

  x = range(0, config.days)
  fig, ax1 = plt.subplots()
  ax2 = ax1.twinx()
  # fitting retention rate
  ax1.plot(x, ret.fitting(config.days), '-', color="g")
  # real retention rate
  ax1.plot(x, ret.ret_arr(config.days), 'o', color="r", markersize=2)
  ax1.set_ylabel('Retention Rate', color='r')

  ax2.plot(x, dau_arr, '-', color='b')
  ax2.plot(x, dau_arr2, '-', color='y')
  ax2.set_ylabel('DAU', color='b')

  ax1.set_ylim(ymin=0)
  ax1.set_xlim(xmin=0)
  ax2.set_ylim(ymin=0)
  ax2.set_xlim(xmin=0)

  ax1.set_xlabel('Age')

  plt.title("Stock DAU Predict")
  plt.grid()
  plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()