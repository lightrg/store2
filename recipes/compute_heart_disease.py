# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
from make_frames import parseColumns, stackData, nameColumns, readFolderContent

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
heart_disease = dataiku.___________("BbVlUqgO")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
paths = heart_disease.list_paths_in_partition()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
names_data = '/heart-disease.names'
paths.remove(names_data)
training_data = paths

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
text_data = readFolderContent(names_data, heart_disease)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
cols = parseColumns(text_data)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = stackData(training_data, heart_disease)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = nameColumns(df, cols)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
cleveland_heart_disease = dataiku.Dataset("heart_disease")
cleveland_heart_disease.write_with_schema(df)