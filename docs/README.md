# Customer Churn Analysis

**Ishak Islam** | UMID28072552431 | Unified Mentor Internship

## About

Analyzing customer churn in telecom industry using Python and Tableau. The dataset contains 7,043 customers and the overall churn rate is 26.5%.

## Running the Project

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Open the Jupyter notebook:
   ```
   jupyter notebook notebooks/01_customer_churn_analysis.ipynb
   ```

3. Run all cells (Cell → Run All)

## Output

- `visualizations/` - Charts generated from analysis
- `tableau/` - CSV files for Tableau dashboards
- [Tableau Dashboard](https://public.tableau.com/app/profile/ishak.islam/viz/CustomerChurnAnalysis-TelecomIndustry/CustomerChurnAnalysis-Dashboard) - Interactive dashboard

## Key Findings

- Churn rate: 26.5% (1,869 out of 7,043 customers)
- Month-to-month contracts have 42.7% churn
- New customers (0-12 months) have 47.4% churn
- Customers with more services are less likely to churn

## Recommendations

- Offer incentives for longer contracts
- Focus on retaining new customers in first year
- Bundle more services to increase retention
- Move customers to automatic payment methods

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau
