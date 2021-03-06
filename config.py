#!python3

days = 90
dnu = 13000

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

ret_target = {
  1: 0.45,
  7: 0.17,
  30: 0.08,
}

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

# reg_date <= 20220617
stock_dau_real = {
  0:  51332,
  1:  38437,
  2:  34738,
  3:  32093,
  4:  31715,
  5:  31585,
  6:  30988,
  7:  28766,
  8:  27803,
  9:  27203,
  10: 27144,
  11: 26690,
  12: 24636,
  13: 25228,
  14: 24133,
  15: 24350,
  16: 23617,
}

# age: dau
init_dau = {
  0: 13409,
  1: 4853,
  2: 2363,
  3: 1649,
  4: 1518,
  5: 1378,
  6: 1157,
  7: 1074,
  8: 1025,
  9: 821,
  10: 711,
  11: 632,
  12: 582,
  13: 552,
  14: 504,
  15: 491,
  16: 455,
  17: 466,
  18: 384,
  19: 389,
  20: 334,
  21: 346,
  22: 363,
  23: 389,
  24: 408,
  25: 375,
  26: 336,
  27: 333,
  28: 306,
  29: 297,
  30: 341,
  31: 302,
  32: 286,
  33: 310,
  34: 327,
  35: 270,
  36: 262,
  37: 250,
  38: 266,
  39: 244,
  40: 208,
  41: 247,
  42: 221,
  43: 181,
  44: 175,
  45: 141,
  46: 139,
  47: 98,
  48: 169,
  49: 140,
  50: 145,
  51: 132,
  52: 127,
  53: 138,
  54: 56,
  55: 143,
  56: 106,
  57: 153,
  58: 152,
  59: 127,
  60: 146,
  61: 130,
  62: 148,
  63: 115,
  64: 108,
  65: 142,
  66: 100,
  67: 108,
  68: 127,
  69: 121,
  70: 125,
  71: 101,
  72: 90,
  73: 99,
  74: 97,
  75: 105,
  76: 135,
  77: 155,
  78: 108,
  79: 107,
  80: 102,
  81: 76,
  82: 75,
  83: 77,
  84: 89,
  85: 91,
  86: 63,
  87: 78,
  88: 69,
  89: 76,
  90: 72,
  91: 77,
  92: 89,
  93: 71,
  94: 68,
  95: 67,
  96: 50,
  97: 73,
  98: 61,
  99: 71,
  100: 60,
  101: 87,
  102: 63,
  103: 60,
  104: 52,
  105: 34,
  106: 35,
  107: 29,
  108: 22,
  109: 30,
  110: 31,
  111: 43,
  112: 31,
  113: 35,
  114: 27,
  115: 52,
  116: 52,
  117: 54,
  118: 49,
  119: 39,
  120: 32,
  121: 34,
  122: 13,
  123: 27,
  124: 2,
  125: 2,
  126: 1,
  127: 1,
  128: 5,
  129: 1,
  130: 3,
  131: 2,
  132: 6,
  133: 1,
  134: 6,
  135: 4,
  136: 4,
  137: 6,
  138: 1,
  139: 5,
  140: 4,
  141: 6,
  142: 7,
  143: 53,
  144: 71,
  145: 91,
  146: 93,
  147: 89,
  148: 89,
  149: 91,
  150: 67,
  151: 99,
  152: 149,
  153: 139,
  154: 145,
  155: 135,
  156: 120,
  157: 101,
  158: 94,
  159: 75,
  160: 27,
  161: 40,
  162: 41,
  163: 38,
  164: 33,
  165: 35,
  166: 51,
  167: 42,
  168: 29,
  169: 17,
  170: 29,
  171: 34,
  172: 27,
  173: 45,
  174: 57,
  175: 22,
  176: 24,
  177: 14,
  178: 9,
  179: 12,
  180: 10,
  181: 13,
  182: 6,
  183: 10,
  184: 17,
  185: 26,
  186: 10,
  187: 5,
  188: 2,
  189: 3,
  190: 1,
  191: 1,
  192: 1,
  193: 2,
  194: 2,
  195: 2,
  196: 4,
  197: 5,
  198: 1,
  199: 2,
  200: 2,
  201: 11,
  202: 2,
  203: 1,
  204: 2,
  205: 1,
  208: 1,
  209: 7,
  212: 2,
  213: 1,
  214: 1,
  220: 1,
  221: 2,
  222: 3,
  223: 5,
  224: 5,
  225: 4,
  226: 12,
  227: 4,
  228: 7,
  229: 6,
  230: 2,
  231: 1,
  232: 3,
  233: 1,
  234: 6,
  235: 3,
  236: 2,
  237: 1,
  238: 1,
  239: 10,
  240: 7,
  241: 11,
  242: 7,
  243: 9,
  244: 11,
  245: 6,
  246: 3,
  247: 7,
  248: 21,
  249: 8,
  250: 3,
  251: 2,
  252: 1
}

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
