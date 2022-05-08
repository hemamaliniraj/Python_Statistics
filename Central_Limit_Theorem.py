import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
#create a list to store sample means
means = []
#Repeat experiment 50 times
for i in range(50):
    #generate a random array of 5 values, with values between 0 and 5
    arr = np.random.rand(5)
    #calculate mean of random sample
    s_mean = np.mean(arr)
    #add s_mean to list 
    means.append(s_mean)
    
    mean = sum(means)/ len(means)

sns.histplot(means,bins=50,color='green',kde=True)
#Calculate the mean
mean = sum(means)/ len(means)

#Plot the mean over the distribution to get a sense of the central tendency
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2)
min_ylim, max_ylim = plt.ylim()
plt.text(mean*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(mean))


plt.title("Sampling distribution of sample means of randomly generated samples (no of samples = 100)")
plt.xlabel("Sample mean")
plt.ylabel("Frequency")

plt.show()