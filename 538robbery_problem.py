import numpy as np

# A town of 1,000 households has a strange law intended to prevent wealth-hoarding. 
# On January 1 of every year, each household robs one other household, selected at 
# random, moving all of that house’s money into their own house. The order in which 
# the robberies take place is also random and is determined by a lottery. (Note that 
# if House A robs House B first, and then C robs A, the houses of A and B would each 
# be empty and C would have acquired the resources of both A and B.)
#
# Two questions about this fateful day:
#
# 1. What is the probability that a house is not robbed over the course of the day?
#
# 2. Suppose that every house has the same amount of cash to begin with — say $100. 
#    Which position in the lottery has the most expected cash at the end of the day, 
#    and what is that amount?


# Question 1 is pretty straightforward. A given household could be robbed by any of 
# the 999 other households. The probability that a household isn't robbed after one
# of these 999 robberies is 998/999. The probability that it isn't robbed after two 
# is (998/999) squared. The probability that it isn't robbed after all 999 robberies 
# is (998/999) to the 999th power, i.e.,

p_not_robbed = (998/999.)**999  #which is about 0.3677.


# To answer Question 2, I just modeled the situation and simulated it a bunch of times.

def sim_one_robbery_day():
    houses = np.ones(1000) * 100 #each house starts with $100
    robber = 0
    for i in range(1000):
        house_to_rob = np.random.randint(1000)
        while house_to_rob == robber:
            house_to_rob = np.random.randint(1000)
        else:
            houses[robber] += houses[house_to_rob]
            houses[house_to_rob] = 0
        robber += 1
    return houses #returns a list of the cash each house ended up with

def sim_many_robbery_days(n):
    houses = np.zeros(1000)
    for i in range(n):
        houses = np.add(houses, sim_one_robbery_day())
    return houses/float(n) #returns a list of the average cash each house ended up with


# sim_many_robbery_days(1000000) yielded the array below. The higher a household's place 
# in the lottery, the more cash they're likely to end up with. This makes a lot of sense, 
# intuitively. The most cash that the house that robs first can end up with is $200.
# Houses that rob later in the day can potentially rob a house that already robbed a house
# that already robbed a house, etc.

# It is best to go last. The house that robs last ends up with a little less than $137, 
# on average.

 
expected_values = np.array(
      [  73.522 ,   73.4922,   73.6049,   73.9902,   73.9585,   73.6509,
         73.6635,   73.7385,   73.8224,   73.848 ,   73.8579,   74.0374,
         74.0542,   74.0282,   74.103 ,   74.0851,   74.3836,   74.0718,
         74.2912,   74.2565,   74.224 ,   74.3808,   74.4631,   74.2519,
         74.3802,   74.6082,   74.3605,   74.3702,   74.8543,   74.5336,
         74.7229,   74.7218,   74.7   ,   74.7616,   74.8829,   74.7802,
         74.9537,   75.0437,   75.0173,   75.0868,   74.9672,   75.1921,
         75.2146,   75.1996,   75.1056,   75.3831,   75.2368,   75.2473,
         75.2882,   75.2715,   75.5926,   75.4636,   75.4832,   75.5525,
         75.5477,   75.5568,   75.6117,   75.5913,   75.6302,   75.6256,
         75.7163,   75.7715,   76.0793,   75.9733,   75.9308,   76.0841,
         75.9968,   76.1372,   76.1206,   76.1188,   76.0961,   76.2198,
         76.3312,   76.1609,   76.3225,   76.3772,   76.5636,   76.6237,
         76.6124,   76.6084,   76.6372,   76.6653,   76.7057,   76.5532,
         76.7776,   76.8806,   76.6482,   77.0038,   77.0517,   76.783 ,
         76.8167,   77.0682,   77.0209,   77.1349,   77.1451,   77.1207,
         77.2468,   77.3164,   77.2978,   77.5236,   77.3557,   77.3883,
         77.4299,   77.5951,   77.5929,   77.698 ,   77.6094,   77.7499,
         77.7792,   77.7266,   77.6597,   77.8143,   77.7791,   77.7985,
         78.0751,   78.045 ,   78.0545,   78.0506,   78.0338,   78.2455,
         78.0931,   78.1135,   78.3403,   78.1925,   78.4682,   78.2967,
         78.5866,   78.4907,   78.4655,   78.6893,   78.7126,   78.691 ,
         78.662 ,   78.7747,   78.6475,   79.0249,   78.784 ,   78.9396,
         78.9612,   78.7977,   79.1601,   79.2522,   79.2949,   79.102 ,
         79.1142,   79.3326,   79.3983,   79.1473,   79.4199,   79.5891,
         79.3651,   79.3994,   79.4839,   79.5453,   79.7177,   79.833 ,
         79.7841,   79.6256,   79.8713,   79.9841,   79.8916,   80.0004,
         79.9703,   79.9008,   80.0037,   80.2248,   80.2315,   80.3151,
         80.2557,   80.2743,   80.3661,   80.2555,   80.3198,   80.441 ,
         80.5018,   80.4863,   80.6478,   80.6081,   80.728 ,   80.6822,
         80.8133,   80.9161,   80.8611,   80.8927,   80.9541,   81.1214,
         80.9728,   81.1826,   81.1512,   81.2943,   81.2191,   81.3145,
         81.3885,   81.4533,   81.5376,   81.3307,   81.4017,   81.6407,
         81.6004,   81.5545,   81.5238,   81.6711,   81.7044,   81.8277,
         81.9578,   81.8549,   82.0164,   81.9994,   82.0841,   82.1084,
         82.0416,   82.2355,   82.2128,   82.2674,   82.3708,   82.4427,
         82.453 ,   82.3046,   82.3827,   82.5271,   82.5335,   82.6032,
         82.823 ,   82.6816,   82.8236,   82.9039,   82.8187,   82.8151,
         83.0625,   83.012 ,   83.0169,   83.3422,   83.1579,   83.3235,
         83.0783,   83.3092,   83.1793,   83.2945,   83.4999,   83.4085,
         83.6231,   83.6145,   83.4826,   83.83  ,   83.7028,   83.7276,
         83.8878,   83.8145,   83.9436,   84.1557,   84.0663,   83.9255,
         84.1532,   84.3001,   84.2137,   84.2783,   84.2427,   84.1613,
         84.3488,   84.4379,   84.3416,   84.3447,   84.5226,   84.6791,
         84.7478,   84.4656,   84.7465,   84.6715,   84.61  ,   84.7948,
         85.1159,   85.0957,   85.1394,   85.1334,   84.9965,   85.1498,
         85.1471,   85.339 ,   85.3622,   85.4958,   85.2957,   85.4134,
         85.5329,   85.6337,   85.6723,   85.6803,   85.6525,   85.6607,
         85.7839,   85.6225,   85.7308,   86.0091,   85.9098,   86.0473,
         86.1383,   86.1587,   86.1838,   86.0893,   86.3438,   86.2164,
         86.3581,   86.3626,   86.5816,   86.622 ,   86.5666,   86.8329,
         86.5668,   86.7331,   86.7691,   86.9893,   86.7747,   87.0169,
         87.0592,   87.2382,   87.2205,   87.0196,   87.0241,   87.2317,
         87.4119,   87.4318,   87.6744,   87.5088,   87.4453,   87.5525,
         87.629 ,   87.4979,   87.8474,   87.6728,   87.8346,   87.8902,
         88.1039,   88.0994,   87.9831,   88.1889,   88.1939,   88.2664,
         88.4454,   88.1914,   88.4165,   88.444 ,   88.3548,   88.4319,
         88.587 ,   88.513 ,   88.5056,   88.5035,   88.674 ,   88.8036,
         88.9027,   88.9628,   89.0646,   89.1229,   89.1794,   89.1915,
         89.2001,   89.2644,   89.4786,   89.3256,   89.3921,   89.4501,
         89.5192,   89.5656,   89.7514,   89.4264,   89.4513,   89.5314,
         89.6371,   89.8335,   89.7891,   89.9689,   90.2344,   90.3609,
         90.0304,   90.1458,   90.4045,   90.3055,   90.206 ,   90.596 ,
         90.4448,   90.3742,   90.5173,   90.6636,   90.6844,   90.6162,
         90.7931,   91.0108,   90.9375,   91.0935,   90.983 ,   91.2772,
         91.1091,   91.1711,   91.1564,   91.4084,   91.2186,   91.4803,
         91.3619,   91.2974,   91.49  ,   91.3692,   91.6062,   91.7893,
         91.8221,   91.6982,   91.7502,   91.7811,   92.1639,   91.8502,
         92.1105,   92.0503,   92.2328,   92.4455,   92.3642,   92.3327,
         92.5645,   92.5602,   92.4605,   92.399 ,   92.7299,   92.7678,
         92.6102,   92.7891,   92.9045,   92.8342,   92.885 ,   93.0056,
         93.0738,   93.0989,   93.2959,   93.3102,   93.3401,   93.5008,
         93.4582,   93.3675,   93.4674,   93.6087,   93.5715,   93.7228,
         93.6667,   93.7549,   93.8371,   93.8984,   93.9928,   93.9679,
         94.1847,   94.1559,   94.3023,   94.1847,   94.4258,   94.3087,
         94.4051,   94.6236,   94.5311,   94.6021,   94.6546,   94.6773,
         94.7845,   94.719 ,   94.9006,   95.112 ,   95.0273,   95.07  ,
         95.016 ,   95.2313,   95.3082,   95.414 ,   95.4001,   95.3527,
         95.4551,   95.5329,   95.5993,   95.8673,   95.7486,   95.7447,
         95.9179,   95.9402,   96.0627,   95.9741,   96.2589,   95.9637,
         96.1552,   96.3142,   96.4447,   96.2699,   96.4171,   96.543 ,
         96.5266,   96.5162,   96.5778,   96.8502,   96.8404,   96.8323,
         97.011 ,   96.8919,   97.0447,   97.0879,   97.2212,   97.2393,
         97.1796,   97.3101,   97.3764,   97.3218,   97.5501,   97.4207,
         97.7765,   97.7385,   97.7803,   97.762 ,   98.1334,   97.7927,
         97.9831,   98.2369,   98.1857,   98.2265,   98.3771,   98.2943,
         98.4111,   98.4166,   98.6054,   98.5511,   98.6654,   98.6508,
         98.6514,   98.7647,   98.8988,   99.1914,   99.2248,   99.1811,
         99.2213,   99.3457,   99.4098,   99.2991,   99.2698,   99.4623,
         99.2686,   99.4726,   99.5166,   99.6149,   99.905 ,   99.6417,
         99.8059,  100.0365,  100.0175,  100.0604,  100.0903,  100.4492,
        100.0436,  100.3917,  100.322 ,  100.4217,  100.5179,  100.7151,
        100.4807,  100.6971,  100.73  ,  100.7967,  101.0176,  100.9699,
        101.0772,  101.0812,  101.2667,  101.1698,  101.3443,  101.358 ,
        101.4491,  101.5846,  101.2955,  101.6502,  101.7221,  101.7616,
        101.7144,  101.7346,  102.1909,  101.9431,  102.0997,  101.9964,
        102.0739,  102.0256,  102.353 ,  102.46  ,  102.3931,  102.6623,
        102.5405,  102.5836,  102.6982,  102.873 ,  102.8011,  102.9796,
        102.8391,  103.0239,  103.3227,  103.0313,  103.3366,  103.3537,
        103.4452,  103.3466,  103.5873,  103.5007,  103.7652,  103.8157,
        103.9676,  103.9079,  104.274 ,  104.0378,  103.8678,  104.1255,
        104.3492,  104.2487,  104.3055,  104.2982,  104.4064,  104.4907,
        104.5376,  104.6375,  104.5623,  104.9099,  105.0348,  105.0149,
        105.1775,  104.9798,  105.2388,  105.2132,  105.3706,  105.3448,
        105.5547,  105.4125,  105.5759,  105.6765,  105.575 ,  105.7439,
        106.0048,  105.9488,  105.8621,  105.8944,  106.2112,  106.1958,
        106.2472,  106.3311,  106.3549,  106.6717,  106.3835,  106.7005,
        106.4278,  106.6959,  106.6726,  106.8131,  106.897 ,  106.906 ,
        106.9983,  107.1301,  107.3574,  107.1259,  107.2517,  107.497 ,
        107.4312,  107.5116,  107.5784,  107.5064,  107.8183,  107.6982,
        107.8311,  107.9941,  108.1674,  108.2698,  108.3633,  108.4707,
        108.3723,  108.1928,  108.4259,  108.6164,  108.7502,  108.7781,
        108.7634,  108.5877,  108.7896,  108.8972,  109.1543,  109.0536,
        109.2474,  109.2112,  109.1981,  109.5066,  109.5744,  109.5133,
        109.7818,  109.8684,  109.7626,  109.9065,  109.9744,  110.0742,
        110.1297,  110.3343,  110.2939,  110.4442,  110.3382,  110.4508,
        110.5173,  110.481 ,  110.8824,  110.7794,  110.7827,  110.9663,
        111.001 ,  111.338 ,  111.2879,  111.2124,  111.1998,  111.2371,
        111.406 ,  111.671 ,  111.5351,  111.8192,  111.6354,  111.7368,
        111.9192,  112.2436,  112.2558,  112.0419,  112.0724,  112.397 ,
        112.0715,  112.285 ,  112.429 ,  112.5609,  112.5635,  112.5387,
        112.9556,  112.7456,  113.0909,  113.1796,  113.2279,  112.9457,
        113.3018,  113.4546,  113.3805,  113.5364,  113.5119,  113.611 ,
        113.6628,  113.8959,  113.7932,  114.0073,  114.1898,  114.3527,
        114.2469,  114.0649,  114.368 ,  114.3461,  114.5872,  114.4863,
        114.4283,  114.6502,  114.6161,  114.765 ,  114.8981,  115.073 ,
        115.101 ,  115.0891,  115.3554,  115.0474,  115.4263,  115.3991,
        115.5194,  115.6268,  115.8297,  116.104 ,  115.7198,  116.146 ,
        115.9833,  116.1023,  116.1272,  116.2267,  116.2141,  116.4999,
        116.5008,  116.6731,  116.6297,  116.9204,  116.8532,  116.7505,
        116.9224,  117.0287,  117.2124,  117.1855,  117.3776,  117.4921,
        117.557 ,  117.6485,  117.7432,  117.7534,  117.7408,  117.926 ,
        117.7921,  118.1187,  118.3518,  118.2275,  118.2268,  118.3481,
        118.3931,  118.5335,  118.788 ,  118.9521,  118.7759,  118.8948,
        118.9263,  119.3841,  119.1315,  119.0842,  119.2371,  119.396 ,
        119.4002,  119.5817,  119.6712,  119.5617,  119.8413,  119.8657,
        119.8916,  119.9739,  120.3078,  120.3007,  120.1696,  120.4612,
        120.648 ,  120.5601,  120.5434,  120.6486,  120.9651,  121.1343,
        121.0749,  120.9608,  120.989 ,  121.1341,  121.4388,  121.4555,
        121.3218,  121.758 ,  121.6602,  122.0025,  121.8329,  121.7917,
        121.9276,  121.9382,  122.1757,  122.1263,  122.1583,  122.4373,
        122.7951,  122.5218,  122.6812,  122.8259,  122.703 ,  122.986 ,
        122.9554,  123.0626,  123.2138,  123.3168,  123.4295,  123.2851,
        123.4148,  123.5748,  123.6172,  123.878 ,  123.6756,  123.9577,
        124.1508,  124.1186,  124.2156,  124.1542,  124.1808,  124.3123,
        124.3033,  124.708 ,  124.8149,  124.8475,  124.9881,  124.9396,
        124.891 ,  125.4231,  125.4586,  125.3756,  125.427 ,  125.7343,
        125.7275,  125.5051,  125.9411,  126.2977,  126.3108,  126.1077,
        125.9955,  126.2849,  126.3487,  126.2716,  126.4261,  126.7593,
        126.6638,  126.4558,  126.6714,  126.5689,  127.0663,  127.2225,
        127.2619,  127.3919,  127.3613,  127.7364,  127.7347,  127.7573,
        128.0118,  127.9196,  127.9366,  128.0976,  128.2422,  128.3238,
        128.1875,  128.4178,  128.3773,  128.6561,  128.8102,  128.8265,
        128.9185,  129.0117,  129.0532,  129.2663,  129.28  ,  129.2249,
        129.6153,  129.4691,  129.6862,  129.59  ,  129.8873,  129.9825,
        130.0237,  130.0761,  130.4033,  130.2935,  130.3519,  130.5191,
        130.6656,  130.6305,  130.863 ,  130.9782,  130.9784,  130.9646,
        131.0784,  131.435 ,  131.29  ,  131.4661,  131.6169,  131.6195,
        131.7462,  131.9573,  132.0718,  132.0433,  132.2239,  131.925 ,
        132.1325,  132.2874,  132.6045,  132.5887,  132.6044,  132.8037,
        132.8606,  132.8635,  132.8818,  133.0283,  133.0394,  133.4498,
        133.49  ,  133.3747,  133.7302,  133.7   ,  133.7543,  133.9177,
        133.8717,  134.0369,  134.3954,  134.2805,  134.6139,  134.3124,
        134.5621,  134.5456,  134.9996,  134.9132,  135.1095,  134.8449,
        135.1437,  135.2405,  135.1996,  135.622 ,  135.6284,  135.7457,
        135.7036,  135.62  ,  136.1612,  136.2452,  136.1735,  136.255 ,
        136.3209,  136.5701,  136.5497,  136.6844]
)