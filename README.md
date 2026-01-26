# Customer Churn Analysis - Telecom Industry

**Ishak Islam** | UMID28072552431 | Unified Mentor Internship

## About

This project analyzes customer churn patterns in the telecom industry. Using the IBM Telco Customer Churn dataset (7,043 customers), I explored which factors lead to customers leaving and provided recommendations to reduce churn.

**Main finding:** 26.5% of customers churned, with new customers on month-to-month contracts being the highest risk group.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the analysis
jupyter notebook notebooks/01_customer_churn_analysis.ipynb
```

Then click Cell → Run All to execute the analysis.

## Dataset

- Source: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 7,043 customers, 21 features
- Target: Churn (Yes/No)

Download the dataset and place `WA_Fn-UseC_-Telco-Customer-Churn.csv` in the `data/` folder.

## Project Structure

```
├── data/                 # Dataset
├── notebooks/            # Main analysis notebook
├── scripts/              # Python modules for processing
├── visualizations/       # Generated charts
├── tableau/              # CSV exports for Tableau
├── docs/                 # Documentation
└── requirements.txt
```

## Key Findings

**Churn Rate:** 26.5% (1,869 customers)

**High-risk segments:**
- Month-to-month contracts: 42.7% churn
- New customers (0-12 months): 47.4% churn  
- Electronic check payment: 45.3% churn
- Fiber optic internet: 41.9% churn

**What helps retention:**
- Longer contracts (2-year: only 2.8% churn)
- More services subscribed (6 services: 13.6% churn)
- Automatic payment methods

## Recommendations

1. Focus retention efforts on new customers in their first year
2. Offer incentives to switch from month-to-month to annual contracts
3. Bundle more services together
4. Encourage customers to use automatic payments

## Output Files

After running the notebook:
- `visualizations/` - 8 analysis charts (PNG)
- `tableau/` - Data exports for Tableau dashboards

## Tableau Dashboard

Interactive dashboard: [View on Tableau Public](https://public.tableau.com/app/profile/ishak.islam/viz/CustomerChurnAnalysis-TelecomIndustry/CustomerChurnAnalysis-Dashboard)

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau

## Author

Ishak Islam  
Internship ID: UMID28072552431  
Unified Mentor Internship Program  
January 2026
