"""
Data processing functions for customer churn analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_data(filepath=None):
    """Load the dataset."""
    if filepath is None:
        project_root = Path(__file__).parent.parent
        filepath = project_root / "data" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows")
    return df


def clean_data(df):
    """Clean and add derived features."""
    df_clean = df.copy()
    
    # Fix TotalCharges (some have spaces instead of numbers)
    df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
    df_clean['TotalCharges'] = df_clean['TotalCharges'].fillna(df_clean['MonthlyCharges'])
    
    # Add useful columns
    df_clean['Churn_Binary'] = df_clean['Churn'].map({'Yes': 1, 'No': 0})
    df_clean['tenure_group'] = df_clean['tenure'].apply(_get_tenure_group)
    df_clean['num_services'] = df_clean.apply(_count_services, axis=1)
    
    print(f"Cleaned data: {len(df_clean)} rows")
    return df_clean


def _get_tenure_group(tenure):
    if tenure <= 12:
        return '0-12 months'
    elif tenure <= 24:
        return '13-24 months'
    elif tenure <= 48:
        return '25-48 months'
    elif tenure <= 60:
        return '49-60 months'
    else:
        return '61+ months'


def _count_services(row):
    services = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                'TechSupport', 'StreamingTV', 'StreamingMovies']
    return sum(1 for s in services if row[s] == 'Yes')


def get_churn_stats(df):
    """Get basic churn statistics."""
    return {
        'total': len(df),
        'churned': df['Churn_Binary'].sum(),
        'churn_rate': df['Churn_Binary'].mean() * 100,
        'revenue_at_risk': df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()
    }


def export_for_tableau(df, output_dir=None):
    """Export data for Tableau."""
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "tableau"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(exist_ok=True)
    
    # Main data
    df.to_csv(output_dir / "churn_data_for_tableau.csv", index=False)
    
    # Summary tables
    for col in ['Contract', 'tenure_group', 'InternetService']:
        summary = df.groupby(col)['Churn_Binary'].agg(['sum', 'count', 'mean'])
        summary.columns = ['Churned', 'Total', 'Churn_Rate']
        summary.to_csv(output_dir / f"summary_by_{col.lower()}.csv")
    
    print(f"Exported to {output_dir}")


if __name__ == "__main__":
    df = load_data()
    df_clean = clean_data(df)
    
    stats = get_churn_stats(df_clean)
    print(f"\nChurn rate: {stats['churn_rate']:.1f}%")
    print(f"Revenue at risk: ${stats['revenue_at_risk']:,.0f}")
    
    export_for_tableau(df_clean)
