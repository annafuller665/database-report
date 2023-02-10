import pandas as pd
df_experiments = pd.read_csv("/Users/phillipscitp/Downloads/database report/all_experiments.csv")
df_plates = pd.read_csv("/Users/phillipscitp/Downloads/database report/all_plates.csv")

# Experiment Data report

def experiment_data(df):
    total_exp = len(df)
    total1 = 0
    for val in df["Experiment Complete"]:
        if val == 1:
            total1 += 1
    total2 = 0
    for val in df["Metadata Complete"]:
        if val == 1:
            total2 += 1
    total3 = 0
    for val in df["Experiment Validated"]:
        if val == 1:
            total3 += 1
    phillips = 0
    lithgow = 0
    driscoll = 0
    for lab in df["Lab"]:
        if lab == "Phillips":
            phillips += 1
        if lab == "Lithgow":
            lithgow += 1
        if lab == "Driscoll":
            driscoll += 1
    recent_date = df["Start Date"].max()
    

    return f"Total Experiments: {total_exp}, Experiments Complete: {total1}, Metadata Complete: {total2}, Experiments Validated: {total3}, Phillips Lab Experiment Count: {phillips}, Driscoll Lab Experiment Count: {driscoll}, Lithgow Lab Experiment Count: {lithgow}, Most Recent Start Date: {recent_date}"

# print(experiment_data(df_experiments)) # Ouputs all parameters

# Plate Data Report
def plate_data(df):
    total_plates = len(df)
    strain_counts = df["Strain"].value_counts()
    compounds_counts = df["Compound"].value_counts()
    same_str_comp_count = df[["Strain", "Compound"]].value_counts()
    return f"Strain Count: {strain_counts}, Compound Count: {compounds_counts}, Same Compound and Strain Count: {same_str_comp_count}"

    

# print(plate_data(df_plates)) Ouputs tables with names and values

# Function Output to TXT file steps done on experiments file

experiment_summary = open("experiment_summary.txt", "w")
experiment_summary.write(f"{experiment_data(df_experiments)}")
experiment_summary.close()

def create_txt(desired_filename: str, func, df):
    the_file = open(desired_filename, "w")
    write_file = the_file.write(f"{func(df)}")
    the_file.close()


                          

