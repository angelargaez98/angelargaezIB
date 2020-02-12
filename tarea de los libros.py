#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


get_ipython().system('wget https://www.gutenberg.org/files/1342/1342-0.txt')
    


# In[5]:


get_ipython().system('ls')


# In[6]:


get_ipython().system('mv 1342-0.txt pride.txt')


# In[7]:


get_ipython().system('ls')


# In[8]:


get_ipython().system('mv 1342-0.txt Ion.txt')


# In[ ]:


get_ipython().system('mv 1342-0.txt pride.txt')


# In[9]:


get_ipython().system('ls')


# In[25]:


with open ('Ion.txt') as f:
    Ion = f.read()


# In[26]:


with open ('pride.txt') as f:
    pride = f.read()


# In[27]:


with open ('moby.txt') as f:
    moby = f.read()


# In[29]:


print (Ion,pride,moby)


# In[33]:


I=len(Ion.split(' '))


# In[34]:


print (I)


# In[31]:


pal = len(Ion.split(' ')+pride.split(' ') + moby.split(' '))


# In[32]:


print (pal)


# In[35]:


print("Los 3 libros tienen " + str(pal) + " palabras")


# In[39]:


unic_io = len(set(Ion.split(' ')))


# In[40]:


print (unic_io )


# In[41]:


pal_unic = len(set(Ion.split(' ')+pride.split(' ') + moby.split(' ')))


# In[42]:


print (pal_unic)


# In[43]:


print("Los libros  tiene " + str(pal_unic) + " palabras únicas")


# In[46]:


set(Ion.split(' ')+pride.split(' ') + moby.split(' '))


# In[52]:


definir_3 = pd.DataFrame({'palabras': Ion.split(' ')+pride.split(' ') + moby.split(' '), "ocurrencia":1})


# In[53]:


definir_3.head()


# In[54]:


print(", ".join(definir_3.groupby('palabras').count().sort_values(by='ocurrencia', ascending=False).head(20).index.tolist()))


# In[55]:


definir_3.head(20)


# In[56]:


definir_3.groupby('palabras').count()


# In[ ]:




