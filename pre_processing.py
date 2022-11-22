import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


df = pd.read_csv('../data/processed/SZmax_Zmin.csv')
plot_figure = True

##########################################
#           DownSample  S- parameter Signals
##########################################

down_sample_factor = 10
x = np.array(df.columns)

length_df = [*range(df.shape[1])]

Selected_index = length_df[::down_sample_factor]
#drop_idx = list(range(0,df.shape[1],down_sample_factor))
new_df_cols = [j for i,j in enumerate(df.columns) if i in Selected_index]

new_df = df[new_df_cols]
new_x = np.array(new_df.columns)




##########################################
#     Import Design Parameters
##########################################














if plot_figure==True:
    n_rows = 4
    n_col = 2
    fig, axes = plt.subplots(nrows = n_rows, ncols = n_col, figsize=(15,12))
    fig.subplots_adjust(hspace = .5, wspace=.001)

    axs = axes.ravel()
    #tickers = np.random.randint(0,len(df),n_rows)
    tickers = np.asarray([9834,10118,9162,10054 ])
    for i in range(n_rows):
        #axs[i].plot(np.asarray(x,float), df.iloc[tickers[i],:],'go' ,np.asarray(new_x,float), new_df.iloc[tickers[i],:],linewidth=0.5, markersize= 0.5)
        axes[i,0].plot(np.asarray(x,float), df.iloc[tickers[i],:])
        axes[i,0].set_title('Iter '+ str(tickers[i]) + '  Original Sample points: ' + str(len(x))    )
        axes[i,1].plot(np.asarray(new_x, float), new_df.iloc[tickers[i], :],'go-', markersize = 1)
        axes[i,1].set_title('      '+ '  Downsampled Sample points: ' + str(len(new_x)))
        #ax.df.iloc[:,ticker].plot()

        #axes[i].set_title(i)
    plt.show()



'''
test_df = df.iloc[9834,:]
gradient = np.gradient(test_df)
gradient_df = pd.DataFrame(gradient)
ax = test_df.T.plot()
gradient_df.plot(ax=ax)

plt.show()
'''
