# https://www.quora.com/What-is-the-optimum-strategy-for-renewing-a-library-book-to-maximize-the-expected-time-you-keep-it
# This could be optimized by finding the expectation based on the geometric distribution directly instead of generating trials.



import random
random.seed()

def recursive():
    k = 7
    n = 10
    p = 0.1
    num_trials = 50000
 
    expecteds = []
    strats = []
 
    for this_n in range(1, n + 1):
      max_mean = 0
      max_strat = 0
      for strat in range(1, k + 1):
        sum_days = 0
        for _ in range(num_trials):
          strat_day = 0
          these_days = k
          while (random.random() > p):
            strat_day += 1
            if (strat_day == strat):
              if (this_n == 1):
                these_days = strat_day + k
              else:
                these_days = strat_day + expecteds[this_n - 2]
              break
          sum_days += these_days
        mean_days = sum_days / num_trials
        if mean_days > max_mean:
          max_mean = mean_days
          max_strat = strat
      expecteds.append(max_mean)
      strats.append(max_strat)
  
    print("k = " + str(k) + ", n = " + str(n) + ", p = " + "{0:.{1}f}".format(p, 1))
    print("Strat = " + str(strats))
    print("Expected = " + str(expecteds))

def geometricoptimized():
    k = 7
    n = 10
    p = 0.1
 
    expecteds = []
    strats = []
 
    for this_n in range(1, n + 1):
      max_mean = 0
      max_strat = 0
      for strat in range(1, k + 1):
        if (this_n == 1):
          mean_days = strat * (1 - p) ** strat + k
        else:
          mean_days = (strat + expecteds[this_n - 2] - k) * (1 - p) ** strat + k
        if mean_days > max_mean:
          max_mean = mean_days
          max_strat = strat
      expecteds.append(max_mean)
      strats.append(max_strat)
  
    print("k = " + str(k) + ", n = " + str(n) + ", p = " + "{0:.{1}f}".format(p, 1))
    print("Strat = " + str(strats))
    print("Expected = " + str(expecteds))