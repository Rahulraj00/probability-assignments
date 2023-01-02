import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from functions import *


#Calculating probability using bernoulli simulation


#Probability of picking red ball
p_1= (0.5)
#Probability of picking black ball
p_2= 1-p_1
#Probability of getting red ball if first ball is red
p_red_1= (7/12)
#Probability of getting red ball if first ball is black
p_red_2= (5/12)

#Probability that a red ball is picked
prob= (p_1*p_red_2+p_2*p_red_1)

print(prob)
