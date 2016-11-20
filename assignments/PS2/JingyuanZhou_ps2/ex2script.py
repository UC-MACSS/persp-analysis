import numpy as np
import ex2module as ex2m
# Declare your parameters
mu = np.log(70)
sigma = 0.2

seed = 300
np.random.seed(seed)

# Then add your code generating 10,000 draws here.
scores = np.random.lognormal(mu, sigma, 10000)

# Then run the scores through the function that performs # three waves of eliminating outliers that are 3 standard # deviations away from the mean.
scrubbed_scores = ex2m.threescrubs(scores)

print("The number of elements in the array returned by the threescrubs function is: ", len(scrubbed_scores))
print("Mean of this vector: ", np.mean(scrubbed_scores))
print("standard deviation of this vector: ", np.std(scrubbed_scores))
