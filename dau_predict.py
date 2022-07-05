#!python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config
import retention
import dau_decr
import dau_incr

#start from 20220617
dau_real = {
  0: 51332,
  1: 51484,
  2: 54439,
  3: 55052,
  4: 57427,
  5: 59878,
  6: 61618,
  7: 60434,
  8: 60983,
  9: 62721,
  10: 64139,
  11: 64903,
  12: 62364,
  13: 64617,
  14: 63613,
  15: 65878,
  16: 67333,
}

def dau_real_arr(days):
  dau_arr = [0]*days
  for i in range(0, days):
    if i in dau_real:
      dau_arr[i] = dau_real[i]
    else:
      dau_arr[i] = None
  return dau_arr


x = range(config.days)
ret_arr = retention.ret_fitting(1000)

fig, ax1 = plt.subplots()
ax1.set_xlabel('Age')
ax2 = ax1.twinx()
# real retention rate
ax1.plot(x, retention.ret_real_arr(config.days), 'o', color="red", markersize=3)
# fitting retention rate
ax1.plot(x, ret_arr[:config.days], '-', color='r')
ax1.set_ylabel('Retention Rate', color='r')

# simulation dau curve
sim_dau = dau_incr.dau_calc(retention.ret_fitting(1000))
sim_dau2 = dau_incr.dau_calc(retention.ret_target_fitting(1000))
stock_dau = dau_decr.calc_stock_dau(np.array(ret_arr)) 

ax2.plot(range(0, config.days), np.add(sim_dau,stock_dau), color="g")
ax2.plot(range(0, config.days), np.add(sim_dau2,stock_dau), color="b")
ax2.plot(range(0, config.days), dau_real_arr(config.days), color="y")

ax2.set_ylabel('DAU', color='b')

ax1.set_ylim(ymin=0)
ax1.set_xlim(xmin=0)
ax2.set_ylim(ymin=0)
ax2.set_xlim(xmin=0)


plt.title("DAU Predict (DNU={},Func={})".format(config.dnu, retention.fun_name))
plt.grid()
plt.show()

