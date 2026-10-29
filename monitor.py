import os
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

ref = pd.read_csv("reference.csv")
cur = pd.read_csv("current.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=cur)

os.makedirs("reports", exist_ok=True)
report.save_html("reports/drift_report.html")

result = report.as_dict()["metrics"][0]["result"]
print("Columns drifted:", result["number_of_drifted_columns"], "/", result["number_of_columns"])
print("Dataset drift  :", result["dataset_drift"])
print("Report saved   : reports/drift_report.html")