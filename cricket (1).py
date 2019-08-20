#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

matches=pd.read_csv('C:/Users/srikrishnan.s/Desktop/project/matches.csv', sep=',')
deliveries=pd.read_csv("C:/Users/srikrishnan.s/Desktop/project/deliveries.csv")


# In[2]:


win_condition = matches[matches['toss_winner']==matches['winner']]
winners_cnt=win_condition['winner'].value_counts()
winners_cnt


# In[3]:


toss_count= matches['toss_winner'].value_counts()
toss_count


# In[11]:


per=(winners_cnt/toss_count)*100
print(per)


# In[5]:


# nbs = deliveries['player_dismissed'].str.extract('^(NaN)')
top_ten=deliveries[deliveries['player_dismissed'].isnull()==False]
# print(top_ten)
# top_ten=top_ten/6
top_ten_VAL=top_ten['bowler'].value_counts()
top_ten_VAL.head(10)


# In[6]:


s=deliveries.groupby(['batsman']).sum()
top_bat=s['batsman_runs']
arr=top_bat.sort_values()
tb=arr.tail(5)
tb.sort_values(ascending=False)


# In[7]:


# Strike Rate = (Total Runs Scored)/(Total Balls Faced)*100
ballsdf=deliveries[deliveries['wide_runs']==0]
totball=ballsdf['batsman'].value_counts()
tot=totball.sort_values(ascending=False).head(50)

sr=(top_bat/tot)*100
sr.sort_values(ascending=False).head(10)


# In[8]:


win_condition = matches[matches['toss_winner']==matches['winner']]
winners_cnt=win_condition['winner'].value_counts()
toss_dec=win_condition['toss_decision'].value_counts()
toss_dec


# In[9]:



ven=matches.groupby(['venue','toss_decision']).size()

ven


# In[54]:




duckworth_1=matches[matches['dl_applied']==0]
duckworth_2=matches[matches['dl_applied']==1]

df1=duckworth_1[['team1','team2']].copy()
df2=duckworth_2[['team1','team2']].copy()
DF1=df1.team1.unique()
DF1=df1.team2.unique()
DF2=df2.team1.unique()
DF2=df2.team2.unique()
test_list=DF1.tolist()
remove_list=DF2.tolist()
new=set(test_list)-set(remove_list)
 
teams1=list(matches.team1.unique())

res = [i for i in teams1 if i not in new]

win_condition = matches[matches['toss_winner']==matches['winner']]

tem=matches.groupby(['toss_winner']).size()

                     


# In[51]:


matches.columns


# In[53]:


matches.toss_winner.value_counts()


# In[63]:


cnt=matches[matches['toss_decision']=='bat']
c=cnt.toss_winner.value_counts()
c


# In[85]:


cnt2=matches[matches['toss_decision']=='field']
c2=cnt2.toss_winner.value_counts()
c2


# In[83]:


x=pd.DataFrame({'batting':c,'fielding':c2})
x

