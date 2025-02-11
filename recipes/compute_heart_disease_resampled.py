# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
from resampling import resampleColumn

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
heart_disease_prepared = dataiku.Dataset("heart_disease_prepared")
df = heart_disease_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = resampleColumn(df, 'chol')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
heart_disease_resampled = dataiku.Dataset("heart_disease_resampled")
heart_disease_resampled.write_with_schema(df)
