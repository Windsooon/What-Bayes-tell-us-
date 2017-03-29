#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# the probability of a positive test in all people is P(A)
# the prevalence of this disease P(D)
# the probability of a positive test result if a person is infected by the disease is P(A1)
# the probability of a positive test result if a person is not infected by the disease is P(A2)
# if someone was tested to be positive, the probability of getting a true infection is
# P(D|A) = P(D, A) / P(A) = P(A|D) * P(D) / P(A)
#
# P(A|D) = P(A1)
#
# P(A) = P(A1) * P(D) + P(A2) * P(1-D)
#
# P(D|A) = P(A1) * P(D) / P(A1) * P(D) + P(A2) * P(1-D)

import argparse
import matplotlib.pyplot as plt


class Fluid(object):

    def __init__(self, S, A1, A2):
        self.A1 = A1
        self.A2 = A2
        self.S = S/100

    def calculate(self):
        P = (self.A1 * self.S) / (self.A1 * self.S + self.A2 * (1 - self.S))
        return P * 100

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ns", type=float, default=0.8)
    parser.add_argument("-s", type=float, default=0.03)
    args = parser.parse_args()

    X = [x for x in range(100) if x % 3 == 0]
    Y = [round(Fluid(
        x, args.ns, args.s).calculate(), 2) for x in range(100) if x % 3 == 0]

    print(Y)

plt.plot(X, Y)
plt.xlabel('the prevalence of this disease')
plt.ylabel('the probability of true positive')
plt.show()
