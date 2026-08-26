# 📡 SocialPulse — Social Media Trend Analyzer

### AI-Powered Social Media Analytics, Trend Discovery & Engagement Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Data%20Analytics-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Sentiment%20Analysis-NLP-7B2CBF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
</p>

<p align="center">
  <b>An interactive social media intelligence workspace that transforms raw post data into meaningful insights about trends, engagement, audience activity, content performance and sentiment.</b>
</p>

<p align="center">
  🚀 <a href="https://social-pulse-ai.streamlit.app/"><b>View Live Application</b></a>
</p>

---

## 🌐 Live Demo

### 🔗 [Launch SocialPulse](https://social-pulse-ai.streamlit.app/)

The application is deployed using **Streamlit Community Cloud** and can be explored directly from the browser.

---

# ✨ Overview

Social media datasets can contain thousands of posts, hashtags, interactions and timestamps. Turning that raw information into useful insights can be difficult without the right analytical workflow.

**SocialPulse** is an interactive analytics application built to simplify social media trend analysis using **Python, Pandas, visualization libraries, sentiment analysis and Streamlit**.

The platform helps users explore social activity and answer questions such as:

- 🔥 Which hashtags are trending?
- 👤 Which users are the most active?
- ❤️ What content receives the most engagement?
- ⏰ When is the audience most active?
- 📈 How does engagement change over time?
- 🥧 Which content categories dominate the dataset?
- 😊 What is the overall sentiment of social conversations?
- 🔍 How can specific posts or trends be discovered quickly?

---

# 🎯 Project Objectives

The goal of this project is to build an end-to-end **social media analytics and trend intelligence platform** capable of:

> Reading social media post data from CSV files, discovering trending hashtags, identifying active users, calculating engagement, analyzing posting behavior, visualizing trends, detecting sentiment patterns and exporting analytics results.

### Key Capabilities Implemented

- ⭐ Interactive CSV data upload
- ⭐ Bundled demo dataset for instant exploration
- ⭐ Top trending hashtag analysis
- ⭐ Most active user analysis
- ⭐ Engagement calculations
- ⭐ Popular posting time detection
- ⭐ Daily engagement trend visualization
- ⭐ Content category distribution analysis
- ⭐ Sentiment classification
- ⭐ Search and interactive filters
- ⭐ Downloadable analytics report
- ⭐ Downloadable chart images

---

# 🧠 How SocialPulse Works

```text
                 SOCIAL MEDIA DATA
                        │
                        ▼
              ┌────────────────────┐
              │     CSV INPUT      │
              │ Posts • Users      │
              │ Likes • Comments   │
              │ Shares • Timestamps│
              └─────────┬──────────┘
                        │
                        ▼
              ┌────────────────────┐
              │ DATA PREPROCESSING │
              │ Clean • Parse      │
              │ Extract • Validate │
              └─────────┬──────────┘
                        │
                        ▼
        ┌──────────────────────────────────┐
        │       ANALYTICS ENGINE           │
        │                                  │
        │ • Hashtag Extraction             │
        │ • User Activity Analysis         │
        │ • Engagement Calculation         │
        │ • Posting Time Analysis          │
        │ • Content Distribution           │
        │ • Sentiment Analysis             │
        └────────────────┬─────────────────┘
                         │
                         ▼
              ┌────────────────────┐
              │  VISUAL INSIGHTS   │
              │ Charts • Metrics   │
              │ Filters • Search   │
              └─────────┬──────────┘
                        │
                        ▼
              📊 SOCIAL INTELLIGENCE
                        │
                        ▼
              📥 REPORT & CHART EXPORT
```

---

# 📊 Analytics Performed

## 🔥 1. Top Trending Hashtags

SocialPulse extracts hashtags from post content and identifies the most frequently used topics.

Example:

```text
#AI              142 mentions
#MachineLearning  118 mentions
#DataScience       96 mentions
#Python            83 mentions
```

This makes it easy to discover the conversations and topics gaining the most attention.

---

## 👤 2. Most Active Users

The application analyzes posting frequency to identify users contributing the most content.

Insights include:

- Number of posts per user
- User activity rankings
- Most frequent contributors

---

## ❤️ 3. Engagement Analysis

SocialPulse calculates engagement using:

```text
Total Engagement =
Likes + Comments + Shares
```

This creates a unified metric for understanding how strongly users interact with content.

The application can surface:

- Total engagement
- Average engagement
- High-performing content
- Engagement changes over time

---

## ⏰ 4. Popular Posting Time

Post timestamps are analyzed to identify when social activity is strongest.

This helps answer:

> **When are users posting and engaging the most?**

The results can support better content scheduling and publishing decisions.

---

## 📈 5. Daily Engagement Trend

The application aggregates engagement by date and visualizes how audience interaction changes over time.

This can reveal:

- Engagement spikes
- High-performing days
- Activity patterns
- Changes in audience interest

---

## 🥧 6. Content Category Distribution

SocialPulse analyzes the distribution of available content categories and displays their relative contribution to the dataset.

This helps users quickly understand:

- Dominant content types
- Category balance
- Underrepresented topics

---

## 😊 7. Sentiment Analysis

The project includes sentiment analysis to classify posts into:

```text
😊 Positive
😐 Neutral
😟 Negative
```

The resulting distribution provides a quick view of the overall tone of social conversations.

---

# 🔍 Interactive Exploration

SocialPulse is designed as an exploration workspace rather than a static report.

Users can interact with the dataset through:

- 🔎 Search functionality
- 🎯 Content filters
- 📅 Date-based exploration where applicable
- 🏷️ Trend and category analysis
- 👤 User activity exploration
- 😊 Sentiment-based filtering

This makes it easier to move from high-level metrics to specific posts and conversations.

---

# 📊 Visualizations

The project generates and presents four core analytical visualizations:

| Visualization | Insight |
|---|---|
| 🔥 **Top Hashtags Chart** | Shows the most frequently occurring hashtags |
| 📈 **Daily Engagement Trend** | Tracks total engagement over time |
| 🥧 **Content Category Distribution** | Shows the share of each content category |
| 😊 **Sentiment Distribution** | Visualizes Positive, Neutral and Negative content |

The charts are also available for download as PNG files for reporting and presentation purposes.

---

# 🚀 Key Features

## 📂 1. CSV Data Upload

Upload your own social media dataset directly into the application.

The platform is designed around CSV-based analysis, making it easy to work with structured social media data.

---

## 🎮 2. Bundled Demo Dataset

A built-in demo dataset allows the application to be explored immediately without requiring an upload.

This makes the project easier to test and demonstrate.

---

## 🔥 3. Trend Discovery

Automatically identify:

- Popular hashtags
- Frequently discussed topics
- Emerging activity patterns

---

## 👤 4. User Activity Intelligence

Analyze who is contributing the most to the conversation and compare posting activity across users.

---

## ❤️ 5. Engagement Intelligence

Combine likes, comments and shares into a unified engagement metric for stronger content performance analysis.

---

## 😊 6. Sentiment Signals

Classify content into Positive, Neutral and Negative sentiment groups to understand the emotional tone of the dataset.

---

## 📊 7. Interactive Dashboard

The modern Streamlit interface presents:

- KPI metrics
- Trend insights
- Interactive exploration
- Search and filtering
- Analytical charts
- Downloadable results

---

## 📥 8. Exportable Results

Users can download:

- 📄 Analytics reports as CSV
- 🖼️ Generated charts as PNG files

This allows insights to be reused outside the dashboard.

---

# 🖥️ Streamlit Interface

The application is organized as an interactive analytics workspace.

### STEP 01 — Load Data

Choose between:

```text
📂 Upload your own CSV
        OR
🎮 Use the bundled demo dataset
```

### STEP 02 — Explore & Filter

Search and filter the available social media data to focus on specific conversations and patterns.

### STEP 03 — Discover Insights

Analyze:

- 🔥 Trending hashtags
- 👤 Active users
- ❤️ Engagement
- ⏰ Posting time
- 📈 Daily trends
- 🥧 Content distribution
- 😊 Sentiment signals

### STEP 04 — Export Results

Download reports and generated visualizations for further analysis or presentation.

---

# 📁 Project Structure

```text
Social_Media_Trend_Analyzer/
│
├── 🚀 app.py
│       └── Main SocialPulse Streamlit application
│
├── 🐍 social_media_trend_analyzer.py
│       └── Core analytics and trend analysis logic
│
├── 📓 social_media_trend_analyzer.ipynb
│       └── Project experimentation and analysis notebook
│
├── 📊 social_media_posts.csv
│       └── Social media dataset / bundled demo data
│
├── 📊 social_media_analytics_report.csv
│       └── Generated analytics report
│
├── 🖼️ top_hashtags_chart.png
│       └── Trending hashtags visualization
│
├── 🖼️ daily_engagement_trend.png
│       └── Engagement over time visualization
│
├── 🖼️ content_category_distribution.png
│       └── Content category distribution visualization
│
├── 🖼️ sentiment_distribution.png
│       └── Sentiment distribution visualization
│
├── 📦 requirements.txt
│       └── Python dependencies
│
└── 📖 README.md
        └── Project documentation
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming language |
| 🌐 **Streamlit** | Interactive web application |
| 🐼 **Pandas** | Data processing and analysis |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Chart generation |
| 📈 **Plotly** | Interactive data visualizations |
| 😊 **TextBlob / NLP** | Sentiment analysis |
| 📄 **CSV** | Dataset input and report export |

---

# ⚙️ Installation & Local Setup

## 1️⃣ Clone the Repository

```bash
git clone <YOUR-STREAMLIT-ANALYTICS-PROJECTS-REPOSITORY>
```

## 2️⃣ Navigate to the Project

```bash
cd Streamlit-Analytics-Projects/Social_Media_Trend_Analyzer
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---

# ☁️ Deployment

The project is deployed on **Streamlit Community Cloud**.

### 🌐 Live Application

## [📡 Launch SocialPulse — Social Media Trend Analyzer](https://social-pulse-ai.streamlit.app/)

### Deployment Configuration

```text
Repository:
Streamlit-Analytics-Projects

Branch:
main

Main File:
Social_Media_Trend_Analyzer/app.py
```

---

# 🧪 Sample Workflow

### 1. Load Social Media Data

Upload a CSV containing social media posts and related engagement information.

Example structure:

```text
Post ID,User,Content,Hashtags,Category,Likes,Comments,Shares,Timestamp
1,alex,"Exploring AI today","#AI #MachineLearning",Technology,120,18,24,2026-08-20 10:30
2,sam,"Python data tips","#Python #DataScience",Education,95,12,16,2026-08-20 14:15
```

### 2. Explore the Dashboard

Review the high-level metrics and analytical sections.

### 3. Search & Filter

Focus the analysis on relevant posts, categories, users or sentiment groups.

### 4. Analyze Trends

Explore:

```text
🔥 Top Hashtags
👤 Most Active Users
❤️ Engagement Metrics
⏰ Popular Posting Times
📈 Daily Engagement Trend
🥧 Content Category Distribution
😊 Sentiment Distribution
```

### 5. Export Insights

Download the analytics report and chart images for reuse.

---

# 💡 Key Learning Outcomes

Through this project, I strengthened my understanding of:

- Building end-to-end data analytics applications
- Reading and processing CSV datasets
- Data cleaning and transformation
- Hashtag extraction and text processing
- Engagement metric design
- Time-series aggregation
- User activity analysis
- Data visualization
- Sentiment analysis
- Interactive filtering and search
- Streamlit dashboard development
- Exporting analytical reports and images
- Deploying Python applications to the cloud
- Managing multi-project GitHub repositories

---

# 🔮 Future Improvements

Potential future enhancements include:

- 📡 Real-time social media API integration
- 🔴 Live trend monitoring
- 🤖 Advanced transformer-based sentiment analysis
- 🧠 Topic modeling and semantic trend discovery
- 🌍 Language detection and multilingual sentiment analysis
- 📈 Predictive engagement forecasting
- 🔥 Emerging trend alerts
- 👥 Influencer identification and network analysis
- 🗺️ Geographic trend visualization
- 🗄️ Database integration
- 🔐 User authentication
- 📱 Additional platform-specific analytics

---

# ⚠️ Disclaimer

**SocialPulse** is an educational and portfolio project designed to demonstrate skills in:

```text
Python • Data Analytics • NLP • Visualization • Streamlit
```

Sentiment and trend results are dependent on the available dataset and analytical approach. They should be interpreted as supportive insights rather than absolute measures of real-world opinion or social impact.

---

# 👩‍💻 About the Developer

## **Shreya Verma**

AI & Machine Learning enthusiast focused on building practical, interactive and data-driven applications.

This project combines:

```text
Python • Data Analytics • NLP • Data Visualization • Streamlit
```

and represents an end-to-end workflow — from raw social media data ingestion and processing to interactive analytics and a deployed cloud application.

---

<p align="center">

### ⭐ If you found this project interesting, consider giving the repository a star!

**Built with ❤️, Python and a lot of debugging by Shreya Verma**

🚀 **From raw social posts → meaningful trends → actionable social intelligence**

</p>
