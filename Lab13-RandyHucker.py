## Lab 13: Monte Carlo ##

import scipy as sp
import numpy as np
from random import random
import matplotlib.pyplot as plt
_author_ = "Randy Hucker"
_credits_ = ["Me, myself, and I, and Ch 11 of PYTHON PROGRAMMING"]
_email_ = "huckerre@mail.uc.edu"


# MODULE 13 LAB
if __name__ == "__main__":
    balls = np.arange(1, 1000)
    emptybin = []
    for N in balls:
        bins = np.zeros(N)
        emptybins = 0
        for b in range(N):
            bins[int(N * random())] += 1
        emptybin.append(len(bins) - len(np.nonzero(bins)[0]))
    plt.plot(balls, emptybin)
    plt.show()

    result = sp.stats.linregress(x=balls, y=emptybin, alternative='greater')
    print(f"Slope: {result.slope:.6f}")
    print(f"Intercept: {result.intercept:.6f}")
    print(f"R-value: {result.rvalue:.6f}")
    print(f"R-squared: {result.rvalue**2:.6f}")


# SEEDING THE RANDOM-NUMBER GENERATOR FOR REPRODUCIBILITY
# from random import seed
# seed(43)
# for roll in range(20):
#     print(1 + int(random()*6), end=' ')


# A COMPUTATIONAL EXPERIMENT
# sum, sumdev = 0.0, 0.0
# N = 10000
# for i in range(N):
#     next = random.random()
#     sum += next
#     dev = (next - 0.5)**2
#     sumdev += dev
# mean = sum / N
# print(f"Mean:{mean}")
# var = sumdev/(N-1)
# print(f"Variance: {var}")


# MONTE CARLO ESTIMATION OF PI
# N = 10000
# circle_hits = 0
# for i in range(N):
#     x, y = random(), random()
#     if x**2 + y**2 <= 1:
#         circle_hits += 1
# pi_est = 4 * circle_hits / N
# print("Final Estimate of Pi=", pi_est)


# MONTE CARLO INTEGRATION
# import numpy as np
# rng = np.random.default_rng()
# # limits of integration are a, b
# a = 0
# b = np.pi # gets the value of pi
# N = 10000
# integral = 0.0
# def f(x):
#     return np.sin(x)
# for i in range (N):
#     x = a + (b-a)*rng()
#     integral += f(x)
# ans = (b-a) * integral/N
# print (f"{ans} is the estimated value.")


# BALLS AND PINS SIMULATION
# import numpy as np
# balls = np.arange(100, 100000, 100)
# maxbin = []
# for N in balls:
#     bins = np.zeros(N)
#     for b in range(N):
#         bins[int(N * random())] += 1
#     maxbin.append(max(bins))
# plt.plot(balls, maxbin)
# plt.show()
