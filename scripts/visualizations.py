"""
Visualization functions for customer churn analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Colors
COLORS = ['#2ecc71', '#e74c3c']  # green for No, red for Yes


def save_fig(fig, filename, output_dir=None):
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "visualizations"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(exist_ok=True)
    fig.savefig(output_dir / filename, dpi=300, bbox_inches='tight')


def plot_churn_distribution(df, output_dir=None):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    counts = df['Churn'].value_counts()
    
    # Bar chart
    axes[0].bar(counts.index, counts.values, color=COLORS)
    axes[0].set_title('Churn Distribution')
    axes[0].set_ylabel('Count')
    
    # Pie chart
    axes[1].pie(counts.values, labels=counts.index, autopct='%1.1f%%', colors=COLORS)
    axes[1].set_title('Churn Rate')
    
    plt.tight_layout()
    save_fig(fig, '01_churn_distribution.png', output_dir)
    return fig


def plot_by_category(df, column, output_dir=None, filename=None):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    cross_tab = pd.crosstab(df[column], df['Churn'], normalize='index') * 100
    cross_tab.plot(kind='bar', ax=ax, color=COLORS)
    
    ax.set_title(f'Churn Rate by {column}')
    ax.set_ylabel('Percentage')
    ax.legend(title='Churn')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    if filename:
        save_fig(fig, filename, output_dir)
    return fig


def plot_correlation(df, output_dir=None):
    # Encode categorical columns for correlation
    df_enc = df.copy()
    df_enc['gender'] = df_enc['gender'].map({'Male': 1, 'Female': 0})
    df_enc['Partner'] = df_enc['Partner'].map({'Yes': 1, 'No': 0})
    df_enc['Contract'] = df_enc['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    
    cols = ['SeniorCitizen', 'Partner', 'tenure', 'Contract', 
            'MonthlyCharges', 'TotalCharges', 'Churn_Binary']
    
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = df_enc[cols].corr()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', center=0, ax=ax)
    ax.set_title('Correlation Matrix')
    
    plt.tight_layout()
    save_fig(fig, '08_correlation_matrix.png', output_dir)
    return fig


def create_all_visualizations(df, output_dir=None):
    print("Creating visualizations...")
    
    plot_churn_distribution(df, output_dir)
    plot_by_category(df, 'Contract', output_dir, '02_by_contract.png')
    plot_by_category(df, 'InternetService', output_dir, '03_by_internet.png')
    plot_by_category(df, 'PaymentMethod', output_dir, '04_by_payment.png')
    plot_by_category(df, 'tenure_group', output_dir, '05_by_tenure.png')
    plot_correlation(df, output_dir)
    
    plt.close('all')
    print("Done!")


if __name__ == "__main__":
    from data_processing import load_data, clean_data
    
    df = load_data()
    df_clean = clean_data(df)
    create_all_visualizations(df_clean)
