# import relevant libraries

import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import seaborn as sns
import math

import warnings


# set options
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)


# read clean Open 2019 dataset
df_19 = pd.read_csv('./data/2019_opens_clean.csv')

df_19 = df_19.loc[:, ~df_19.columns.str.contains('^Unnamed')]


df_rand = df_19.sample(frac=0.05, random_state=42)


# create new feature: top_athletes
overallrank_list = df_rand['overallrank'].to_list()
top_athletes = []
for i in overallrank_list:
    if i > 0 and i < 1855:
        top_athletes.append('top_01')
    elif i >= 1856 and i < 9277:
        top_athletes.append('top_05')
    elif i >= 9278 and i < 46387:
        top_athletes.append('top_25')
    elif i >= 46388 and i < 92775:
        top_athletes.append('top_50')
    elif i >= 92776 and i <= 185550:
        top_athletes.append('rest')
    else:
        top_athletes.append(np.NaN)
df_rand['top_athletes'] = top_athletes

df_rand['w4_bmu_status'].replace([1.0,0.0,np.NaN],['Yes','No','unknown'],inplace=True)
df_rand['w3_hspu_status'].replace([1.0,0.0,np.NaN],['Yes','No','unknown'],inplace=True)


#hue_list = ['gender','is_scaled','w4_bmu_status']

#for i in hue_list:
#    plot_file = sns.pairplot(
#        data=df_rand[['height','weight',i]],
#        hue=i
#        )
#    plot_file.savefig(f'./images/{i}_test.png')
#    print(f'{i} has been plotted.')

hue_list = [
    #'gender',
    #'region',
    'top_athletes',
    'is_scaled',
    #'time_completed',
    'w3_hspu_status',
    'w4_bmu_status'
    ]
    

for i in hue_list:
    
    plot_file = sns.pairplot(
        data=df_rand[[
            'affiliateid','age','height','weight','overallscore','time_2','time_3',
            'time_4','bs_backsquat','bs_cleanandjerk','bs_snatch','bs_deadlift','bs_fightgonebad','bs_maxpull_ups',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_01.png')
    print(f'{i} #01 has been plotted.')

    plot_file = sns.pairplot(
        data=df_rand[[
            'affiliateid','age','height','weight','overallscore','time_2','time_3',
            'bs_fran','bs_grace','bs_helen','bs_filthy50','bs_sprint400m','bs_run5k','w1_reps_total',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_02.png')
    print(f'{i} #02 has been plotted.')

    plot_file = sns.pairplot(
        data=df_rand[[
            'affiliateid','age','height','weight','overallscore','time_2','time_3',
            'w2_reps_total','w3_reps_total','w4_reps_total','w5_reps_total','w2_tiebreak','w3_tiebreak','w4_tiebreak',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_03.png')
    print(f'{i} #03 has been plotted.')

    plot_file = sns.pairplot(
        data=df_rand[[
            'time_4','bs_backsquat','bs_cleanandjerk','bs_snatch','bs_deadlift','bs_fightgonebad','bs_maxpull_ups',
            'bs_fran','bs_grace','bs_helen','bs_filthy50','bs_sprint400m','bs_run5k','w1_reps_total',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_04.png')
    print(f'{i} #04 has been plotted.')

    plot_file = sns.pairplot(
        data=df_rand[[
            'time_4','bs_backsquat','bs_cleanandjerk','bs_snatch','bs_deadlift','bs_fightgonebad','bs_maxpull_ups',
            'w2_reps_total','w3_reps_total','w4_reps_total','w5_reps_total','w2_tiebreak','w3_tiebreak','w4_tiebreak',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_05.png')
    print(f'{i} #05 has been plotted.')

    plot_file = sns.pairplot(
        data=df_rand[[
            'bs_fran','bs_grace','bs_helen','bs_filthy50','bs_sprint400m','bs_run5k','w1_reps_total',
            'w2_reps_total','w3_reps_total','w4_reps_total','w5_reps_total','w2_tiebreak','w3_tiebreak','w4_tiebreak',
            i]],
            hue=i,
            palette="husl"
        )
    plot_file.savefig(f'./images/{i}_06.png')
    print(f'{i} #06 has been plotted.')