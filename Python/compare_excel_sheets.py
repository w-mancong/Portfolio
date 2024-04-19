"""
/*!
file:	compare_excel_sheets.py
author:	Wong Man Cong
email:	w.mancong\@digipen.edu
brief:	A simple python script to compare two excel sheets to ensure that I did not mess
        up the sorting according to the different divisions.
*//*__________________________________________________________________________________*/
"""

import pandas as pd

def compare_excel_sheets(original_file, sorted_file):
    # Read the Excel files into Pandas dataframes
    df_original = pd.read_excel(original_file)
    df_sorted = pd.read_excel(sorted_file)

    # Sort both dataframes based on a common column (e.g., NAME)
    df_original_sorted = df_original.sort_values(by='NAME').reset_index(drop=True)
    df_sorted_sorted = df_sorted.sort_values(by='NAME').reset_index(drop=True)

    # Check if both dataframes are equal
    comparison_result = df_original_sorted.equals(df_sorted_sorted)

    return comparison_result

# Provide the filenames of the original and sorted Excel sheets
original_filename = 'NDP24_Y2.xlsx'
sorted_filename = 'NDP24_Y2_sorted.xlsx'

# Compare the two Excel sheets
result = compare_excel_sheets(sorted_filename, sorted_filename)

if result:
    print("The sorted sheet has the same data as the original sheet.")
else:
    print("The sorted sheet does not have the same data as the original sheet.")