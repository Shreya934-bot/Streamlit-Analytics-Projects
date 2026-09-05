# 🧾 Invoice Intelligence

<p align="center">
  <strong>Turn invoice files into structured financial records, payment-status insights, and export-ready reports.</strong>
</p>

<p align="center">
  <a href="https://sv-invoice-intelligence.streamlit.app/">🚀 Live Demo</a>
  &nbsp;•&nbsp;
  <a href="https://github.com/Shreya934-bot/Streamlit-Analytics-Projects/tree/main/Invoice_Processor">📦 Repository</a>
</p>

---

## ✨ Overview

**Invoice Intelligence** is an interactive document-processing and financial analytics application built with Python, Pandas, NumPy, Plotly, Streamlit, pypdf, and ReportLab.

It transforms invoice data from **CSV files or text-based PDF invoices** into structured records and turns those records into useful operational insights.

**Invoice Files → Extraction → Validation → Consolidation → Payment Analysis → Reporting**

---

## 🎯 Core Capabilities

### 📂 Multi-Source Invoice Ingestion
- CSV invoice datasets
- One or more text-based PDF invoices
- Required-field validation
- Date and monetary-value cleaning
- Invoice-line consolidation

### 🧾 Invoice Information Extraction

| Field | Purpose |
|---|---|
| Invoice Number | Unique invoice identification |
| Customer Name | Customer-level reporting |
| Customer Email | Contact information |
| Invoice Date | Invoice timeline |
| Due Date | Payment deadline |
| Item | Product/service description |
| Quantity | Item quantity |
| Unit Price | Per-unit value |
| Line Amount | Item-level value |
| Invoice Total | Total invoice value |

### 🚨 Payment & Overdue Intelligence
- Current vs overdue classification
- Days-overdue calculation
- Total overdue value
- Selected as-of date
- Payment-status monitoring
- Searchable invoice records

### 📊 Interactive Analytics
- Monthly invoice value
- Top customers
- Payment-status distribution
- Invoice value trend
- Overdue monitoring
- Invoice search and filtering
- KPI cards
- Downloadable reports

---

## 🔄 Processing Workflow

```text
Invoice Input
CSV / Text-based PDF
        ↓
File Validation
        ↓
Data Extraction
Fields + Line Items
        ↓
Cleaning & Normalization
        ↓
Invoice Consolidation
        ↓
Payment / Overdue Analysis
        ↓
Charts + Tables + CSV Reports
```

---

## 🧠 Application Architecture

```text
                 ┌──────────────────────┐
                 │     Streamlit UI     │
                 │ Upload / Filters     │
                 └──────────┬───────────┘
                            │
             ┌──────────────┴──────────────┐
             ▼                             ▼
      ┌───────────────┐             ┌───────────────┐
      │ CSV Processing│             │ PDF Extraction │
      │    Pandas     │             │     pypdf      │
      └───────┬───────┘             └───────┬───────┘
              └──────────────┬──────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Clean + Validate │
                    └────────┬─────────┘
                             ▼
                    ┌──────────────────┐
                    │ Consolidate Data │
                    │ + Calculations   │
                    └────────┬─────────┘
                             ▼
              ┌──────────────┴──────────────┐
              ▼                             ▼
       Plotly Analytics                CSV Reports
```

---

## 📥 Expected CSV Structure

Required fields:

```text
Invoice Number
Customer Name
Invoice Date
```

Optional fields can include:

```text
Customer Email
Due Date
Item
Quantity
Unit Price
Amount
Tax
```

A sample dataset is included as `sample_invoices.csv`.

---

## 📤 Generated Reports

The workflow produces export-ready CSV outputs including:

- `consolidated_invoice_report.csv`
- `overdue_invoices.csv`
- `invoice_summary_report.csv`

These reports can be reused for spreadsheet analysis, operational reporting, or downstream data workflows.

---

## 📁 Project Structure

```text
Invoice_Processor/
│
├── app.py
├── invoice_processor.py
├── Invoice_Processor.ipynb
├── requirements.txt
├── README.md
│
├── sample_invoices.csv
│
├── invoices/
│   ├── sample_invoice_001.pdf
│   ├── sample_invoice_002.pdf
│   └── sample_invoice_003.pdf
│
└── reports/
    ├── consolidated_invoice_report.csv
    ├── overdue_invoices.csv
    └── invoice_summary_report.csv
```

| File / Folder | Responsibility |
|---|---|
| `app.py` | Streamlit dashboard |
| `invoice_processor.py` | Core processing and analytics |
| `Invoice_Processor.ipynb` | Notebook implementation |
| `sample_invoices.csv` | Example invoice dataset |
| `invoices/` | Sample PDF invoices |
| `reports/` | Generated CSV reports |
| `requirements.txt` | Project dependencies |

---

## 🛠️ Technology Stack

| Technology | Role |
|---|---|
| **Python** | Application logic |
| **Pandas** | Data processing and aggregation |
| **NumPy** | Numerical operations |
| **Plotly** | Interactive visualization |
| **Streamlit** | Web application |
| **pypdf** | Text-based PDF extraction |
| **ReportLab** | Report/document generation |
| **Jupyter** | Notebook workflow |

---

## 🚀 Run Locally

```bash
git clone https://github.com/Shreya934-bot/Streamlit-Analytics-Projects.git
cd Streamlit-Analytics-Projects/Invoice_Processor
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch:

```bash
streamlit run app.py
```

---

## 🌐 Live Application

### 🚀 Invoice Intelligence

**Live Demo:**  
https://sv-invoice-intelligence.streamlit.app/

The deployed application provides the CSV/PDF processing workflow through a browser-based Streamlit interface.

---

## 🔐 Data Handling

The application is designed around files supplied by the user through the interface.

For real financial documents, use appropriate organizational privacy and security controls. The included sample files are intended for demonstration and testing.

---

## 📚 Concepts Demonstrated

- CSV processing
- PDF text extraction
- File upload handling
- Data validation
- Data cleaning
- Date parsing
- Monetary-value processing
- GroupBy aggregation
- Invoice consolidation
- Customer analysis
- Item-level extraction
- Invoice total calculation
- Payment-status classification
- Days-overdue calculation
- Financial reporting
- CSV export
- Interactive visualization
- Search and filtering
- Streamlit application development

---

## 💡 Why This Project Matters

Invoices are more than documents: they contain structured operational and financial information.

This project demonstrates an end-to-end approach:

```text
Raw Invoice Files
       ↓
Information Extraction
       ↓
Validated Data
       ↓
Financial Metrics
       ↓
Payment Signals
       ↓
Actionable Reports
```

The application combines **document processing, financial analytics, visualization, and interactive application development** in one workflow.

---

## 🔮 Potential Extensions

- OCR for scanned invoices
- More robust invoice-template detection
- Vendor-level analytics
- Customer payment-history analysis
- Payment reminders
- Email integration
- Duplicate invoice detection
- Anomaly detection
- Tax/GST analytics
- Database-backed invoice storage
- Authentication and role-based access
- Automated scheduled reporting
- API-based invoice ingestion

---

## ⚠️ Scope & Limitations

The current extraction pipeline is designed for **text-based PDF invoices**. Scanned or image-only PDFs require OCR and are outside the current lightweight `pypdf` implementation.

PDF extraction can also vary with different invoice layouts and document structures.

---

## 👩‍💻 Author

**Shreya Verma**  
Data • ML • Analytics

---

## ⭐ Project Links

- 🚀 [Live Application](https://sv-invoice-intelligence.streamlit.app/)
- 📦 [GitHub Repository](https://github.com/Shreya934-bot/Streamlit-Analytics-Projects/tree/main/Invoice_Processor)

---

<p align="center">
  <strong>Invoice files in. Structured financial insight out. 🧾📊</strong>
</p>
