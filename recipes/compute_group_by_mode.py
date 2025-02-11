# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
heart_disease_prepared = dataiku.Dataset("heart_disease_resampled")
df = heart_disease_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
group_by_mode_df = df.groupby('location', as_index=False)[['fbs', 'restecg', 'exang']].agg(lambda x:x.value_counts().index[0])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
group_by_mode = dataiku.Dataset("group_by_mode")
group_by_mode.write_with_schema(group_by_mode_df)