# 🔐 Fraud Detection & Transaction Intelligence

> **An interactive fraud analytics dashboard that transforms raw transaction data into risk scores, suspicious activity signals, investigation insights, and actionable reports.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

---

## 🌐 Live Demo

### 🚀 **[Open the Fraud Detection Dashboard]**

>`https://shreya-fraud-detection-dashboard.streamlit.app/` 

---

## ✨ Overview

**Fraud Detection & Transaction Intelligence** is an end-to-end data analytics project designed to help explore transaction behaviour and surface potentially suspicious activity.

Instead of relying on a single condition, the application combines multiple signals—such as unusually high transaction amounts, duplicate patterns, frequent account activity, and failed transactions—to generate a **rule-based risk score** for every transaction.

The result is an interactive investigation platform where users can:

- Monitor key transaction metrics
- Identify suspicious and high-risk transactions
- Understand **why** a transaction was flagged
- Investigate accounts with unusual activity
- Explore transaction patterns across time, cities, categories, and payment methods
- Filter and search large sets of transactions
- Export investigation-ready reports

---

# 🎯 Problem Statement

Financial datasets can contain thousands of transactions, making manual investigation slow and difficult.

Important questions include:

> 💰 Which transactions involve unusually large amounts?  
> 🔁 Are there duplicate transaction patterns?  
> 👤 Which accounts are making transactions unusually frequently?  
> ❌ Do failed transactions contribute to suspicious behaviour?  
> 🚨 Which transactions should investigators prioritise first?  

This project addresses these questions through a **rule-based fraud intelligence workflow**.

---

# 🧠 How the Risk Engine Works

Each transaction is evaluated using multiple risk signals.

## Risk Signals

| Signal | Condition | Risk Score |
|---|---|---:|
| 💰 High-value transaction | Amount > ₹50,000 | +40 |
| 💎 Extremely high-value transaction | Amount > ₹100,000 | +20 |
| 👤 Frequent account activity | Account exceeds activity threshold | +25 |
| 🔁 Duplicate transaction pattern | Duplicate detected | +35 |
| ❌ Failed transaction | Status = Failed | +10 |

The final score is capped at **100**.

### Risk Classification

| Score | Level | Meaning |
|---:|---|---|
| 0–24 | 🟢 Low | Low immediate concern |
| 25–49 | 🟡 Medium | Requires attention |
| 50–74 | 🟠 High | Strong investigation candidate |
| 75–100 | 🔴 Critical | Highest investigation priority |

> **Note:** This is a rule-based analytics and prioritisation system, not a trained machine-learning fraud classifier.

---

# 🖥️ Dashboard Features

## 📊 Executive Overview

Get an instant snapshot of transaction activity through key performance indicators such as:

- Total Transactions
- Total Transaction Value
- Average Transaction Amount
- High-Risk Transactions
- Suspicious Transactions
- Suspicious Accounts

---

## 🔍 Smart Investigation Filters

Explore the dataset using interactive controls for:

- 📅 Date range
- 🏷️ Transaction category
- 💳 Payment method
- 🏙️ City
- 📌 Transaction status
- 🚨 Risk level
- ⚠️ Suspicious transactions only
- 🔎 Transaction ID search
- 👤 Account ID search

This allows investigators to narrow thousands of records down to the transactions that matter.

---

## 🚨 Investigation Queue

A dedicated investigation view helps prioritise transactions using:

- Risk Score
- Risk Level
- Risk Reasons
- Transaction Amount
- Account ID
- Transaction Status
- Duplicate Flags
- Frequent Account Flags

The most important feature is **risk explainability**: users can see the reasons behind each transaction's score.

---

## 👤 Account Intelligence

The dashboard provides account-level insights to identify potentially unusual behaviour.

Analyse:

- Transaction frequency
- Total transaction value
- Average transaction amount
- Suspicious transaction counts
- Account-level risk exposure

This makes it easier to move from **transaction investigation** to **behavioural account analysis**.

---

## 📈 Trends & Patterns

Explore transaction behaviour through interactive visualizations covering:

- Daily transaction trends
- Transaction categories
- Payment methods
- City-wise activity
- Risk-level distribution
- Transaction status patterns
- High-value transaction behaviour

---

## 📥 Investigation Report Export

Export the currently filtered transaction data as CSV for:

- Further investigation
- Offline analysis
- Reporting
- Documentation
- Audit workflows

---

# 📂 Dataset Structure

The application expects a CSV file with the following columns:

| Column | Description |
|---|---|
| `Transaction_ID` | Unique identifier for each transaction |
| `Transaction_Date` | Date of the transaction |
| `Account_ID` | Account associated with the transaction |
| `Transaction_Category` | Category or type of transaction |
| `Amount` | Monetary value of the transaction |
| `Payment_Method` | Payment method used |
| `City` | City associated with the transaction |
| `Status` | Transaction status |

The dashboard performs validation to ensure the required columns are available before analysis begins.

---

# 🏗️ Project Architecture

```text
                        ┌─────────────────────────┐
                        │   Transaction Dataset   │
                        │          CSV            │
                        └────────────┬────────────┘
                                     │
                                     ▼
                        ┌─────────────────────────┐
                        │ Data Loading & Cleaning │
                        │ • Date Processing       │
                        │ • Duplicate Checks      │
                        │ • Data Validation       │
                        └────────────┬────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │    Suspicious Activity Engine   │
                    │                                │
                    │ • High-Value Detection         │
                    │ • Duplicate Detection          │
                    │ • Frequent Account Detection   │
                    │ • Failed Transaction Flags     │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │       Risk Scoring Engine       │
                    │                                │
                    │ • Risk Score                   │
                    │ • Risk Level                   │
                    │ • Risk Reasons                 │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │     Streamlit Intelligence     │
                    │          Dashboard             │
                    │                                │
                    │ Overview • Investigation       │
                    │ Accounts • Trends • Export     │
                    └────────────────────────────────┘
```

---

# 📊 Analytics Workflow

```text
Raw Data
   │
   ▼
Data Validation
   │
   ▼
Data Cleaning
   │
   ├── Remove / detect duplicate records
   ├── Convert transaction dates
   └── Prepare analytical features
   │
   ▼
Suspicious Pattern Detection
   │
   ├── High-value transactions
   ├── Frequent account activity
   ├── Duplicate patterns
   └── Failed transactions
   │
   ▼
Risk Scoring
   │
   ▼
Risk Classification
   │
   ▼
Interactive Investigation Dashboard
   │
   ├── Filters & Search
   ├── Transaction Intelligence
   ├── Account Intelligence
   ├── Trends & Patterns
   └── CSV Export
```

---

# 🗂️ Repository Structure

```text
Fraud-Detection-Analytics/
│
├── streamlit_dashboard.py
│   └── Main interactive Streamlit application
│
├── transactions_dataset.csv
│   └── Transaction dataset used for analysis
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_NAME
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run streamlit_dashboard.py
```

The application will then open in your browser.

---

# 📦 Requirements

Your `requirements.txt` should contain:

```text
pandas
streamlit
plotly
```

---

# 🛠️ Tech Stack

| Technology | Role in the Project |
|---|---|
| 🐍 Python | Core application logic |
| 🐼 Pandas | Data cleaning, transformation and analysis |
| 📊 Plotly | Interactive charts and visualizations |
| 🖥️ Streamlit | Interactive dashboard and web interface |
| 📄 CSV | Transaction data storage and report export |

---

# 💡 Questions This Dashboard Can Answer

### Transaction Intelligence

- What is the total value of all transactions?
- Which transactions have the highest amounts?
- How does transaction activity change over time?
- Which categories contain the most transactions?

### Fraud & Risk Intelligence

- Which transactions are considered suspicious?
- Which transactions have the highest risk scores?
- Why was a specific transaction flagged?
- How many transactions fall into each risk category?

### Account Intelligence

- Which accounts transact most frequently?
- Which accounts are associated with the most suspicious activity?
- Which accounts have the highest transaction values?

### Behavioural Analysis

- Which payment methods are used most frequently?
- How does activity vary across cities?
- Are particular statuses associated with elevated risk?

---

# 🚀 Future Improvements

This project can be extended into a more advanced fraud monitoring platform with:

- 🤖 Machine Learning fraud classification
- 🧠 Unsupervised anomaly detection using Isolation Forest
- 🧬 Deep-learning-based anomaly detection
- ⚡ Real-time transaction streaming
- 🔔 Automated critical-risk alerts
- 📧 Email notifications
- 🗄️ SQL / cloud database integration
- 🔐 Authentication and role-based access
- 🗺️ Geographic fraud mapping
- 📡 REST API integration
- 📊 Historical risk monitoring
- 📝 Automated investigation summaries

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

- Data Cleaning
- Exploratory Data Analysis
- Transaction Analytics
- Fraud Pattern Detection
- Rule-Based Risk Scoring
- Risk Classification
- Feature Engineering
- Data Aggregation
- Time-Series Analysis
- Interactive Data Visualization
- Dashboard Development
- Search and Filtering
- CSV Report Generation
- Python Application Development

---

# ⚠️ Disclaimer

This project is built for **educational and analytical purposes**. The risk scoring methodology is rule-based and should not be treated as a production fraud detection model without further validation, domain expertise, testing, and appropriate machine-learning or statistical evaluation.

---

# 👩‍💻 Author

**Shreya Verma**

Computer Science Engineering student specialising in **Artificial Intelligence & Machine Learning**, with interests in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Data Analytics
- Python Development

---

## ⭐ Support

If you find this project interesting, consider giving the repository a **star ⭐**.

It helps showcase the project and supports my journey of building practical **AI, Machine Learning, Data Science, and Analytics projects**.

---

<div align="center">

### 🔐 Turning Raw Transactions into Actionable Risk Intelligence

**Built with Python • Pandas • Plotly • Streamlit**

</div>
