# -*- coding: utf-8 -*-
import dataiku
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
heart_disease_joined = dataiku.Dataset("heart_disease_joined")
df = heart_disease_joined.get_dataframe()


def imputeLocationAvg(df, col_name):
    try:
        return df[col_name].fillna(df[col_name + '_avg'])
    except KeyError:
        try:
            return df[col_name].fillna(df['mode_' + col_name])
        except KeyError:
            return df[col_name]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
for col_name in df.columns:
    df[col_name] = imputeLocationAvg(df, col_name)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
heart_disease_imputed_values = dataiku.Dataset("heart_disease_imputed_values")
heart_disease_imputed_values.write_with_schema(heart_disease_imputed_values)