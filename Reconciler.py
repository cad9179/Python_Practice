#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install reconciler


# In[1]:


from reconciler import reconcile
import pandas as pd

# A DataFrame with a column you want to reconcile.
test_df = pd.DataFrame(
    {
        "City": ["Rio de Janeiro", "São Paulo", "São Paulo", "Natal"],
        "Country": ["Q155", "Q155", "Q155", "Q155"]
    }
)
reconciled = reconcile(test_df["City"], type_id="Q515")


# In[5]:


reconciled

