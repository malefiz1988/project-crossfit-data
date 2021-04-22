import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import math
import plotly.io as pio
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import squarify

import EDA_plots as plot

import warnings

# set options
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.plotting.backend = "plotly"
pio.renderers.default = 'iframe' # or 'notebook' or 'colab'

#sns.set_style('white')
sns.set_context("talk")


##########



def gender_distribution(data):
    plt.figure(figsize=(7,4))
    g = sns.countplot(
        x ='gender',
        data = data,
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in g.get_yticks()/1000]
    g.set_yticklabels(ylabels)
    g.set_title('Gender Distribution')
    g.set_xlabel('')
    g.set_ylabel('')
    plt.show()
    
def age_distribution(data):
    plt.figure(figsize=(10,4))
    g = sns.histplot(
        data=data,
        x='age',
        hue='gender',
        bins=24,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    g.set_title('Age Distributions (stacked)')
    g.set_ylabel('')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in g.get_yticks()/1000]
    g.set_yticklabels(ylabels)
    g.set_xlabel('age [years]')
    plt.show()
    
def workout_participation_all(df):
    rx,sc = [],[]
    for i in [1,2,3,4,5]:
        rx.append(df[(df[f'scaled_{i}']==0) & (df[f'score_{i}']!=0)]['competitorid'].count())
        sc.append(df[(df[f'scaled_{i}']==1) & (df[f'score_{i}']!=0)]['competitorid'].count())
    tot = np.add(rx,sc)
    
    plt.figure(figsize=(15,6))
    idx = ['19.1','19.2','19.3','19.4','19.5']
    bar1 = sns.barplot(
        x=idx,
        y=tot,
        color='lightblue',
        edgecolor='black'
    )
    bar2 = sns.barplot(
        x=idx,
        y=rx,
        color='darkblue',
        edgecolor='black'
    )
    bar1.set_title('Workout Participation (M & F)')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in bar1.get_yticks()/1000]
    bar1.set_yticklabels(ylabels)
    bar1.set_xlabel('Open Workout')
    top_bar = mpatches.Patch(color='lightblue', label='Scaled')
    bottom_bar = mpatches.Patch(color='darkblue', label='Rx')
    top_bar
    plt.legend(handles=[top_bar, bottom_bar])
    plt.show()
    
def workout_participation_male(df):
    rx,sc = [],[]
    df_m = df[df['gender']=='M']
    for i in [1,2,3,4,5]:
        rx.append(df_m[(df_m[f'scaled_{i}']==0) & (df_m[f'score_{i}']!=0)]['competitorid'].count())
        sc.append(df_m[(df_m[f'scaled_{i}']==1) & (df_m[f'score_{i}']!=0)]['competitorid'].count())
    tot = np.add(rx,sc)
    
    plt.figure(figsize=(15,6))
    idx = ['19.1','19.2','19.3','19.4','19.5']
    bar1 = sns.barplot(
        x=idx,
        y=tot,
        color='lightblue',
        edgecolor='black'
    )
    bar2 = sns.barplot(
        x=idx,
        y=rx,
        color='gold',
        edgecolor='black'
    )
    bar1.set_title('Workout Participation (Men)')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in bar1.get_yticks()/1000]
    bar1.set_yticklabels(ylabels)
    bar1.set_xlabel('Open Workout')
    top_bar = mpatches.Patch(color='lightblue', label='Scaled')
    bottom_bar = mpatches.Patch(color='gold', label='Rx')
    plt.legend(handles=[top_bar, bottom_bar])
    plt.show()
    
def workout_participation_female(df):
    rx,sc = [],[]
    df_f = df[df['gender']=='F']
    for i in [1,2,3,4,5]:
        rx.append(df_f[(df_f[f'scaled_{i}']==0) & (df_f[f'score_{i}']!=0)]['competitorid'].count())
        sc.append(df_f[(df_f[f'scaled_{i}']==1) & (df_f[f'score_{i}']!=0)]['competitorid'].count())
    tot = np.add(rx,sc)
    
    plt.figure(figsize=(15,6))
    idx = ['19.1','19.2','19.3','19.4','19.5']
    bar1 = sns.barplot(
        x=idx,
        y=tot,
        color='lightblue',
        edgecolor='black'
    )
    bar2 = sns.barplot(
        x=idx,
        y=rx,
        color='limegreen',
        edgecolor='black'
    )
    bar1.set_title('Workout Participation (Women)')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in bar1.get_yticks()/1000]
    bar1.set_yticklabels(ylabels)
    bar1.set_xlabel('Open Workout')
    top_bar = mpatches.Patch(color='lightblue', label='Scaled')
    bottom_bar = mpatches.Patch(color='limegreen', label='Rx')
    plt.legend(handles=[top_bar, bottom_bar])
    plt.show()
    
def workout_balance_1(df):
    fig, axes = plt.subplots(1, 3, figsize=(30, 7))
    a = sns.histplot(
        ax=axes[0],
        data=df[df['scaled_1']==0],
        x='w1_reps_total',
        hue='gender',
        bins=30,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    a.set_title('19.1 | Rx')
    a.set_ylabel('')
    a.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    a.set_yticklabels(ylabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[df['scaled_1']==1],
        x='w1_reps_total',
        hue='gender',
        bins=30,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    b.set_title('19.1 | Scaled')
    b.set_ylabel('')
    b.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    b.set_yticklabels(ylabels)
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    c = sns.histplot(
        ax=axes[2],
        data=df_ta,
        x='w1_reps_total',
        hue='gender',
        bins=10,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    c.set_title('19.1 | Top 1%')
    c.set_ylabel('')
    c.set_xlabel('total reps');
    
def workout_balance_2_rx(df):
    fig = go.Figure()
    df_m_rx = df[(df['gender']=='M') & (df['scaled_2']==0) & (df['score_2']!=0)].groupby(by='w2_full_rounds_completed').count()
    df_m_rx_list = list(df_m_rx.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_m_rx_list),
            sum(df_m_rx_list)-sum(df_m_rx_list[:1]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:2]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:3]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_rx = df[(df['gender']=='F') & (df['scaled_2']==0) &(df['score_2']!=0)].groupby(by='w2_full_rounds_completed').count()
    df_f_rx_list = list(df_f_rx.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_f_rx_list),
            sum(df_f_rx_list)-sum(df_f_rx_list[:1]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:2]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:3]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"})) 
    fig.show()
    
def workout_balance_2_sc(df):
    fig = go.Figure()
    df_m_sc = df[(df['gender']=='M') & (df['scaled_2']==1) & (df['score_2']!=0)].groupby(by='w2_full_rounds_completed').count()
    df_m_sc_list = list(df_m_sc.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_m_sc_list),
            sum(df_m_sc_list)-sum(df_m_sc_list[:1]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:2]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:3]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_sc = df[(df['gender']=='F') & (df['scaled_2']==1) & (df['score_2']!=0)].groupby(by='w2_full_rounds_completed').count()
    df_f_sc_list = list(df_f_sc.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_f_sc_list),
            sum(df_f_sc_list)-sum(df_f_sc_list[:1]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:2]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:3]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"}))
    fig.show()
    
def workout_balance_2_ta(df):
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    fig = go.Figure()
    df_m_1 = df_ta[df_ta['gender']=='M'].groupby(by='w2_full_rounds_completed').count()
    df_m_1_list = list(df_m_1.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_m_1_list),
            sum(df_m_1_list),
            sum(df_m_1_list)-sum(df_m_1_list[:1]),
            sum(df_m_1_list)-sum(df_m_1_list[:2]),
            sum(df_m_1_list)-sum(df_m_1_list[:3])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_1 = df_ta[df_ta['gender']=='F'].groupby(by='w2_full_rounds_completed').count()
    df_f_1_list = list(df_f_1.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['start', ' 8 min', '12 min', '16 min', '20 min'],
        x = [
            sum(df_f_1_list),
            sum(df_f_1_list),
            sum(df_f_1_list)-sum(df_f_1_list[:1]),
            sum(df_f_1_list)-sum(df_f_1_list[:2]),
            sum(df_f_1_list)-sum(df_f_1_list[:3])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"}))
    fig.show()
    
def workout_balance_3(df):
    fig, axes = plt.subplots(1, 3, figsize=(30, 7))
    a=sns.histplot(
        ax=axes[0],
        data=df[df['scaled_3']==0],
        x='w3_reps_total',
        hue='gender',
        bins=30,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    a.set_title('19.3 | Rx')
    a.set_ylabel('')
    a.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    a.set_yticklabels(ylabels)
    b=sns.histplot(
        ax=axes[1],
        data=df[df['scaled_3']==1],
        x='w3_reps_total',
        hue='gender',
        bins=30,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    b.set_title('19.3 | Scaled')
    b.set_ylabel('')
    b.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    b.set_yticklabels(ylabels)
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    c=sns.histplot(
        ax=axes[2],
        data=df_ta,
        x='w3_reps_total',
        hue='gender',
        bins=25,
        multiple='stack',
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    c.set_title('19.3 | Top 1%')
    c.set_ylabel('')
    c.set_xlabel('total reps');
    
def workout_balance_3_rx(df):
    fig = go.Figure()
    df_m_rx = df[(df['gender']=='M') & (df['scaled_3']==0) & (df['score_3']!=0)].groupby(by='w3_full_rounds_completed').count()
    df_m_rx_list = list(df_m_rx.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['start', 'OHL', 'Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_m_rx_list),
            sum(df_m_rx_list)-sum(df_m_rx_list[:1]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:2]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:3]),
            sum(df_m_rx_list)-sum(df_m_rx_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_rx = df[(df['gender']=='F') & (df['scaled_3']==0) & (df['score_3']!=0)].groupby(by='w3_full_rounds_completed').count()
    df_f_rx_list = list(df_f_rx.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['start', 'OHL', 'Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_f_rx_list),
            sum(df_f_rx_list)-sum(df_f_rx_list[:1]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:2]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:3]),
            sum(df_f_rx_list)-sum(df_f_rx_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"}))
    fig.show()
    
def workout_balance_3_sc(df):
    fig = go.Figure()
    df_m_sc = df[(df['gender']=='M') & (df['scaled_3']==1) & (df['score_3']!=0)].groupby(by='w3_full_rounds_completed').count()
    df_m_sc_list = list(df_m_sc.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['start', 'OHL', 'Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_m_sc_list),
            sum(df_m_sc_list)-sum(df_m_sc_list[:1]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:2]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:3]),
            sum(df_m_sc_list)-sum(df_m_sc_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_sc = df[(df['gender']=='F') & (df['scaled_2']==1) & (df['score_3']!=0)].groupby(by='w3_full_rounds_completed').count()
    df_f_sc_list = list(df_f_sc.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['start', 'OHL', 'Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_f_sc_list),
            sum(df_f_sc_list)-sum(df_f_sc_list[:1]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:2]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:3]),
            sum(df_f_sc_list)-sum(df_f_sc_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"}))
    fig.show()
    
def workout_balance_3_ta(df):
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    fig = go.Figure()
    df_m_1 = df_ta[df_ta['gender']=='M'].groupby(by='w3_full_rounds_completed').count()
    df_m_1_list = list(df_m_1.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Men',
        y = ['Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_m_1_list),
            sum(df_m_1_list)-sum(df_m_1_list[:1]),
            sum(df_m_1_list)-sum(df_m_1_list[:2]),
            sum(df_m_1_list)-sum(df_m_1_list[:3]),
            sum(df_m_1_list)-sum(df_m_1_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#86CE00"}))
    df_f_1 = df_ta[df_ta['gender']=='F'].groupby(by='w3_full_rounds_completed').count()
    df_f_1_list = list(df_f_1.competitorid)
    fig.add_trace(go.Funnel(
        name = 'Women',
        y = ['Box SU', 'HSPU', 'HS-Walk'],
        x = [
            sum(df_f_1_list),
            sum(df_f_1_list)-sum(df_f_1_list[:1]),
            sum(df_f_1_list)-sum(df_f_1_list[:2]),
            sum(df_f_1_list)-sum(df_f_1_list[:3]),
            sum(df_f_1_list)-sum(df_f_1_list[:4])
        ],
        textinfo = "value+percent initial",
        marker = {"color": "#FBE426"}))
    fig.show()
    
def workout_balance_4(df):
    fig, axes = plt.subplots(1, 3, figsize=(30, 7))
    a = sns.histplot(
        ax=axes[0],
        data=df[df['scaled_4']==0],
        x='w4_reps_total',
        hue='gender',
        bins=33,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    a.set_title('19.4 | Rx')
    a.set_ylabel('')
    a.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    a.set_yticklabels(ylabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[df['scaled_4']==1],
        x='w4_reps_total',
        hue='gender',
        bins=33,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    b.set_title('19.4 | Scaled')
    b.set_ylabel('')
    b.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    b.set_yticklabels(ylabels)
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    c = sns.histplot(
        ax=axes[2],
        data=df_ta,
        x='w4_reps_total',
        hue='gender',
        bins=15,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    c.set_title('19.4 | Top 1%')
    c.set_ylabel('')
    c.set_xlabel('total reps')
    ylabels = ['{:,.1f}'.format(y) + 'k' for y in c.get_yticks()/1000]
    c.set_yticklabels(ylabels);
    
def workout_balance_5(df):
    fig, axes = plt.subplots(1, 3, figsize=(30, 7))
    a = sns.histplot(
        ax=axes[0],
        data=df[df['scaled_5']==0],
        x='w5_reps_total',
        hue='gender',
        bins=15,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    a.set_title('19.5 | Rx')
    a.set_ylabel('')
    a.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    a.set_yticklabels(ylabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[df['scaled_5']==1],
        x='w5_reps_total',
        hue='gender',
        bins=15,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    b.set_title('19.5 | Scaled')
    b.set_ylabel('')
    b.set_xlabel('total reps')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    b.set_yticklabels(ylabels)
    df_ta = df[(df['division']=='Men')|(df['division']=='Women')]
    ta_1 = int(0.01*df_ta.overallrank.max())
    df_ta = df_ta[df_ta['overallrank']<=ta_1]
    c = sns.histplot(
        ax=axes[2],
        data=df_ta,
        x='w5_reps_total',
        hue='gender',
        bins=3,
        multiple='stack',
        palette={"F": "gold", "M": "limegreen"}
    )
    c.set_title('19.5 | Top 1%')
    c.set_ylabel('')
    c.set_xlabel('total reps')
    ylabels = ['{:,.1f}'.format(y) + 'k' for y in c.get_yticks()/1000]
    c.set_yticklabels(ylabels);
    
def ranking_1_m_rx(df):
    df_m = df[(df['division']=='Men')&(df['scaled_1']==0)]
    max_m = (df_m['rank_1'].max())/100
    a_m=list(df_m.groupby(by='w1_reps_total')['rank_1'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w1_reps_total')['w1_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    g=sns.relplot(x=c_m, y=a_m, kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(xlabel='total reps', ylabel='rank [%]', title= '19.1 | Male | Rx');
    
def ranking_1_m_rx_ta(df):
    df_m = df[(df['division']=='Men')&(df['scaled_1']==0)]
    max_m = (df_m['rank_1'].max())/100
    a_m=list(df_m.groupby(by='w1_reps_total')['rank_1'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w1_reps_total')['w1_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    last=58
    g=sns.relplot(x=c_m[-last:], y=a_m[-last:], kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(
        xlabel='total reps',
        ylabel='rank [%]',
        title= '19.1 | Male | Rx | Top 1%')
    g.fig.set_figheight(4)
    g.fig.set_figwidth(7)
    
def ranking_2_m_rx(df):
    df_m = df[(df['division']=='Men')&(df['scaled_2']==0)]
    max_m = (df_m['rank_2'].max())/100
    a_m=list(df_m.groupby(by='w2_reps_total')['rank_2'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w2_reps_total')['w2_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    g=sns.relplot(x=c_m, y=a_m, kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(xlabel='total reps', ylabel='rank [%]', title= '19.2 | Male | Rx');
    
def ranking_2_m_rx_ta(df):
    df_m = df[(df['division']=='Men')&(df['scaled_2']==0)]
    max_m = (df_m['rank_2'].max())/100
    a_m=list(df_m.groupby(by='w2_reps_total')['rank_2'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w2_reps_total')['w2_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    last=30
    g=sns.relplot(x=c_m[-last:], y=a_m[-last:], kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(
        xlabel='total reps',
        ylabel='rank [%]',
        title= '19.2 | Male | Rx | Top 1%')
    g.fig.set_figheight(4)
    g.fig.set_figwidth(7)
    
def ranking_3_m_rx(df):
    df_m = df[(df['division']=='Men')&(df['scaled_3']==0)]
    max_m = (df_m['rank_3'].max())/100
    a_m=list(df_m.groupby(by='w3_reps_total')['rank_3'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w3_reps_total')['w3_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    g=sns.relplot(x=c_m, y=a_m, kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(xlabel='total reps', ylabel='rank [%]', title= '19.3 | Male | Rx');
    
def ranking_3_m_rx_ta(df):
    df_m = df[(df['division']=='Men')&(df['scaled_3']==0)]
    max_m = (df_m['rank_3'].max())/100
    a_m=list(df_m.groupby(by='w3_reps_total')['rank_3'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w3_reps_total')['w3_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    last=27
    g=sns.relplot(x=c_m[-last:], y=a_m[-last:], kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(
        xlabel='total reps',
        ylabel='rank [%]',
        title= '19.3 | Male | Rx | Top 1%')
    g.fig.set_figheight(4)
    g.fig.set_figwidth(7)
    
def ranking_4_m_rx(df):
    df_m = df[(df['division']=='Men')&(df['scaled_4']==0)]
    max_m = (df_m['rank_4'].max())/100
    a_m=list(df_m.groupby(by='w4_reps_total')['rank_4'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w4_reps_total')['w4_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    g=sns.relplot(x=c_m, y=a_m, kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(xlabel='total reps', ylabel='rank [%]', title= '19.4 | Male | Rx');
    
def ranking_4_m_rx_ta(df):
    df_m = df[(df['division']=='Men')&(df['scaled_4']==0)]
    max_m = (df_m['rank_4'].max())/100
    a_m=list(df_m.groupby(by='w4_reps_total')['rank_4'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w4_reps_total')['w4_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    last=15
    g=sns.relplot(x=c_m[-last:], y=a_m[-last:], kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(
        xlabel='total reps',
        ylabel='rank [%]',
        title= '19.4 | Male | Rx | Top 1%')
    g.fig.set_figheight(4)
    g.fig.set_figwidth(7)
    
def ranking_5_m_rx(df):
    df_m = df[(df['division']=='Men')&(df['scaled_5']==0)]
    max_m = (df_m['rank_5'].max())/100
    a_m=list(df_m.groupby(by='w5_reps_total')['rank_5'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w5_reps_total')['w5_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    g=sns.relplot(x=c_m, y=a_m, kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(xlabel='total reps', ylabel='rank [%]', title= '19.5 | Male | Rx');
    
def ranking_5_m_rx_ta(df):
    df_m = df[(df['division']=='Men')&(df['scaled_5']==0)]
    max_m = (df_m['rank_5'].max())/100
    a_m=list(df_m.groupby(by='w5_reps_total')['rank_5'].mean())
    a_m=np.divide(a_m,max_m)
    b_m=list(df_m.groupby(by='w5_reps_total')['w5_reps_total'])
    c_m=[]
    for i in b_m:
        c_m.append(i[0])
    last=20
    g=sns.relplot(x=c_m[-last:], y=a_m[-last:], kind="line",linewidth=4)
    g.fig.set_size_inches(15,5)
    g.set(
        xlabel='total reps',
        ylabel='rank [%]',
        title= '19.5 | Male | Rx | Top 1%')
    g.fig.set_figheight(4)
    g.fig.set_figwidth(7)
    
def regional_participation(df):
    plt.figure(figsize=(18,7))
    g = sns.countplot(
        data=df,
        x='region',
        hue='gender',
        order=df.region.value_counts().iloc[:6].index,
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    g.set_ylabel('')
    g.set_xlabel('')
    g.set_title('Regional Participation')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in g.get_yticks()/1000]
    g.set_yticklabels(ylabels)
    plt.show()
    
def regional_ranking(df):
    plt.figure(figsize=(20,9))
    g = sns.barplot(
        data=df[(df['division']=='Men')|(df['division']=='Women')],
        x='region',
        y='overallrank',
        hue='gender',
        order=df.region.value_counts().iloc[:6].index,
        edgecolor='black',
        palette={"F": "gold", "M": "limegreen"}
    )
    g.set_title('Average Ranking')
    g.set_xlabel('')
    g.set_ylabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in g.get_yticks()/1000]
    g.set_yticklabels(ylabels)
    plt.show()

countries = ['United States', 'Bahamas', 'New Zealand', 'Canada',
       'Russian Federation', 'Kenya', 'Australia', 'Costa Rica',
       'Denmark', 'United Kingdom', 'Sweden', 'Netherlands', 'France',
       'Ireland', 'Switzerland', 'South Africa', 'Germany', 'Argentina',
       'Italy', 'Norway', 'Iceland', 'Zimbabwe', 'Peru', 'Portugal',
       'Korea, Republic of', 'Philippines', 'Colombia', 'Mexico',
       'Singapore', 'Chile', 'Israel', 'Brazil', 'Ukraine', 'Spain',
       'Ecuador', 'United Arab Emirates', 'Slovenia', 'Turkey', 'China',
       'Jamaica', 'Bahrain', 'Czech Republic', 'Malaysia', 'Egypt',
       'Hungary', 'Indonesia', 'Finland', 'Angola', 'Tonga',
       'Trinidad and Tobago', 'Belgium', 'Brunei Darussalam',
       'Afghanistan', 'Austria', 'Croatia', 'Latvia', 'India', 'Malta',
       'Bulgaria', 'Thailand', 'Morocco', 'Greece', 'Iran', 'Japan',
       'Dominican Republic', 'Barbados', 'Honduras', 'Guatemala',
       'Panama', 'Samoa', 'Venezuela', 'Iraq', 'Slovakia', 'Viet Nam',
       'Romania', 'Lebanon', 'Poland', 'Belarus', 'Sri Lanka', 'Kuwait',
       'Palestinian Territory', 'Namibia', 'Estonia', 'Tunisia',
       'Bolivia', 'Saudi Arabia', 'Luxembourg', 'Nigeria',
       'Papua New Guinea', 'Zambia', 'El Salvador', 'Serbia', 'Oman',
       'Macedonia', 'Guyana', 'Tanzania', 'Fiji', 'Andorra', 'Cyprus',
       'Nicaragua', 'Belize', 'Jordan', 'Qatar', 'Uruguay', 'Lithuania',
       'Montenegro', 'Uganda', 'Paraguay', 'Madagascar', 'Kazakhstan',
       'Cambodia', 'San Marino', 'Mauritius', 'Algeria', 'Suriname',
       'Saint Vincent/Grenadines', 'Bosnia and Herzegovina',
       'Congo, The Republic of', 'Libya', 'Pakistan', 'Mozambique',
       'Liechtenstein', 'Moldova', 'Syrian Arab Republic', 'Kyrgyzstan',
       'Saint Lucia', 'Uzbekistan', 'Azerbaijan', 'Senegal',
       'Congo, The Democratic Republic of the', 'Mongolia', 'Kosovo',
       'Botswana', 'Djibouti', 'Armenia', 'Georgia', 'Somalia', 'Vanuatu',
       "Côte d'Ivoire", 'Ghana', 'Antigua and Barbuda', 'Tajikistan',
       'Nepal', 'Yemen', 'Rwanda', 'Tuvalu', 'Myanmar', 'Guinea-Bissau',
       'Maldives', 'Eritrea', 'Niger', 'Albania', 'Cameroon', 'Mali',
       'Malawi', 'Bangladesh']    

def top_countries(df):
    df_x = df[(df['division']=='Men') | (df['division']=='Women')]
    df_1 = df_x[df_x['countryoforiginname']=='United States'].sort_values(by='overallrank')[:100]
    df_2 = df_x[df_x['countryoforiginname']=='Canada'].sort_values(by='overallrank')[:100]
    df_3 = df_x[df_x['countryoforiginname']=='Australia'].sort_values(by='overallrank')[:100]
    df_4 = df_x[df_x['countryoforiginname']=='United Kingdom'].sort_values(by='overallrank')[:100]
    df_5 = df_x[df_x['countryoforiginname']=='France'].sort_values(by='overallrank')[:100]
    df_6 = df_x[df_x['countryoforiginname']=='New Zealand'].sort_values(by='overallrank')[:100]
    df_7 = df_x[df_x['countryoforiginname']=='Brazil'].sort_values(by='overallrank')[:100]
    df_8 = df_x[df_x['countryoforiginname']=='Russian Federation'].sort_values(by='overallrank')[:100]
    df_9 = df_x[df_x['countryoforiginname']=='Sweden'].sort_values(by='overallrank')[:100]
    df_10 = df_x[df_x['countryoforiginname']=='Italy'].sort_values(by='overallrank')[:100]
    df_tot = pd.concat([df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8,df_9,df_10])
    plt.figure(figsize=(20,10))
    g = sns.stripplot(
        data=df_tot,
        x='countryoforiginname',
        y='overallrank',
        hue='gender',
        palette={"F": "gold", "M": "limegreen"},
        edgecolor='black'
    )
    g.set_title('Top 100 of best Countries')
    g.set_xlabel('')
    plt.xticks(rotation=45)
    plt.show()
    
def hspu_results(df_hspu):
    plt.figure(figsize=(10,5))
    g = sns.scatterplot(
        data=df_hspu[(df_hspu['scaled_1']==0)&(df_hspu['scaled_2']==0)].sample(150,random_state=10),
        x='w1_reps_total',
        y='w2_reps_sqcl',
        hue='w3_hspu_status',
        edgecolor='black',
        palette={1: "darkblue", 0: "lightblue"},
    )
    g.set_title('Results of Workouts 1&2 | Rx')
    g.set_xlabel('19.1 - total reps')
    g.set_ylabel('19.2 - Squat Cleans')
    g.legend_.set_title('HSPU?')
    plt.show()
    
def bmu_results(df_bmu):
    plt.figure(figsize=(10,5))
    g = sns.scatterplot(
        data=df_bmu[(df_bmu['scaled_1']==0)&(df_bmu['scaled_2']==0)].sample(150,random_state=10),
        x='w1_reps_total',
        y='w2_reps_sqcl',
        hue='w4_bmu_status',
        edgecolor='black',
        palette={1: "darkblue", 0: "lightblue"}
    )
    g.set_title('Results of Workouts 1&2 | Rx')
    g.set_xlabel('19.1 - total reps')
    g.set_ylabel('19.2 - Squat Cleans')
    g.legend_.set_title('BMU?')
    plt.show()
    
def hspu_benchmark(df_hspu):
    plt.figure(figsize=(10,5))
    g = sns.scatterplot(
        data=df_hspu[df_hspu['gender']=='M'].sample(300,random_state=10),
        x='bs_cleanandjerk',
        y='bs_snatch',
        hue='w3_hspu_status',
        palette={1: "darkblue", 0: "lightblue"},
        edgecolor='black'
    )
    g.set_title('Benchmarks - Clean&Jerk vs. Snatch | Men')
    g.set_xlabel('1RM clean&jerk [kg]')
    g.set_ylabel('1RM snatch [kg]')
    g.legend_.set_title('HSPU?')
    plt.show()
    
def bmu_benchmark(df_bmu):
    plt.figure(figsize=(10,5))
    g = sns.scatterplot(
        data=df_bmu[df_bmu['gender']=='M'].sample(300,random_state=10),
        x='bs_cleanandjerk',
        y='bs_snatch',
        hue='w4_bmu_status',
        palette={1: "darkblue", 0: "lightblue"},
        edgecolor='black'
    )
    g.set_title('Benchmarks - Clean&Jerk vs. Snatch | Men')
    g.set_xlabel('1RM clean&jerk [kg]')
    g.set_ylabel('1RM snatch [kg]')
    g.legend_.set_title('BMU?')
    plt.show()
    
def hspu_body(df_hspu):
    plt.figure(figsize=(8,6))
    g = sns.scatterplot(
        data=df_hspu[df_hspu['gender']=='M'].sample(300,random_state=10),
        x='weight',
        y='height',
        hue='w3_hspu_status',
        palette={1: "darkblue", 0: "lightblue"},
        edgecolor='black'
    )
    g.set_title('Body Measurements | Men')
    g.set_xlabel('weight [kg]')
    g.set_ylabel('height [m]')
    g.legend_.set_title('HSPU?')
    plt.show()
    
def bmu_body(df_bmu):
    plt.figure(figsize=(8,6))
    g = sns.scatterplot(
        data=df_bmu.sample(300,random_state=10),
        x='weight',
        y='height',
        hue='w4_bmu_status',
        palette={1: "darkblue", 0: "lightblue"},
        edgecolor='black'
    )
    g.set_title('Body Measurements | Men')
    g.set_xlabel('weight [kg]')
    g.set_ylabel('height [m]')
    g.legend_.set_title('BMU?')
    plt.show()
    
def scaling_1(df):
    fig, axes = plt.subplots(1,2,figsize=(15,3))
    a = sns.histplot(
        ax=axes[0],
        data=df[(df['division']=='Men')],
        x='overallrank',
        hue='scaled_1',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "gold"}
    )
    a.set_title('19.1 | Men')
    a.set_ylabel('')
    a.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in a.get_xticks()/1000]
    a.set_yticklabels(ylabels)
    a.set_xticklabels(xlabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[(df['division']=='Women')],
        x='overallrank',
        hue='scaled_1',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "limegreen"}
    )
    b.set_title('19.1 | Women')
    b.set_ylabel('')
    b.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in b.get_xticks()/1000]
    b.set_yticklabels(ylabels)
    b.set_xticklabels(xlabels);
    
def scaling_2(df):
    fig, axes = plt.subplots(1,2,figsize=(15,3))
    a = sns.histplot(
        ax=axes[0],
        data=df[(df['division']=='Men')],
        x='overallrank',
        hue='scaled_2',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "gold"}
    )
    a.set_title('19.2 | Men')
    a.set_ylabel('')
    a.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in a.get_xticks()/1000]
    a.set_yticklabels(ylabels)
    a.set_xticklabels(xlabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[(df['division']=='Women')],
        x='overallrank',
        hue='scaled_2',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "limegreen"}
    )
    b.set_title('19.2 | Women')
    b.set_ylabel('')
    b.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in b.get_xticks()/1000]
    b.set_yticklabels(ylabels)
    b.set_xticklabels(xlabels);
    
def scaling_3(df):
    fig, axes = plt.subplots(1,2,figsize=(15,3))
    a = sns.histplot(
        ax=axes[0],
        data=df[(df['division']=='Men')],
        x='overallrank',
        hue='scaled_3',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "gold"}
    )
    a.set_title('19.3 | Men')
    a.set_ylabel('')
    a.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in a.get_xticks()/1000]
    a.set_yticklabels(ylabels)
    a.set_xticklabels(xlabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[(df['division']=='Women')],
        x='overallrank',
        hue='scaled_3',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "limegreen"}
    )
    b.set_title('19.3 | Women')
    b.set_ylabel('')
    b.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in b.get_xticks()/1000]
    b.set_yticklabels(ylabels)
    b.set_xticklabels(xlabels);

def scaling_4(df):
    fig, axes = plt.subplots(1,2,figsize=(15,3))
    a = sns.histplot(
        ax=axes[0],
        data=df[(df['division']=='Men')],
        x='overallrank',
        hue='scaled_4',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "gold"}
    )
    a.set_title('19.4 | Men')
    a.set_ylabel('')
    a.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in a.get_xticks()/1000]
    a.set_yticklabels(ylabels)
    a.set_xticklabels(xlabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[(df['division']=='Women')],
        x='overallrank',
        hue='scaled_4',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "limegreen"}
    )
    b.set_title('19.4 | Women')
    b.set_ylabel('')
    b.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in b.get_xticks()/1000]
    b.set_yticklabels(ylabels)
    b.set_xticklabels(xlabels);
    
def scaling_5(df):
    fig, axes = plt.subplots(1,2,figsize=(15,3))
    a = sns.histplot(
        ax=axes[0],
        data=df[(df['division']=='Men')],
        x='overallrank',
        hue='scaled_5',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "gold"}
    )
    a.set_title('19.5 | Men')
    a.set_ylabel('')
    a.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in a.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in a.get_xticks()/1000]
    a.set_yticklabels(ylabels)
    a.set_xticklabels(xlabels)
    b = sns.histplot(
        ax=axes[1],
        data=df[(df['division']=='Women')],
        x='overallrank',
        hue='scaled_5',
        bins=20,
        multiple='stack',
        palette={1: "darkblue", 0: "limegreen"}
    )
    b.set_title('19.5 | Women')
    b.set_ylabel('')
    b.set_xlabel('Overall Ranking')
    ylabels = ['{:,.0f}'.format(y) + 'k' for y in b.get_yticks()/1000]
    xlabels = ['{:,.0f}'.format(x) + 'k' for x in b.get_xticks()/1000]
    b.set_yticklabels(ylabels)
    b.set_xticklabels(xlabels);
    