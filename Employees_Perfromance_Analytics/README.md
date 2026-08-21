
# 📊 Employee Performance Analytics Dashboard

An interactive **Employee Performance Analytics Dashboard** built using **Python, Streamlit, Pandas, Matplotlib, and Plotly**. The application helps analyze employee performance, attendance, department distribution, and top-performing employees through interactive filters, KPI cards, and visualizations.

---

## 🚀 Live Demo

🔗 **Streamlit App:** https://shreya-employee-analytics.streamlit.app/

---

## ✨ Features

### 📌 Interactive Filters
Users can filter the dashboard by:

- 🏢 Department
- 📈 Performance Score Range
- 🕒 Attendance Percentage Range

All dashboard metrics and visualizations update dynamically based on the selected filters.

### 📊 Key Performance Indicators

The dashboard displays important employee insights, including:

- Total Employees
- Average Performance Score
- Average Attendance Percentage
- Employees with Low Attendance
- Top Performing Employee
- Best Performing Department

### 📈 Data Visualizations

The dashboard includes:

- Department-wise Average Performance Analysis
- Performance Comparison Across Departments
- Top 10 Employee Performers
- Attendance Distribution
- Department-wise Employee Distribution
- Low Attendance Employee Analysis

### 🔎 Employee Insights

Users can explore:

- Employee ID
- Employee Name
- Department
- Performance Score
- Attendance Percentage

### 📥 Downloadable Reports

The filtered employee dataset can be downloaded directly as a CSV report.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core Programming Language |
| 🎈 Streamlit | Interactive Web Dashboard |
| 🐼 Pandas | Data Processing and Analysis |
| 📊 Plotly | Interactive Data Visualizations |
| 📉 Matplotlib | Statistical Charts and Graphs |

---

## 📂 Project Structure

```text
Employees_Performance_Analytics/
│
├── streamlit_dashboard.py
├── employees_performance_analytics.py
├── employees_performance_analytics.ipynb
├── employees_performance_dataset.csv
├── final_employee_report.csv
├── attendance_trend.png
├── department_distribution.png
├── performance_comparison.png
├── README.md
└── requirements.txt
````

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shreya934-bot/Streamlit-Analytics-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd Streamlit-Analytics-Projects/Employees_Performance_Analytics
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run streamlit_dashboard.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

---

## 📦 Requirements

The project uses the following main libraries:

```text
streamlit==1.62.0
pandas==3.0.5
matplotlib==3.11.1
plotly==6.9.0
```

---

## 📊 Dataset

The dataset contains employee-related information such as:

* Employee ID
* Employee Name
* Department
* Performance Score
* Attendance Percentage
* Joining Date

The dashboard performs data cleaning before analysis, including:

* Removing duplicate records
* Handling missing department values
* Filling missing performance scores using the median
* Filling missing attendance values using the median
* Converting joining dates into datetime format

---

## 📸 Dashboard Capabilities

The dashboard provides a complete overview of employee performance through interactive analytics.

### Key Insights

* Identify high-performing employees
* Compare performance between departments
* Analyze employee attendance patterns
* Detect employees with attendance below 75%
* Explore department-wise employee distribution
* Generate and download filtered reports

---

## 🎯 Project Objective

The objective of this project is to demonstrate how raw employee data can be transformed into meaningful business insights using data analysis and interactive visualization.

This dashboard can help organizations monitor employee performance, identify attendance-related concerns, and compare performance across different departments.

---

## 👩‍💻 Author

**Shreya Verma**

B.Tech Computer Science Engineering
Specialization in Artificial Intelligence & Machine Learning

🔗 GitHub: [https://github.com/Shreya934-bot](https://github.com/Shreya934-bot)

---

## ⭐ If you found this project useful

Consider giving the repository a **star ⭐**!

```


