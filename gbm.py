# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pylab as p
import numpy as np

#Setup parameters
mu = 0.1;
sigma = 0.26;
S0 = 39;
n_path = 1000;
n = n_partitions = 1000;

#Create 1000 paths of Geometric Brownian Motion for 0 < t < 3
t = p.linspace(0,3,n+1);
dB = p.randn(n_path,n+1) / p.sqrt(n);
dB[:,0] = 0;
B = dB.cumsum(axis=1);

#Calculate stock prices
nu = mu - sigma*sigma/2.0;
S = p.zeros_like(B);
S[:,0] = S0;
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

#Plot 5 realizations of the Geometric Brownian Motion
S_5plot = S[0:5];
p.plot(t,S_5plot.transpose()); 
p.xlabel('Time, $t$');
p.ylabel('Stock price, $S_t$');
p.title('5 realizations of the Geometric Brownian Motion');
p.show;

#Calculate the expectation value of S(3)
S3 = p.array(S[:,-1]);
print('E[S(3)] =', np.mean(S3));

#Calculate the variance of S(3)
print('Var[S(3)] =',np.var(S3));

#Calculate P[S(3)> 39]
mask = S3 > 39;
probability_of_S3_more_than_39 = sum(mask) / len(mask);
print('P[S(3)> 39] =', probability_of_S3_more_than_39);

#Calculate E[S(3) | S(3) > 39]
S3_mask = S3 * mask;
expected_value_of_S3_given_S3_more_than_39 = sum(S3_mask) / sum(mask);
print('E[S(3) | S(3) > 39] =', expected_value_of_S3_given_S3_more_than_39);