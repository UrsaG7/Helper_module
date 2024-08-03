import pandas as pd
import numpy as np

def remove_outliers(df, verbose=False, keep=None, imputation="median"):
    def _is_outlier(series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return (series < lower_bound) | (series > upper_bound)

    df_clean = df.copy()
    columns_to_check = df.select_dtypes(include=[np.number]).columns
    if keep:
        columns_to_check = [col for col in columns_to_check if col not in keep]

    iteration = 0
    total_rows_dropped = 0
    while True:
        iteration += 1
        rows_to_drop = pd.Series(False, index=df_clean.index)
        
        for column in columns_to_check:
            outliers = _is_outlier(df_clean[column])
            rows_to_drop |= outliers
        
        rows_dropped = rows_to_drop.sum()
        if rows_dropped == 0:
            break
        
        df_clean = df_clean[~rows_to_drop]
        total_rows_dropped += rows_dropped
        
        if verbose:
            print(f"Iteration {iteration}, {rows_dropped} rows dropped")
        
        if imputation == "median":
            df_clean.loc[:, columns_to_check] = df_clean[columns_to_check].fillna(df_clean[columns_to_check].median())
    
    if verbose:
        print(f"Rows dropped from {len(df)} to {len(df_clean)}")
    
    return df_clean