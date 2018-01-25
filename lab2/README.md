# Lab2

## Analysis

In order to compare the current and new vehicles and from the data collected that includes the MPG of some cars in both fleet, the histogram of said MPG is shown in the following chart:

![logo](./hist_vehicles.png?raw=true)

From the data collected, there are more observations of current cars (blue bars) than new cars, nevertheless, from the fleet with new cars (orange bars), the MPG recorded is larger and the median from the current cars is smaller than for the new cars. 

In order to review and to compare the performance of each fleet (current and new vehicles), bootstrapping was applied in order to calculate the confidence intervals for the standard deviation for each fleet. Both confidence intervals are shown bellow:

#Confidence interval for current vehicles
![logo](./bootstrap_confidence_current.png?raw=true)

#Confidence interval for new vehicles
![logo](./bootstrap_confidence_new.png?raw=true)

 
Given that the confidence interval for the current vehicles is within the confidence interval of the new project, there is no evidence of further improvement on the MPG.
