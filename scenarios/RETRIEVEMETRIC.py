from dataiku.scenario import Scenario
from dataiku import Dataset
from datetime import datetime
import pandas as pd

# The Scenario object is the main handle from which you initiate steps
scenario = Scenario()

# Building a dataset
scenario.build_dataset("heart_disease_imputed_values")
# Computing the metrics
scenario.compute_dataset_metrics("heart_disease_imputed_values")

# Getting the metric
dataset = Dataset("heart_disease_imputed_values")
metrics = dataset.get_last_metric_values()
at_risk_percentage = _____________("python:at_risk_percentage:at_risk_percentage")['lastValues'][-1]['value']

row = {
    "timestamp": datetime.now(),
    "metric": _____________,
}


results = Dataset("results")

df = pd.DataFrame([row])
results.write_dataframe(df)