#!python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import config
import retention
import dau_decr
import dau_incr

def dau_real_arr(days):
  dau_arr = [0]*days
  for i in range(0, days):
    if i in config.dau_real:
      dau_arr[i] = config.dau_real[i]
    else:
      dau_arr[i] = None
  return dau_arr


x = range(config.days)
ret = retention.ret_fit(config.ret_real)
ret_target = retention.ret_fit(config.ret_target)

fig, ax1 = plt.subplots()
ax1.set_xlabel('Age')
ax2 = ax1.twinx()
# real retention rate
ax1.plot(x, ret.ret_arr(config.days), 'o', color="red", markersize=3)
# fitting retention rate
ax1.plot(x, ret.fitting(config.days), '-', color='r')
ax1.set_ylabel('Retention Rate', color='r')

# simulation dau curve
sim_dau = dau_incr.dau_calc(ret.fitting(config.days))
sim_dau2 = dau_incr.dau_calc(ret_target.fitting(config.days))
stock_dau = dau_decr.calc_stock_dau(ret, config.days, config.init_dau) 

ax2.plot(range(0, config.days), np.add(sim_dau,stock_dau), color="g")
ax2.plot(range(0, config.days), np.add(sim_dau2,stock_dau), color="b")
ax2.plot(range(0, config.days), dau_real_arr(config.days), color="y")

ax2.set_ylabel('DAU', color='b')

ax1.set_ylim(ymin=0)
ax1.set_xlim(xmin=0)
ax2.set_ylim(ymin=0)
ax2.set_xlim(xmin=0)


plt.title("DAU Predict (DNU={},Func={})".format(config.dnu, ret.fun_name))
plt.grid()
plt.show()

