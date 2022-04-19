#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
City = ["New York", "New Jersey", "Michigan", "California", "Florida", "Massachusetts", "Texas"]
No_of_deaths_in_last_month = [3406, 1469, 662, 583, 582, 526, 461]
No_of_deaths_in_current_month = [4398, 1846, 1288, 382, 879, 430, 321]
df = pd.DataFrame({"City": City, "No_of_deaths_in_last_month":No_of_deaths_in_last_month, "No_of_deaths_in_current_month": No_of_deaths_in_current_month})
print(df)




predicted=[]
significance=[]
for i in No_of_deaths_in_last_month:
    predicted.append((0.30*i)+i)
    significance.append(0.1*i)
print("predicted by scientist",predicted)
print("actual current death value ",No_of_deaths_in_current_month)





#difference between actual and predicted
import numpy as np
n_predicted=np.array(predicted)
n_No_of_deaths_in_current_month=np.array(No_of_deaths_in_current_month)
difference=np.absolute(n_No_of_deaths_in_current_month-n_predicted)
print("difference between predicted and current",difference)
print("signicance of 0.1",significance)


# In[ ]:




