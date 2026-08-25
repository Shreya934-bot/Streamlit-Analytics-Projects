# 🤖 ResumeAI — Smart Candidate Screening Tool

### AI-Powered Resume Screening, Candidate Ranking & Skill Gap Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
</p>

<p align="center">
  <b>An intelligent resume screening system that analyzes candidate resumes, evaluates job compatibility, identifies skill gaps, and automatically ranks candidates.</b>
</p>

<p align="center">
  🚀 <a href="https://shreya-ai-resume.streamlit.app/"><b>View Live Application</b></a>
</p>

---

## 🌐 Live Demo

### 🔗 [Launch ResumeAI](https://shreya-ai-resume.streamlit.app/)

The application is deployed using **Streamlit Community Cloud** and is ready to use directly from the browser.

---

# ✨ Overview

Recruiters often need to manually review hundreds of resumes for a single job opening. This process can be time-consuming and inconsistent.

**ResumeAI** is designed to simplify this process using Python, Machine Learning, NLP techniques, and a modern Streamlit interface.

The system allows users to:

- 📄 Upload multiple candidate resumes
- 📊 Support both TXT and CSV resume formats
- 🧠 Extract candidate information
- 🎯 Compare resumes against a job description
- 📈 Calculate an overall Resume Match Score
- 🏆 Rank candidates automatically
- ⚠️ Identify missing or unmatched skills
- ✅ Shortlist candidates based on a configurable threshold
- 📥 Export shortlisted candidates to CSV

---

# 🎯 Project Objectives

This project was built as part of my **Python Internship — Day 26 Challenge**.

The primary objective was to build an AI-powered tool capable of:

> Reading multiple resumes, extracting candidate information, matching candidates against a job description, calculating a compatibility score, ranking applicants, and exporting shortlisted candidates.

### Bonus Features Implemented

- ⭐ Missing Skill / Skill Gap Analysis
- ⭐ Interactive Streamlit Web Interface
- ⭐ TXT and CSV file support
- ⭐ NLP-based text similarity
- ⭐ Weighted multi-factor candidate scoring
- ⭐ Downloadable shortlist results

---

# 🧠 How ResumeAI Works

```text
                 JOB DESCRIPTION
                        │
                        ▼
              ┌──────────────────┐
              │  Extract Skills   │
              │  & Requirements   │
              └────────┬─────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │     CANDIDATE RESUMES         │
        │        TXT / CSV Input        │
        └──────────────┬───────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Data Extraction   │
              │ Name • Skills     │
              │ Experience        │
              │ Education         │
              └────────┬─────────┘
                       │
                       ▼
          ┌───────────────────────────┐
          │   AI / NLP MATCHING       │
          │                           │
          │ • Skill Compatibility     │
          │ • Experience Match        │
          │ • Education Match         │
          │ • NLP Text Similarity     │
          └─────────────┬─────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │  Resume Score     │
              │   Calculation     │
              └────────┬─────────┘
                       │
                       ▼
             🏆 Candidate Rankings
                       │
                       ▼
              📥 Shortlisted CSV
```

---

# 📊 Scoring Model

ResumeAI uses a **weighted scoring model** to evaluate candidates.

| Evaluation Factor | Weight |
|---|---:|
| 🧠 Skill Compatibility | **50%** |
| 💼 Experience Compatibility | **25%** |
| 🎓 Education Compatibility | **15%** |
| 🔤 NLP Text Similarity | **10%** |
| **Total** | **100%** |

### Overall Match Score

```text
Overall Score =
(0.50 × Skill Score)
+ (0.25 × Experience Score)
+ (0.15 × Education Score)
+ (0.10 × NLP Similarity)
```

This approach provides a more balanced evaluation than simply checking whether a keyword appears in a resume.

---

# 🚀 Key Features

## 📂 1. Multiple Resume Input Support

The application supports:

### 📄 TXT Files

Each TXT file can contain an individual candidate's resume.

```text
Name: John Doe

Skills:
Python, SQL, Machine Learning, Pandas

Experience:
3 years

Education:
Bachelor's Degree in Computer Science
```

### 📊 CSV Files

A CSV file can contain multiple candidates.

```text
Name,Skills,Experience,Education
John Doe,"Python, SQL, Machine Learning",3,Bachelor's
Jane Smith,"Python, AWS, Deep Learning",4,Master's
```

---

## 🧠 2. Candidate Information Extraction

The system extracts key candidate details including:

- 👤 Name
- 🛠️ Technical Skills
- 💼 Years of Experience
- 🎓 Education
- 📄 Resume Content

---

## 🎯 3. Job Description Matching

Users can enter or paste a job description containing:

- Required skills
- Experience requirements
- Educational requirements
- Role-specific information

Each candidate is then evaluated against these requirements.

---

## 📈 4. Resume Match Scoring

Every candidate receives an overall compatibility score based on:

- Skill overlap
- Experience compatibility
- Education compatibility
- NLP-based resume-to-job-description similarity

This helps transform raw resume information into a more structured screening result.

---

## ⚠️ 5. Skill Gap Analysis

One of the key features of ResumeAI is identifying skills required for the role but missing from a candidate's profile.

Example:

```text
Required Skills:
Python, SQL, Machine Learning, Docker, AWS

Candidate Skills:
Python, SQL, Machine Learning

Missing Skills:
Docker, AWS
```

This makes the screening process more transparent and helps quickly identify candidate gaps.

---

## 🏆 6. Automatic Candidate Ranking

Candidates are automatically sorted according to their:

> **Overall Resume Match Score**

The highest-scoring candidate appears at the top of the rankings.

---

## ✅ 7. Configurable Shortlisting

The application includes a configurable **shortlist threshold**.

Candidates scoring above the selected threshold are marked as:

```text
SHORTLISTED
```

This gives the user control over how selective the screening process should be.

---

## 📥 8. CSV Export

Shortlisted candidates can be exported into a CSV file for further review.

Example output:

```text
Rank,Name,Match Score,Experience,Education,Status
1,Shreya Verma,91.92,4.0,Master's,Shortlisted
2,John Doe,85.40,3.0,Bachelor's,Shortlisted
```

---

# 🖥️ Streamlit Interface

The project includes a modern interactive interface built using **Streamlit**.

The workflow is divided into three major stages:

### STEP 01 — Define the Role

Enter the job description and define the candidate requirements.

### STEP 02 — Upload Resumes

Upload one or more:

```text
TXT files
CSV files
```

### STEP 03 — Analyze & Rank

The system processes the candidates and displays:

- 🏆 Candidate rankings
- 📊 Match scores
- 🧠 Skills profile
- ⚠️ Skill gaps
- 💼 Experience compatibility
- 🎓 Education compatibility
- 🔤 NLP text similarity
- 📥 Shortlist export

---

# 📁 Project Structure

```text
AI_Resume_Screening_Tool/
│
├── 📓 AI_Resume_Screening_Tool.ipynb
│       └── Project development and experimentation notebook
│
├── 🐍 ai_resume_screening_tool.py
│       └── Core Python implementation
│
├── 🚀 app.py
│       └── Main Streamlit application
│
├── 🐍 app_final_fixed.py
│       └── Final development/backup version
│
├── 📄 candidate_1.txt
├── 📄 candidate_2.txt
├── 📄 candidate_3.txt
├── 📄 candidate_4.txt
├── 📄 candidate_5.txt
│       └── Sample candidate resumes
│
├── 📊 candidates.csv
│       └── Sample multi-candidate CSV input
│
├── 📄 sample_job_description.txt
│       └── Example job description
│
├── 📊 shortlisted_candidates.csv
│       └── Sample generated shortlist output
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
| 🐍 Python | Core programming language |
| 🌐 Streamlit | Interactive web application |
| 🐼 Pandas | CSV processing and data handling |
| 🤖 Scikit-learn | NLP and similarity calculations |
| 🔤 TF-IDF | Text feature extraction |
| 📐 Cosine Similarity | Resume-to-JD similarity matching |
| 📝 Regex | Candidate information extraction |

---

# ⚙️ Installation & Local Setup

## 1️⃣ Clone the Repository

```bash
git clone <YOUR-STREAMLIT-ANALYTICS-PROJECTS-REPOSITORY>
```

## 2️⃣ Navigate to the Project

```bash
cd Streamlit-Analytics-Projects/AI_Resume_Screening_Tool
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

## [🤖 Launch ResumeAI — Smart Candidate Screening Tool](https://shreya-ai-resume.streamlit.app/)

### Deployment Configuration

```text
Repository:
Streamlit-Analytics-Projects

Branch:
main

Main File:
AI_Resume_Screening_Tool/app.py
```

---

# 🧪 Sample Workflow

### 1. Enter a Job Description

For example:

```text
We are looking for a Machine Learning Engineer
with at least 2 years of experience.

Required Skills:
Python, SQL, Machine Learning, Deep Learning,
Scikit-learn, TensorFlow, Pandas, AWS and Docker.

Education:
Bachelor's or Master's degree in Computer Science,
Artificial Intelligence, Data Science or a related field.
```

### 2. Upload Candidate Resumes

Upload:

- Multiple TXT resumes
- A CSV containing multiple candidates
- Or both

### 3. Set the Shortlist Threshold

Choose the minimum match score required for shortlisting.

### 4. Analyze Candidates

ResumeAI calculates compatibility scores and generates rankings.

### 5. Review Results

Analyze:

```text
🏆 Candidate Ranking
📊 Overall Match Score
🧠 Skills Profile
⚠️ Missing Skills
💼 Experience Compatibility
🎓 Education Compatibility
🔤 NLP Text Similarity
```

### 6. Export the Shortlist

Download the shortlisted candidates as a CSV file.

---

# 💡 Key Learning Outcomes

Through this project, I strengthened my understanding of:

- Building end-to-end Python applications
- Processing structured and unstructured data
- Working with TXT and CSV files
- Regular Expressions for information extraction
- NLP preprocessing and text similarity
- TF-IDF Vectorization
- Cosine Similarity
- Feature-based scoring systems
- Candidate ranking algorithms
- DataFrame manipulation using Pandas
- Building interactive applications with Streamlit
- Deploying applications to the cloud
- Managing multi-project GitHub repositories

---

# 🔮 Future Improvements

Potential future enhancements include:

- 📄 PDF and DOCX resume support
- 🤖 Advanced LLM-powered resume understanding
- 🧠 Semantic skill matching
- 📊 Candidate comparison dashboard
- 🔍 Resume keyword highlighting
- 📝 Job description recommendations
- 📧 Automated candidate reports
- 🔐 User authentication
- 🗄️ Database integration
- 📈 Recruitment analytics dashboard
- ⚖️ Bias and fairness analysis for screening results

---

# ⚠️ Disclaimer

ResumeAI is designed as an **educational and portfolio project** to demonstrate Python, Machine Learning, NLP, data processing, and Streamlit development.

The scoring results should be used as an **assistive screening mechanism**, not as the sole basis for real-world hiring decisions.

---

# 👩‍💻 About the Developer

## **Shreya Verma**

AI & Machine Learning enthusiast focused on building practical, data-driven applications.

This project combines:

```text
Python • Machine Learning • NLP • Data Processing • Streamlit
```

and represents an end-to-end implementation — from data ingestion and candidate analysis to an interactive deployed web application.

---

<p align="center">

### ⭐ If you found this project interesting, consider giving the repository a star!

**Built with ❤️, Python and a lot of debugging by Shreya Verma**

🚀 **From raw resumes → intelligent insights → smarter shortlisting**

</p>