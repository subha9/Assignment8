
# coding: utf-8

# In[7]:


import pandas as pd
def distanceFromZero(data):
    x=0
    y=[]
    df1 = pd.DataFrame(data,columns=['X'])
    for row in df1.itertuples():
        if row.X==0 or row.Index==0:
            x=0
        else:
            x=x+1
        y.append(x)
    df2=df1.assign(Y=y)
    return df2


# In[8]:


distanceFromZero([7,2,0,3,4,2,5,0,3,4])


# In[11]:


import pandas as pd
import numpy as np
dateAr=pd.date_range('2018-01-01','2018-12-31',freq='B')
df1 = pd.DataFrame({'A1':np.random.randint(261,size=261),'B1':dateAr,'C1':dateAr.weekday})
df1.head(5)


# In[12]:


dfSum=df1.query('C1==2').groupby('C1').sum()

dfSum


# In[18]:


dfMean=df1[['B1','A1']].groupby(pd.Grouper(key='B1',freq='M')).mean()
#print("Mean for every Month is:\n")
dfMean


# In[19]:



df2=df1.assign(Q=lambda x:((dateAr.month-1)//4))
dfMax=df2.groupby('Q')['A1','Q'].max()
dfMax.set_index(['A1','Q'],inplace=True)
df2.set_index(['A1','Q'],inplace=True)
dfMax.join(df2,how='left', lsuffix='_l',rsuffix='_r')

