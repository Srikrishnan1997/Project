#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

str1="https://clinicaltrials.gov/ct2/results?cond="+input("enter the disease ")+"&term=&cntry=&state=&city=&dist="
html = urlopen(str1)
soup = BeautifulSoup(html, 'lxml')
title = soup.title
text = soup.get_text()
soup.find_all('a')
all_links = soup.find_all("a")
for link in all_links:
    link.get("href")
rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
# print(row_td)
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()


list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)


df = pd.DataFrame(list_rows)
# df.head(10)
df1 = df[0].str.split(',', expand=True)
df1.head(10)

df1.drop(df1.index[0:3])


# In[2]:


col_labels = soup.find_all("th.sorting_disabled")
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
print(all_header)


# In[ ]:




