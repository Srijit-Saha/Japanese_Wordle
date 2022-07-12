#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from pathlib import Path
import csv


# In[3]:


f = open("D:\\out_radical.csv",encoding = 'utf-8')
csv_radical = csv.reader(f)
rows_rad = []
for row in csv_radical:
        rows_rad.append(row)


# In[4]:


f = open("D:\\out_kanji.csv",encoding = 'utf-8')
csv_kanji = csv.reader(f)
rows_kan = []
for row in csv_kanji:
        rows_kan.append(row)


# In[5]:


import string
string.ascii_lowercase
alpha_sm=list(string.ascii_lowercase)
alpha_bg = [i.upper() for i in alpha_sm]


# In[6]:


alpha_bg_2 = [ i+j for i in alpha_bg for j in alpha_bg]
alpha_bg_3 = [ i+j+k for i in alpha_bg for j in alpha_bg for k in alpha_bg]
kanji = alpha_bg + alpha_bg_2
x=len(kanji)
y=len(rows_kan)-x
kanji = kanji + alpha_bg_3[:y]
len(kanji)


# In[7]:


alpha_sm_2 = [ i+j for i in alpha_sm for j in alpha_sm]
radical = alpha_sm 
x=len(radical)
y=len(rows_rad)-x
radical = radical + alpha_sm_2[:y]
len(radical)


# In[8]:


#kanji japanese to english
kan_j2e = {}
for i in range(len(rows_kan)):
  kan_j2e[rows_kan[i][0]] = kanji[i]
  

print(kan_j2e)


# In[ ]:


#dumping the kanjis
with open('D:\\updated_test_j2e.txt', 'w', encoding='utf8') as json_file:
    json.dump(dicto, json_file, ensure_ascii=False)


# In[9]:


#radical japanese to english
rad_j2e = {}
for i in range(len(rows_rad)):
  rad_j2e[rows_rad[i][0]] = radical[i]

rad_j2e


# In[ ]:


#dumping the radicals
with open('D:\\updated_test_j2e.txt', 'w', encoding='utf8') as json_file:
    json.dump(dicto, json_file, ensure_ascii=False)


# In[18]:


#text file from japanese to english
dicto = json.loads(Path('D:\\Updated_test_kanji_dictionary.txt').read_text(encoding = 'utf-8'))
for i in dicto:
    for j in range(len(dicto[i])):
        num = dicto[i][j][0]
        kan = dicto[i][j][1]
        for k in range(len(kan)):
            x = kan_j2e[dicto[i][j][1][k]]
            kan[k] = x
        rad_sc = dicto[i][j][2]
        for l in rad_sc:#24
            z = list(l.keys())
            for hj in z:
                l[rad_j2e[hj]] = l[hj]
                del l[hj]
          
    
z = list(dicto.keys())
for i in z:
    dicto[kan_j2e[i]] = dicto[i]
    del dicto[i]           


# In[20]:


#dumping the changed dictionary
with open('D:\\updated_test_j2e.txt', 'w', encoding='utf8') as json_file:
    json.dump(dicto, json_file, ensure_ascii=False)

