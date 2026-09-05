# 💰 Smart Expense Tracker & Budget Analyzer

> **A polished personal-finance analytics dashboard for understanding spending, budgeting, savings, and future expense trends.**

[🚀 Live Demo](https://sv-expense-tracker.streamlit.app/) · [📦 Repository](https://github.com/Shreya934-bot/Streamlit-Analytics-Projects/tree/main/Expense_Tracker)

---

## ✨ Overview

**Smart Expense Tracker & Budget Analyzer** turns raw expense records into an interactive financial analytics workspace.

Upload an expense CSV and the application automatically validates the data, categorizes transactions, calculates spending and savings metrics, compares actual spending with budgets, surfaces spending insights, visualizes trends, and provides a simple next-month expense estimate.

The project combines **data cleaning, rule-based categorization, aggregation, budgeting logic, time-series analysis, visualization, reporting, and interactive Streamlit UI** into one end-to-end application.

### What the dashboard helps answer

- 💸 How much am I spending?
- 🏷️ Where is most of my money going?
- 📊 Which categories are driving my spending?
- 🎯 Am I staying within my category budgets?
- 💰 How much am I saving?
- 📅 How does spending change over time?
- 🔎 Which individual transactions matter most?
- 🔮 What might next month's spending look like?

> **Note:** The forecasting component is a simple trend-based estimate for analytical purposes. It is not financial advice or a guaranteed prediction.

---

## 🚀 Live Application

### [Launch Smart Expense Tracker](https://sv-expense-tracker.streamlit.app/)

The deployed application is intentionally **upload-driven**. Users upload their own expense CSV from the sidebar to unlock the analytics workspace.

The dashboard provides:

- Spending KPIs
- Smart financial insights
- Budget controls
- Category analysis
- Monthly and daily trends
- Transaction search and filtering
- Budget vs actual analysis
- Trend-based expense forecasting
- Downloadable CSV reports

---

# 🎯 Core Capabilities

## 📥 1. CSV Data Ingestion & Validation

The application accepts expense data through Streamlit's file uploader.

### Required columns

```text
Date
Description
Amount
```

### Optional column

```text
Category
```

The processing layer validates the required schema and prepares the data for downstream analysis.

It also handles:

- Date conversion
- Numeric amount conversion
- Invalid records
- Missing values
- Expense filtering
- Dataset preparation

---

## 🏷️ 2. Automatic Expense Categorization

Transactions can be categorized automatically from their descriptions using keyword-based rules.

Supported categories include:

| Category | Example spending areas |
|---|---|
| 🍽️ Food & Dining | Restaurants, groceries, food |
| 🚗 Transport | Fuel, taxi, metro, travel transport |
| 🛍️ Shopping | Purchases and retail |
| 💡 Bills & Utilities | Electricity, internet, utilities |
| 🎬 Entertainment | Movies, subscriptions, leisure |
| 🏥 Health | Medical and healthcare |
| 📚 Education | Courses, books, learning |
| ✈️ Travel | Trips and travel expenses |
| 🏠 Rent & Housing | Rent and housing costs |
| 💆 Personal Care | Salon and personal-care spending |
| 📦 Other | Unmatched transactions |

This converts unstructured transaction descriptions into a consistent analytical dimension.

---

# 📊 Financial Intelligence

## 💸 3. Spending Overview

The dashboard summarizes the uploaded dataset through high-level KPIs:

- **Total Spent**
- **Savings**
- **Savings Rate**
- **Transaction Count**
- **Average Transaction**

These metrics provide an immediate snapshot of financial activity.

### Savings

```text
Savings = Monthly Income − Total Expenses
```

### Savings Rate

```text
Savings Rate = (Savings ÷ Monthly Income) × 100
```

The dashboard also surfaces contextual insights, such as whether expenses exceed entered income and which category has the highest spending.

---

## 📅 4. Monthly Spending Analysis

Monthly aggregation helps reveal changes in spending over time.

The application generates:

- Monthly total spending
- Monthly transaction counts
- Monthly spending trends
- Month-level comparisons

This makes it easier to identify periods of unusually high or low expenditure.

---

## 📈 5. Daily Spending Analysis

Daily aggregation provides a more granular view of financial activity.

The dashboard can reveal:

- Daily spending spikes
- High-spending periods
- Changes in spending intensity
- Day-level patterns

---

## 🏷️ 6. Category-Level Spending Intelligence

Category summaries show how total expenses are distributed across spending areas.

The analysis can identify:

- Highest-spending category
- Category contribution to total spending
- Relative category sizes
- Concentrated spending areas

This provides a practical way to identify where budget adjustments could have the greatest impact.

---

# 🎯 Budget Control

## 7. Budget vs Actual Analysis

The application compares actual category spending against predefined budgets.

For each category, it evaluates:

| Metric | Meaning |
|---|---|
| Budget | Planned spending limit |
| Actual | Recorded spending |
| Remaining | Budget still available |
| Variance | Difference between budget and actual |
| Utilization | Percentage of budget consumed |
| Status | Within budget / over budget |

### Budget utilization

```text
Budget Utilization =
Actual Spending ÷ Budget × 100
```

The dashboard highlights categories that exceed their allocated budget.

---

## 🎛️ Budget Profiles

The Streamlit interface supports budget configuration through the sidebar.

Users can work with predefined budget profiles and adjust the financial assumptions used by the dashboard.

This allows the same expense dataset to be evaluated under different budgeting approaches.

---

# 🔎 Transaction Intelligence

## 8. Search & Filtering

The **Transactions** section provides an interactive way to explore individual records.

Users can:

- Search transaction descriptions
- Filter by category
- Set a minimum amount
- Inspect transaction-level data
- Review the cleaned dataset

This makes the application useful not only for high-level summaries but also for detailed expense investigation.

---

# 🔮 Forecasting

## 9. Next-Month Expense Estimate

The project includes a lightweight trend-based forecasting component.

The estimate uses the **latest three months of expense data** and applies a simple linear trend to estimate the next month's spending.

Conceptually:

```text
Historical Monthly Spending
          │
          ▼
Select Latest 3 Months
          │
          ▼
Fit Simple Linear Trend
          │
          ▼
Estimate Next Month
```

### Why this approach?

The goal is to provide an interpretable baseline rather than an opaque forecasting system.

It demonstrates how historical time-series information can be transformed into a simple forward-looking estimate.

> ⚠️ This is an educational analytical estimate and should not be interpreted as a financial forecast or investment recommendation.

---

# 📊 Visual Analytics

The analytical workflow produces visualizations for:

### 📈 Monthly Spending Trend

Shows how total spending changes across months.

### 🏷️ Category Distribution

Shows the contribution of each expense category to total spending.

### 📊 Category Spending

Highlights the categories with the largest expense amounts.

### 📉 Daily Spending

Shows changes in spending at the daily level.

### 🎯 Budget vs Actual

Compares planned category budgets with recorded spending.

### 📅 Weekday Spending

Analyzes spending patterns across days of the week.

---

# 📑 Reporting & Export

The project generates reusable CSV reports for further analysis.

Available outputs include:

```text
cleaned_expenses.csv
monthly_expense_summary.csv
category_expense_summary.csv
daily_expense_summary.csv
budget_analysis.csv
```

These reports make the analytical results portable beyond the Streamlit dashboard.

---

# 🧠 Application Architecture

```text
                Expense CSV
                    │
                    ▼
          ┌───────────────────┐
          │ Data Validation   │
          │ & Cleaning        │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Categorization    │
          │ & Preparation     │
          └─────────┬─────────┘
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
      Spending   Budget     Trend
      Analysis   Analysis   Analysis
          │         │         │
          └─────────┼─────────┘
                    ▼
          ┌───────────────────┐
          │ Financial         │
          │ Insights          │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Streamlit         │
          │ Dashboard         │
          └─────────┬─────────┘
                    │
             ┌──────┴──────┐
             ▼             ▼
       Interactive      CSV Reports
       Exploration
```

---

# 🛠️ Technology Stack

### Application

- **Python**
- **Streamlit**

### Data & Numerical Analysis

- **Pandas**
- **NumPy**

### Visualization

- **Plotly**
- **Matplotlib**

### Development

- **Jupyter Notebook**
- **VS Code**
- **Git**
- **GitHub**

### Deployment

- **Streamlit Community Cloud**

---

# 📁 Project Structure

```text
Expense_Tracker/
│
├── app.py
├── expense_tracker.py
├── expense_tracker.ipynb
├── sample_expenses.csv
├── requirements.txt
├── README.md
│
├── charts/
│   ├── 01_monthly_spending_trend.png
│   ├── 03_category_distribution.png
│   ├── 04_daily_spending.png
│   ├── 05_budget_vs_actual.png
│   └── README.md
│
└── reports/
    ├── budget_analysis.csv
    ├── category_expense_summary.csv
    ├── cleaned_expenses.csv
    ├── daily_expense_summary.csv
    └── monthly_expense_summary.csv
```

---

# 📄 Input Dataset Format

A compatible CSV can look like:

```csv
Date,Description,Amount,Category
2026-05-01,Rent,20000,Rent & Housing
2026-05-02,Grocery Store,2500,Food & Dining
2026-05-03,Metro Recharge,800,Transport
```

### Required

```text
Date
Description
Amount
```

### Optional

```text
Category
```

If a category is not supplied or needs to be standardized, the application can use its automatic categorization logic.

---

# ⚙️ Local Setup

Clone the repository:

```bash
git clone https://github.com/Shreya934-bot/Streamlit-Analytics-Projects.git
```

Navigate to the project:

```bash
cd Streamlit-Analytics-Projects/Expense_Tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The dashboard will be available locally at:

```text
http://localhost:8501
```

---

# 📦 Dependencies

The project uses:

```text
pandas
numpy
matplotlib
streamlit
plotly
```

See [`requirements.txt`](requirements.txt) for the deployment dependency specification.

---

# 🔐 Data & Privacy

The application is designed around user-provided CSV data and does not require brokerage credentials or financial-account integrations.

For the public deployment, users should avoid uploading sensitive personal financial information.

The deployed application uses an upload-first workflow, so no private expense dataset is required to be committed to the repository.

---

# ⚠️ Disclaimer

This application is intended for **personal analytics, learning, and demonstration purposes**.

It does not:

- Provide financial advice
- Connect to bank accounts
- Execute transactions
- Guarantee savings
- Guarantee forecast accuracy
- Provide investment recommendations

The next-month estimate is a simple trend-based analytical calculation and should be interpreted accordingly.

---

# 🌱 Future Enhancements

Potential extensions include:

- 📱 Mobile-first expense entry
- 🔐 User authentication
- 🗄️ Persistent database storage
- 🏦 Bank statement import
- 💳 Transaction synchronization
- 🔁 Recurring expense detection
- 🔔 Budget threshold notifications
- 📊 Year-over-year spending comparison
- 📈 Advanced time-series forecasting
- 🤖 ML-based expense forecasting
- 🧠 Personalized spending recommendations
- 📤 PDF financial reports
- ☁️ Multi-user cloud dashboards
- 📆 Recurring budget planning
- 💰 Savings-goal tracking

---

# 🧪 Analytical Concepts Demonstrated

- CSV file handling
- Schema validation
- Data cleaning
- Missing-value handling
- Type conversion
- Data filtering
- Rule-based categorization
- GroupBy aggregation
- Monthly aggregation
- Daily aggregation
- Time-series analysis
- Budget variance analysis
- Percentage calculations
- Savings analysis
- Trend analysis
- Simple linear forecasting
- Data visualization
- Interactive dashboards
- Search and filtering
- CSV report generation

---

# 💡 Why This Project Matters

Expense tracking is easy to reduce to a simple list of transactions. The goal of this application is to go one step further:

```text
Raw Transactions
       ↓
Structured Data
       ↓
Spending Patterns
       ↓
Budget Intelligence
       ↓
Financial Insights
       ↓
Forward-Looking Estimate
```

Instead of simply answering **"What did I spend?"**, the dashboard helps users explore:

> **Where did I spend it, how does that compare with my budget, what patterns are emerging, and what might spending look like next?**

---

## 👩‍💻 Author

**Shreya Verma**

Built with:

`Python` · `Pandas` · `NumPy` · `Plotly` · `Matplotlib` · `Streamlit`

### 🔗 Project

[🚀 Live Application](https://sv-expense-tracker.streamlit.app/)

[📦 GitHub Project](https://github.com/Shreya934-bot/Streamlit-Analytics-Projects/tree/main/Expense_Tracker)

---

> **Smart Expense Tracker — turning everyday transactions into actionable financial insight.**
