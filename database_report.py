import pandas as pd
df_experiments = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_experiments.csv")
df_experiments_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_experiments_previous.csv")
df_plates1 = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_plates.csv")
df_plates2 = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_pletes_previous.csv")
df_strains = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_strains.csv")
df_strains_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_strains_previous.csv")
df_comps = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_compounds.csv")
df_comps_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/all_compounds_previous.csv")
celest = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/celest_experiment_table.csv")
celest_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/celest_experiment_table_previous.csv")
xcomps = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/xcomps.csv")
xcomps_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/xcomps_previous.csv")
xstrains = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/xstrainthaws.csv")
xstrains_prev = pd.read_csv("/Users/phillipscitp/Desktop/database-report/tables/xstrainthaws_previous.csv")

# Experiment Data report single file

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

# experiment_summary = open("experiment_summary.txt", "w")
# experiment_summary.write(f"{experiment_data(df_experiments)}")
# experiment_summary.close()

def create_txt(desired_filename: str, func, df):
    the_file = open(desired_filename, "w")
    write_file = the_file.write(f"{func(df)}")
    the_file.close()
# Comparison data compiler
def experiment_data_comparison(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14):
    """Comparing previous and current experiment summaries"""
    total_expa = len(df1)
    total_expb = len(df2)
    total1a = 0
    total1b = 0
    for val in df1["Experiment Complete"]:
        if val == 1:
            total1a += 1
    for val in df2["Experiment Complete"]:
        if val == 1:
            total1b += 1
    total2a = 0
    total2b = 0
    for val in df1["Metadata Complete"]:
        if val == 1:
            total2a += 1
    for val in df2["Metadata Complete"]:
        if val == 1:
            total2b += 1
    total3a = 0
    total3b = 0
    for val in df1["Experiment Validated"]:
        if val == 1:
            total3a += 1
    for val in df2["Experiment Validated"]:
        if val == 1:
            total3b += 1
    phillips_a = 0
    lithgow_a = 0
    driscoll_a = 0
    phillips_b = 0
    lithgow_b = 0
    driscoll_b = 0

    for lab in df1["Lab"]:
        if lab == "Phillips":
            phillips_a += 1
        if lab == "Lithgow":
            lithgow_a += 1
        if lab == "Driscoll":
            driscoll_a += 1
    for lab in df2["Lab"]:
        if lab == "Phillips":
            phillips_b += 1
        if lab == "Lithgow":
            lithgow_b += 1
        if lab == "Driscoll":
            driscoll_b += 1
    recent_datea = df1["Start Date"].max()
    recent_dateb = df2["Start Date"].max()
    manual_a =0
    manual_b = 0
    alm_a = 0 
    alm_b = 0
    for type in df1["Type"]:
        if type == "manual_lifespan":
            manual_a += 1
        else:
            alm_a += 1
    for type in df2["Type"]:
        if type == "manual_lifespan":
            manual_b += 1
        else:
            alm_b += 1
    total_plates = len(df3)
    new_plates = total_plates - len(df4)
    new_plate_ids = []
    for id in df3["Plate ID"]:
        if id not in df4["Plate ID"]:
            new_plate_ids.append(id)
    total_strains = len(df5)
    new_strains = total_strains - len(df6)
    
    total_comp = len(df7)
    new_comp = total_comp - len(df8)
    total_celest = len(df9)
    new_celest = total_celest - len(df10)
    total_xcomps = len(df11)
    new_xcomps = total_xcomps - len(df12)
    total_xstrains = len(df13)
    new_xstrains = total_xstrains - len(df14)

    
    
    


    data = {"Total Experiments": total_expa, "New Experiments": total_expa-total_expb, "Total Experiments Completed": total1a, "New Experiments Completed": total1a -total1b, "Total Metadata Completed": total2a, "New Metadata Completed": total2a-total2b, "Total Experiments Validated": total3a, "New Experiments Validated": total3a-total3b, "Total Phillips Lab": phillips_a, "New Phillips Lab": phillips_a-phillips_b, "Total Lithgow Lab": lithgow_a, "New Lithgow Lab": lithgow_a-lithgow_b, "Total Driscoll Lab": driscoll_a, "New Driscoll Lab": driscoll_a-driscoll_b, "Most Recent Start Date": recent_datea, "Total Manual Lifespan Types": manual_a, "New Manual Lifespan Types": manual_a-manual_b, "Total ALM Lifepsan Types": alm_a, "New ALM Lifespan Types": alm_a-alm_b, "Total Plates": total_plates, "New Plates": new_plates, "Total Strains": total_strains, "New Strains": new_strains, "Total Compounds": total_comp, "New Compounds": new_comp, "Total Celest Experiments": total_celest, "New Celest Experiments": new_celest, "Total Xcomp Experiments": total_xcomps, "New Xcomp Experiments": new_xcomps, "Total Xstrain Experiments": total_xstrains, "New Xstrain Experiments": new_xstrains}                      
    compiler_df = pd.DataFrame.from_dict(data, orient="index")
    
    
    
    return compiler_df
 # New Strain Compiler   
def new_strains(df1, df2):
    new_strains_name = []
    new_strains_id = []
    for name in df1["Strain"]:
        if name not in df2["Strain"]:
            new_strains_name.append(name)
    for name in df1["Strain ID"]:
        if name not in df2["Strain ID"]:
            new_strains_id.append(name)
    data = {"New Strain Names": new_strains_name, "New Strain IDs": new_strains_id}
    strain_names_df = pd.DataFrame.from_dict(data, orient = "columns")
    return strain_names_df
new_strains(df_strains, df_strains_prev).to_csv("new_strains_ids.csv")

# New Compound Compiler
def new_compounds(df1, df2):
    new_comp_names = []
    for name in df1["Compound"]:
        if name not in df2["Compound"]:
            new_comp_names.append(name)
    new_comp_ids = []
    for id in df1["Compound ID"]:
        if id not in df2["Compound ID"]:
            new_comp_ids.append(id)
    data = {"New Compound Names": new_comp_names, "New Compound IDs": new_comp_ids}
    compound_names_df = pd.DataFrame.from_dict(data, orient="columns")
    return compound_names_df
new_compounds(df_comps, df_comps_prev).to_csv("new_compounds_names_ids.csv")

experiment_data_comparison(df_experiments, df_experiments_prev, df_plates1, df_plates2, df_strains, df_strains_prev, df_comps, df_comps_prev, celest, celest_prev, xcomps, xcomps_prev, xstrains, xstrains_prev).to_csv("experiment_data_summary.csv")

# Plate Data Comparison Compiler
def plate_data_comparison(df1, df2):
    total_plates1 = len(df1)
    total_plates2 = len(df2)
    return f"There are {total_plates1 - total_plates2} more plates included in the recent plate dataset."

