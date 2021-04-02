# # # # # # # # # # # # # # # # # # # # # # # # #
# CLEANING PROCESS OF ATHLETE'S BENCHMARK STATS #
# # # # # # # # # # # # # # # # # # # # # # # # #

# import relevant libraries
import pandas as pd
import numpy as np

# load the data
df_bs = pd.read_csv('./data/2019_opens_bs_01.csv')

# drop columns which are already in core dataframe
df_bs = df_bs.drop(columns=['fullname','countryoforigin','division','affiliate'])
# drop first columns 'Unnamed'
df_bs = df_bs.loc[:, ~df_bs.columns.str.contains('^Unnamed')]


# # # # # # # # # # # # #
# CLEANING OF FEATURES  #
# # # # # # # # # # # # #

# create clean list of height
# set height between 1.40 and 2.20 meter
height_list = df_bs['height'].to_list()
new_height_list = []
for height in height_list:
    if "\'" in height:
        height = height[:-1].split(sep="'")
        height_m = round(int(height[0])*0.3048 + int(height[1])*0.0254, 2)
        if height_m >= 1.4 and height_m <= 2.2:
            new_height_list.append(height_m)
        else:
            new_height_list.append(np.NaN)
    elif 'cm' in height:
        height_m = int(height.strip('cm'))/100
        if height_m >= 1.4 and height_m <= 2.2:
            new_height_list.append(height_m)
        else:
            new_height_list.append(np.NaN)
    elif height == '--':
        new_height_list.append(np.NaN)
    else:
        new_height_list.append(height)

# create clean list of weight
# set weight between 30 and 160 kg
weight_list = df_bs['weight'].to_list()
new_weight_list = []
for weight in weight_list:
    if 'lb' in weight:
        weight_kg = int(int(weight.strip('lb'))*0.453592)
        if weight_kg > 29 and weight_kg < 161:
            new_weight_list.append(weight_kg)
        else:
            new_weight_list.append(np.NaN)
    elif 'kg' in weight:
        weight_kg = int(float(weight.strip('kg')))
        if weight_kg > 29 and weight_kg < 161:
            new_weight_list.append(weight_kg)
        else:
            new_weight_list.append(np.NaN)
    elif weight == '--':
        new_weight_list.append(np.NaN)
    else:
        new_weight_list.append(weight)

# create clean list of bs_backsquat
# set bs_backsquat between 20 and 250 kg
backsquat_list = df_bs['bs_backsquat'].to_list()
new_backsquat_list = []
for weight in backsquat_list:
    if 'lb' in weight:
        weight_kg = int(int(weight.strip('lb'))*0.453592)
        if weight_kg > 19 and weight_kg < 251:
            new_backsquat_list.append(weight_kg)
        else:
            new_backsquat_list.append(np.NaN)
    elif 'kg' in weight:
        weight_kg = int(int(weight.strip('kg')))
        if weight_kg > 19 and weight_kg < 251:
            new_backsquat_list.append(weight_kg)
        else:
            new_backsquat_list.append(np.NaN)
    elif weight == '--':
        new_backsquat_list.append(np.NaN)
    else:
        new_backsquat_list.append(weight)

# create clean list of bs_cleanandjerk
# set bs_cleanandjerk between 20 and 200 kg
cleanandjerk_list = df_bs['bs_cleanandjerk'].to_list()
new_cleanandjerk_list = []
for weight in cleanandjerk_list:
    if 'lb' in weight:
        weight_kg = int(int(weight.strip('lb'))*0.453592)
        if weight_kg > 19 and weight_kg < 201:
            new_cleanandjerk_list.append(weight_kg)
        else:
            new_cleanandjerk_list.append(np.NaN)
    elif 'kg' in weight:
        weight_kg = int(int(weight.strip('kg')))
        if weight_kg > 19 and weight_kg < 201:
            new_cleanandjerk_list.append(weight_kg)
        else:
            new_cleanandjerk_list.append(np.NaN)
    elif weight == '--':
        new_cleanandjerk_list.append(np.NaN)
    else:
        new_cleanandjerk_list.append(weight)

# create clean list of bs_snatch
# set bs_snatch between 20 and 160 kg
snatch_list = df_bs['bs_snatch'].to_list()
new_snatch_list = []
for weight in snatch_list:
    if 'lb' in weight:
        weight_kg = int(int(weight.strip('lb'))*0.453592)
        if weight_kg > 19 and weight_kg < 161:
            new_snatch_list.append(weight_kg)
        else:
            new_snatch_list.append(np.NaN)
    elif 'kg' in weight:
        weight_kg = int(int(weight.strip('kg')))
        if weight_kg > 19 and weight_kg < 161:
            new_snatch_list.append(weight_kg)
        else:
            new_snatch_list.append(np.NaN)
    elif weight == '--':
        new_snatch_list.append(np.NaN)
    else:
        new_snatch_list.append(weight)

# create clean list of bs_deadlift
# set bs_deadlift between 20 and 300 kg
deadlift_list = df_bs['bs_deadlift'].to_list()
new_deadlift_list = []
for weight in deadlift_list:
    if 'lb' in weight:
        weight_kg = int(int(weight.strip('lb'))*0.453592)
        if weight_kg > 19 and weight_kg < 301:
            new_deadlift_list.append(weight_kg)
        else:
            new_deadlift_list.append(np.NaN)
    elif 'kg' in weight:
        weight_kg = int(int(weight.strip('kg')))
        if weight_kg > 19 and weight_kg < 301:
            new_deadlift_list.append(weight_kg)
        else:
            new_deadlift_list.append(np.NaN)
    elif weight == '--':
        new_deadlift_list.append(np.NaN)
    else:
        new_deadlift_list.append(weight)

# create clean list of bs_fightgonebad
# set bs_fightgonebad between 150 and 600 reps
fightgonebad_list = df_bs['bs_fightgonebad'].to_list()
new_fightgonebad_list = []
for reps in fightgonebad_list:
    if reps == '--':
        new_fightgonebad_list.append(np.NaN)
    else:
        if int(reps) >= 150 and int(reps) <= 600:
            new_fightgonebad_list.append(int(reps))
        else:
            new_fightgonebad_list.append(np.NaN)

# create clean list of bs_maxpull_ups
# set bs_maxpull_ups between 0 and 1000 reps
maxpull_ups_list = df_bs['bs_maxpull_ups'].to_list()
new_maxpull_ups_list = []
for reps in maxpull_ups_list:
    if reps == '--':
        new_maxpull_ups_list.append(np.NaN)
    else:
        if int(reps) >= 0 and int(reps) < 1000:
            new_maxpull_ups_list.append(int(reps))
        else:
            new_maxpull_ups_list.append(np.NaN)

# create clean list of bs_fran
# set bs_fran between 100 and 2000 seconds
fran_list = df_bs['bs_fran'].to_list()
new_fran_list = []
for t in fran_list:
    if t == '--':
        new_fran_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        f_time = int(segm[0])*60 + int(segm[1])
        if f_time > 100 and f_time < 2000:
            new_fran_list.append(f_time)
        else:
            new_fran_list.append(np.NaN)
    else:
        new_fran_list.append(int(t))

# create clean list of bs_grace
# set bs_grace between 50 and 2000 seconds
grace_list = df_bs['bs_grace'].to_list()
new_grace_list = []
for t in grace_list:
    if t == '--':
        new_grace_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        g_time = int(segm[0])*60 + int(segm[1])
        if g_time > 50 and g_time < 2000:
            new_grace_list.append(g_time)
        else:
            new_grace_list.append(np.NaN)
    else:
        new_grace_list.append(int(t))

# create clean list of bs_helen
# set bs_helen between 300 and 1500 seconds
helen_list = df_bs['bs_helen'].to_list()
new_helen_list = []
for t in helen_list:
    if t == '--':
        new_helen_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        h_time = int(segm[0])*60 + int(segm[1])
        if h_time > 300 and h_time < 1500:
            new_helen_list.append(h_time)
        else:
            new_helen_list.append(np.NaN)
    else:
        new_helen_list.append(int(t))

# create clean list of bs_filthy50
# set bs_filthy50 between 500 and 4000 seconds
filthy50_list = df_bs['bs_filthy50'].to_list()
new_filthy50_list = []
for t in filthy50_list:
    if t == '--':
        new_filthy50_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        f_time = int(segm[0])*60 + int(segm[1])
        if f_time > 500 and f_time < 4000:
            new_filthy50_list.append(f_time)
        else:
            new_filthy50_list.append(np.NaN)
    else:
        new_filthy50_list.append(int(t))

# create clean list of bs_sprint400m
# set bs_sprint400m between 50 and 200 seconds
sprint400m_list = df_bs['bs_sprint400m'].to_list()
new_sprint400m_list = []
for t in sprint400m_list:
    if t == '--':
        new_sprint400m_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        s_time = int(segm[0])*60 + int(segm[1])
        if s_time > 50 and s_time < 200:
            new_sprint400m_list.append(s_time)
        else:
            new_sprint400m_list.append(np.NaN)
    else:
        new_sprint400m_list.append(int(t))

# create clean list of bs_run5k
# set bs_run5k between 500 and 5000 seconds
run5k_list = df_bs['bs_run5k'].to_list()
new_run5k_list = []
for t in run5k_list:
    if t == '--':
        new_run5k_list.append(np.NaN)
    elif ':' in t:
        segm = t.split(':')
        f_time = int(segm[0])*60 + int(segm[1])
        if f_time > 500 and f_time < 5000:
            new_run5k_list.append(f_time)
        else:
            new_run5k_list.append(np.NaN)
    else:
        new_run5k_list.append(int(t))


# # # # # # # # # # # #
# DROP & ADD COLUMNS  #
# # # # # # # # # # # #

# drop original columns in dataframe
orig_cols = [
    'height', 'weight', \
    'bs_backsquat', 'bs_cleanandjerk', 'bs_snatch', 'bs_deadlift', \
    'bs_fightgonebad', 'bs_maxpull_ups', 'bs_fran', 'bs_grace', 'bs_helen', 'bs_filthy50', \
    'bs_sprint400m', 'bs_run5k'
]
df_bs = df_bs.drop(columns=orig_cols)

# add clean features to dataframe
df_bs['height'] = new_height_list
df_bs['weight'] = new_weight_list
df_bs['bs_backsquat'] = new_backsquat_list
df_bs['bs_cleanandjerk'] = new_cleanandjerk_list
df_bs['bs_snatch'] = new_snatch_list
df_bs['bs_deadlift'] = new_deadlift_list
df_bs['bs_fightgonebad'] = new_fightgonebad_list
df_bs['bs_maxpull_ups'] = new_maxpull_ups_list
df_bs['bs_fran'] = new_fran_list
df_bs['bs_grace'] = new_grace_list
df_bs['bs_helen'] = new_helen_list
df_bs['bs_filthy50'] = new_filthy50_list
df_bs['bs_sprint400m'] = new_sprint400m_list
df_bs['bs_run5k'] = new_run5k_list

# save dataframe to csv-file
df_bs.to_csv('./data/athletes_bs_clean.csv')