'''
-------------------
This is Bobae's PS1
-------------------
'''
# import packages
import numpy as np
from numpy import log
import scipy as sp
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
'''
------------------------------------------------------------------------
Exercise 1a: Simulate the data
------------------------------------------------------------------------
'''
# set parameters
inc0 = 80000 # base income
sigma = 0.1 # standard deviation
rho = 0.2 # persistence
g = 0.03 # annual growth rate

beg_year = int(2018) # beginning year
lf_years = 40 # lifetime working years
num_draws = 10000 # number of simulations

dim = (lf_years, num_draws) # dimension of the matrix
ln_inc = np.zeros(dim) # empty 40 by 10000 matrix

# set the error term
np.random.seed(12341234)
norm_errors = np.random.normal(0, sigma, dim) # normally distributed error matrix

# Set 2018 income
ln_inc[0, :] = log(inc0) + norm_errors[0, :]

# Set following income
for yr in range(1, 40):
    ln_inc[yr,:] = (1 - rho)*(log(inc0) + g*yr) + rho*ln_inc[yr-1, :] + norm_errors[yr, :]

inc = np.exp(ln_inc)

# plot one lifetime income path
plot_1a = True
if plot_1a:
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # plot a lifetime income path
    x = range(beg_year, (beg_year+lf_years))
    y = inc[:,0]

    plt.plot(x,y)
    plt.xlabel('Year $t$')
    plt.ylabel('Annual income (\$s)')
    plt.title('One simulated lifetime income path', fontsize = 20)

    # save the output
    output_path = os.path.join(output_dir, 'Fig_1a')
    plt.savefig(output_path)
    plt.close()

'''
------------------------------------------------------------------------
Exercise 1b: Plot a histogram
------------------------------------------------------------------------
'''
# plot a histogram
plot_1b = True
if plot_1b:
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # plot a histogram of the income distribution in 2018
    plt.hist(inc[0,:], bins=50)
    plt.xlabel('Income in 2018 (\$s)')
    plt.ylabel('Count')
    plt.title('Simulated income distribution in 2018', fontsize = 20)

    # save the output
    output_path = os.path.join(output_dir, 'Fig_1b')
    plt.savefig(output_path)
    plt.close()

# answer questions
inc2018 = inc[0,:]
inc2018_gt100k_pct = sum(inc2018>100000)/len(inc2018)
inc2018_ls70k_pct =  sum(inc2018<70000)/len(inc2018)

# print answers
print('1b. Percent of students getting more than $100k in first period: ',
      inc2018_gt100k_pct * 100, '%')
print('1b. Percent of students getting less than $70k in first period: ',
      inc2018_ls70k_pct * 100, '%')
'''
------------------------------------------------------------------------
Exercise 1c: Paying off the student loan
------------------------------------------------------------------------
'''
# set the student loan
loan = 95000
payoff = []
paying = list(zip(*inc*0.1))

for i in range(len(paying)):
    for j in range(len(paying[i])):
        a = np.cumsum(paying[i][:j+1])
        if a[j] > loan:
            payoff.append(j)
            break

# plot a histogram
plot_1c = True
if plot_1c:
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # plot a histogram
    plt.hist(payoff, bins=len(set(payoff))) # set() gives only unique values
    plt.xlabel('Years to pay off the loan')
    plt.ylabel('Count')
    plt.title('Paying off student loan', fontsize = 20)

    # save the output
    output_path = os.path.join(output_dir, 'Fig_1c')
    plt.savefig(output_path)
    plt.close()

# answer question
payoff_10yrs_pct = sum(i <= 10 for i in payoff)/len(payoff)

# print answer
print('1c. Percent of students paying off $95k loan in 10 years: ',
      payoff_10yrs_pct * 100, '%')
'''
------------------------------------------------------------------------
Exercise 1d: Paying off the student loan 2
------------------------------------------------------------------------
'''
# set changed parameters
inc0_2 = 85000 # new base income
sigma_2 = 0.15 # new standard deviation
ln_inc_2 = np.zeros(dim)

# set changed error term
norm_errors_2 = np.random.normal(0, sigma_2, dim)

# Set changed 2018 income
ln_inc_2[0, :] = log(inc0_2) + norm_errors_2[0, :]

# Set changed following income
for yr in range(1, 40):
    ln_inc_2[yr,:] = (1 - rho)*(log(inc0_2) + g*yr) + rho*ln_inc_2[yr-1, :] + norm_errors_2[yr, :]

inc_2 = np.exp(ln_inc_2)

# changed student loan
payoff_2 = []
paying_2 = list(zip(*inc_2*0.1))

for i in range(len(paying_2)):
    for j in range(len(paying_2[i])):
        a = np.cumsum(paying_2[i][:j+1])
        if a[j] > loan:
            payoff_2.append(j)
            break

# plot histogram
plot_1d = True
if plot_1d:
    # Create directory if images directory does not already exist
    cur_path = os.path.split(os.path.abspath(__file__))[0]
    output_fldr = 'images'
    output_dir = os.path.join(cur_path, output_fldr)
    if not os.access(output_dir, os.F_OK):
        os.makedirs(output_dir)

    # plot a histogram
    plt.hist(payoff_2, bins=len(set(payoff_2)))
    plt.xlabel('Years to pay off the loan')
    plt.ylabel('Count')
    plt.title('Paying off student loan', fontsize = 20)

    # save the output
    output_path = os.path.join(output_dir, 'Fig_1d')
    plt.savefig(output_path)
    plt.close()

# answer question
payoff_10yrs_pct_2 = sum(i <= 10 for i in payoff_2)/len(payoff_2)

# print answer
print('1d. Percent of students paying off $95k loan in 10 years: ',
      payoff_10yrs_pct_2 * 100, '%')
