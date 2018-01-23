import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_std = data.std()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_std,lower, upper


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	#print df.columns
	
	#data = df.values.T[1]

	data_c = df.values[:,0]
	df_dum = df.dropna()
	data_n = df_dum.values[:,1]

	boots = []
	for i in range(1,1000,10):
		boot = boostrap(np.std, i, data_c)
		boots.append([i,boot[0], "mean"])
		boots.append([i,boot[1], "lower"])
		boots.append([i,boot[2], "upper"])


	df_boot = pd.DataFrame(boots,  columns=['Boostrap Iterations','Std',"Value"])
	sns_plot_c = sns.lmplot(df_boot.columns[0],df_boot.columns[1], data=df_boot, fit_reg=False,  hue="Value")

	sns_plot_c.axes[0,0].set_ylim(0,)
	sns_plot_c.axes[0,0].set_xlim(0,1000)

	sns_plot_c.savefig("bootstrap_confidence_current.png",bbox_inches='tight')
	sns_plot_c.savefig("bootstrap_confidence_current.pdf",bbox_inches='tight')

	boots = []
	for i in range(1, 1000, 10):
		boot = boostrap(np.std, i, data_n)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Std', "Value"])
	sns_plot_n = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot_n.axes[0, 0].set_ylim(0, )
	sns_plot_n.axes[0, 0].set_xlim(0, 1000)

	sns_plot_n.savefig("bootstrap_confidence_new.png", bbox_inches='tight')
	sns_plot_n.savefig("bootstrap_confidence_new.pdf", bbox_inches='tight')
	
	
	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))
	


	