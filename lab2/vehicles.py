import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#print((df.columns))

	data_c = df.values[:,0]
	df_dum = df.dropna()
	data_n = df_dum.values[:,1]

	#HISTOGRAM
	sns_hist_c = sns.distplot(data_c, bins=20, kde=False, rug=True).get_figure()
	axes = plt.gca()
	axes.set_xlabel('MPG Current vehicles')
	axes.set_ylabel('Vehicles count')
	#sns_hist_c.savefig("hist_current.png", bbox_inches = 'tight')
	#sns_hist_c.savefig("hist_current.pdf", bbox_inches='tight')

	#plt.clf()
	sns_hist_n = sns.distplot(data_n, bins = 20, kde=False, rug=True).get_figure()
	axes = plt.gca()
	axes.set_xlabel('MPG New vehicles')
	axes.set_ylabel('Vehicles count')
	sns_hist_n.savefig("hist_vehicles.png", bbox_inches = 'tight')
	sns_hist_n.savefig("hist_vehicles.pdf", bbox_inches='tight')

	#SCATTER PLOT
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot_vehicles.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot_vehicles.pdf",bbox_inches='tight')



	# print((("Mean: %f")%(np.mean(data))))
	# print((("Median: %f")%(np.median(data))))
	# print((("Var: %f")%(np.var(data))))
	print((("Std of current vehicles: %f") % (np.std(data_c))))
	print((("Std of new vehicles: %f") % (np.nanstd(data_n))))
	# print((("MAD: %f")%(mad(data))))



