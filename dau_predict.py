#!python

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

days = 100
dnu = 13000
retn = {
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
  if n in retn:
    return retn[n]
  return None

x = range(1, days)
y = [ret(i) for i in x]

fun_name = "hyperbolic"
def fun(x, a, b, c):
  return a/np.power(x, b)+c

def dau_calc(fun):
  dau_n = [dnu] * days
  for d in range(1, days):
    for dd in range(1, d):
      dau_n[d] += dnu * fun(dd)
  return dau_n

#fun_name = "exponent"
#def fun(x, a, b, c):
#  return a * np.power(math.e, -1*b*x)+c

params, covariance = curve_fit(fun, list(retn.keys()), list(retn.values()))
fun1 = lambda x: fun(x, params[0], params[1], params[2])

print(params, covariance)
yf = [fun(i, params[0], params[1], params[2]) for i in x]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
# real retention rate
ax1.plot(x, y, 'o', color="red", markersize=3)
# fitting retention rate
ax1.plot(x, fun1(x), '-', color='b')
# simulation dau curve
ax2.plot(range(0, days), dau_calc(fun1), color="b")

ax1.set_ylim(ymin=0)
ax1.set_xlim(xmin=0)
ax2.set_ylim(ymin=0)
ax2.set_xlim(xmin=0)

ax1.set_xlabel('Age')
ax1.set_ylabel('Retention Rate', color='g')
ax2.set_ylabel('DAU', color='b')

plt.title("DAU Predict (DNU={},Func={})".format(dnu, fun_name))
plt.grid()
plt.show()

