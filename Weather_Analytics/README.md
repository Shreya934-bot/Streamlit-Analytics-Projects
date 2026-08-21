
# 🌦️ Weather Data Analytics Dashboard

An interactive Python-based Weather Data Analytics project that analyzes weather data, identifies temperature patterns, compares cities, visualizes weather conditions, predicts future temperature using a moving average, and presents the results through an interactive Streamlit dashboard.

---

## 📌 Project Overview

The **Weather Data Analytics Dashboard** reads weather data from a CSV dataset and transforms it into meaningful insights through data analysis, visualization, report generation, and interactive dashboard development.

The project analyzes temperature patterns across different cities, identifies the hottest and coldest cities, counts rainy and sunny days, and predicts tomorrow's temperature using a moving average approach.

An interactive **Streamlit dashboard** is included to make the analysis easier to explore and understand.

---

## 🎯 Features

- 📄 Read and analyze weather data from a CSV file
- 🌡️ Calculate average temperature for each city
- 🔥 Identify the hottest city
- ❄️ Identify the coldest city
- 🌧️ Count rainy days
- ☀️ Count sunny days
- 📈 Analyze temperature trends over time
- 📊 Visualize weather condition distribution
- 🏙️ Compare average temperatures across cities
- 📄 Export the final analysis report as CSV
- 🔮 Predict tomorrow's temperature using a moving average
- 🖥️ Explore the analysis through an interactive Streamlit dashboard

---

## 📂 Project Structure

```text
Weather_Analytics/
│
├── weather_data.csv
├── weather_analytics.py
├── weather_analytics.ipynb
├── streamlit_dashboard.py
├── final_weather_report.csv
├── temperature_trend.png
├── weather_distribution.png
├── average_temperature_city.png
└── README.md
````

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* Matplotlib
* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📊 Data Analysis

The project performs several weather-related analyses on the dataset.

### 🌡️ Average Temperature per City

The dataset is grouped by city to calculate the average temperature.

```python
df.groupby("City")["Temperature"].mean()
```

This helps compare temperature patterns across different cities.

---

### 🔥 Hottest City

The city with the highest average temperature is identified from the dataset.

---

### ❄️ Coldest City

The city with the lowest average temperature is identified from the dataset.

---

### 🌧️ Rainy Days

The total number of days with rainy weather conditions is calculated.

---

### ☀️ Sunny Days

The total number of days with sunny weather conditions is calculated.

---

## 📈 Visualizations

### 🌡️ Temperature Trend

A line chart visualizes how temperature changes over time and helps identify weather patterns and trends.

**Output:**

```text
temperature_trend.png
```

---

### 🌧️ Weather Distribution

A chart displays the distribution of different weather conditions in the dataset, such as:

* Sunny
* Rainy
* Cloudy
* Other weather conditions

**Output:**

```text
weather_distribution.png
```

---

### 📊 Average Temperature per City

A comparison chart displays the average temperature for each city.

This helps identify:

* The hottest city
* The coldest city
* Temperature differences between cities

**Output:**

```text
average_temperature_city.png
```

---

## 🔮 Temperature Prediction

As an additional analytical feature, the project predicts tomorrow's temperature using a **moving average**.

The moving average uses recent temperature values to estimate the next temperature while smoothing short-term fluctuations.

This provides a simple introduction to time-series analysis and basic forecasting.

---

# 🖥️ Interactive Streamlit Dashboard

The project includes an interactive dashboard built using **Streamlit**.

The dashboard provides a user-friendly interface for exploring weather data and analytics results.

## Dashboard Features

* View the weather dataset
* Analyze key weather metrics
* View average temperature by city
* Identify hottest and coldest cities
* Analyze rainy and sunny days
* Explore temperature trends
* View weather distribution
* Interact with available filters
* View moving average temperature prediction

---

## 📄 Final Report

The processed weather analysis results are exported as:

```text
final_weather_report.csv
```

The report contains important findings and processed analytical results generated from the weather dataset.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Shreya934-bot/Streamlit-Analytics-Projects.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Streamlit-Analytics-Projects/Weather_Analytics
```

### 3️⃣ Install Required Libraries

```bash
pip install pandas matplotlib streamlit
```

### 4️⃣ Run the Python Analysis

```bash
python weather_analytics.py
```

### 5️⃣ Run the Streamlit Dashboard

```bash
streamlit run streamlit_dashboard.py
```

After running the command, Streamlit will generate a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to view the interactive dashboard.

---

## 📚 Key Concepts Practiced

* CSV file handling
* Data analysis using Pandas
* Data grouping and aggregation
* Calculating averages
* Finding maximum and minimum values
* Data filtering
* Weather data analysis
* Data visualization
* Line charts
* Bar charts
* Pie charts
* Time-series trend analysis
* Moving average calculations
* Basic temperature prediction
* CSV report generation
* Interactive dashboard development
* Streamlit

---

## 🎯 Project Outcome

This project demonstrates an end-to-end weather analytics workflow.

Raw weather data is transformed into meaningful insights through:

* Data processing
* Statistical analysis
* City-wise temperature comparison
* Weather condition analysis
* Data visualization
* Report generation
* Moving average prediction
* Interactive dashboard development

---

## 👩‍💻 Author

**Shreya Verma**

Computer Science Engineering student specializing in **Artificial Intelligence & Machine Learning**.

Interested in building practical projects in:

* Machine Learning
* Data Science
* Data Analytics
* Artificial Intelligence
* Python Development

---

## 🔗 Connect With Me

* **GitHub:** [https://github.com/Shreya934-bot](https://github.com/Shreya934-bot)
* **LinkedIn:** [https://www.linkedin.com/in/shreya-verma-2b73b6290/](https://www.linkedin.com/in/shreya-verma-2b73b6290/)

---

⭐ If you found this project interesting, feel free to explore the dashboard and the complete weather analytics workflow!

```


