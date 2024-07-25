import numpy as np
import math
import pandas as pd
import random
from ydata_profiling import ProfileReport
import matplotlib.pyplot as plt

def generate_profile_report(df_cd):

    # Generate the profile report
    profile = ProfileReport(
        df_cd,
        title="Profiling Data",
        html={"style": {"full_width": True}},
    )
    
    # Export to an HTML file
    profile.to_file("constituents_sample_data_report.html")

# ===========================================================================
# If it's a large data set, take a sample:

# def generate_profile_report_large(sample=False):
#     path = "C:/Users/Lvu/Internal - Analytics/"
#     filename = "constituents_sample_data.csv"
#     file = f"{path}/{filename}"

#     df_cd = pd.read_csv(file)

#     if sample:
#         # If sampling is enabled, take a 15% sample of the dataset
#         description = "Disclaimer: this profiling report was generated using a sample of 15% of the original dataset."
#         df_cd_sample = df_cd.sample(frac=0.15)
        
#         profile = ProfileReport(
#             df_cd_sample,
#             title="Profiling National Multiple Sclerosis Data",
#             dataset={"description": description},
#             html={"style": {"full_width": True}},
#             minimal=True
#         )
        
#         profile.to_file("large_data_report.html")
#     else:
#         # Generate the profile report using the full dataset
#         profile = ProfileReport(
#             df_cd,
#             title="Profiling Synthetic Data",
#             html={"style": {"full_width": True}},
#         )
        
#         profile.to_file("constituents_sample_data_report.html")

# if __name__ == "__main__":
#     generate_profile_report()

    # Set sample to True if we want to generate the report using a sample of the dataset
    # generate_profile_report_large(sample=True)