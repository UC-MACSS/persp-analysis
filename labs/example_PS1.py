# Import initial packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def pareto_wealth_sim(p):
    
    """
    Requires a simulation profile, p, structured as a dictionary
    
    p = {
        'w0'          : 10000,      #starting wealth
        'inc'         : 50000,      #starting income
        'gr'          : 1.07,       #growth rate
        'ms'          : 0.05,       #market shocks
        'ir'          : 0.45,       #irrationality
        'st_year'     : int(2006),  #start year
        'lf_years'    : 60,         #years to live
        'a'           : 10,         #shape of pareto pmf 
        'num_draws'   : 15000       #simulations
    }
    """    

    #set random seed
    np.random.seed(524)

    pareto_errors = np.random.pareto(p['a'], (p['lf_years'], p['num_draws']))

    #create a matrix of dim (lf_years, num_draws)
    ln_wealth_mat = np.zeros((p['lf_years'], p['num_draws']))

    #fill the matrix
    ln_wealth_mat[0, :] = np.log(p['w0']) + pareto_errors[0, :]

    #loop and apply model
    for yr in range(1, p['lf_years']):
        ln_wealth_mat[yr, :] = ((1 - p['gr']/4) * (np.log(p['w0']) + p['ms'] * (yr)) +
                                p['ir']/4 * ln_wealth_mat[yr - 1, :]  +
                                np.log(p['inc']/1000+(p['inc']/10000*yr)) +
                                pareto_errors[yr, :])


    wealth_mat = np.exp(ln_wealth_mat) #dealing with large numbers so put in terms of 10k's
    return wealth_mat