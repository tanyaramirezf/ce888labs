# Lab2

## Analysis

In order to compare the car's fuel effiency of current and new vehicles and from the data collected that includes the MPG of some cars in both fleet, the histogram of said miles per gallon (MPG - L/100 km) is shown in the following chart:

![logo](./hist_vehicles.png?raw=true)

From the data collected, there are more observations of current cars (blue bars) than new cars, nevertheless, from the fleet with new cars (orange bars), the MPG recorded is larger and the median from the current cars is smaller than for the new cars. Furthermore, comparing the MPG from a current and a new car under the same circumstances (say distance), the efficiency is different as it is shown in the scatter plot of the MPG of current vehicles and new vehicles:

![logo](./scaterplot_vehicles.png?raw=true))

In order to review and to compare the performance of each fleet (current and new vehicles), bootstrapping was applied in order to calculate the confidence intervals for the standard deviation for each fleet. It is worth to mention that the standard deviation for the current vehicles and new vehicles is 6.401805 and 6.068931, respectively, so overall, reviewing only this sample of cars there is not significant variation between the performance of each fleet. 

The confidence intervals for std for each fleet are shown bellow:

**Confidence interval for current vehicles**
![logo](./bootstrap_confidence_current.png?raw=true)

**Confidence interval for new vehicles**
![logo](./bootstrap_confidence_new.png?raw=true)

Given that the confidence interval for the current vehicles is within the confidence interval of the new project, there is no evidence of further improvement in the efficiency (measured by MPG) from using new cars instead of the current cars.
