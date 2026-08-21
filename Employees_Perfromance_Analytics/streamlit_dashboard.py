from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Employee Performance Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    .stApp {
        background-color: #0e1626;
        color: #f8fafc;
    }

    section[data-testid="stSidebar"] {
        background-color: #111c2e;
    }

    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #aab8cc;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }

    div[data-testid="stMetric"] {
        background-color: #162235;
        border: 1px solid #2a3b55;
        padding: 18px;
        border-radius: 14px;
    }

    div[data-testid="stMetricLabel"] {
        color: #aab8cc;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff;
        font-size: 1.8rem;
    }

    .insight-box {
        background-color: #162235;
        border: 1px solid #2a3b55;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 12px;
    }

    .footer {
        text-align: center;
        color: #7f8da3;
        font-size: 0.85rem;
        padding-top: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    BASE_DIR = Path(__file__).resolve().parent
    DATA_PATH = BASE_DIR / "employees_performance_dataset.csv"

    df = pd.read_csv(DATA_PATH)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing Department values
    if df["Department"].isnull().any():
        df["Department"] = df["Department"].fillna(
            df["Department"].mode()[0]
        )

    # Handle missing Performance Score
    df["Performance_Score"] = pd.to_numeric(
        df["Performance_Score"],
        errors="coerce"
    )

    df["Performance_Score"] = df["Performance_Score"].fillna(
        df["Performance_Score"].median()
    )

    # Handle missing Attendance Percentage
    df["Attendance_Percentage"] = pd.to_numeric(
        df["Attendance_Percentage"],
        errors="coerce"
    )

    df["Attendance_Percentage"] = df["Attendance_Percentage"].fillna(
        df["Attendance_Percentage"].median()
    )

    # Convert joining date
    df["Joining_Date"] = pd.to_datetime(
        df["Joining_Date"],
        errors="coerce"
    )

    # Create useful additional columns
    df["Joining_Year"] = df["Joining_Date"].dt.year

    # Employee category based on performance
    df["Performance_Category"] = pd.cut(
        df["Performance_Score"],
        bins=[-float("inf"), 60, 75, 90, float("inf")],
        labels=[
            "Needs Improvement",
            "Average",
            "Good",
            "Excellent"
        ]
    )

    # Attendance risk category
    df["Attendance_Status"] = pd.cut(
        df["Attendance_Percentage"],
        bins=[-float("inf"), 75, 90, float("inf")],
        labels=[
            "Low Attendance",
            "Moderate Attendance",
            "Excellent Attendance"
        ]
    )

    return df


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 📊 Dashboard Controls")

    st.caption(
        "Customize the employee analytics using the filters below."
    )

    st.divider()

    st.markdown("### 🏢 Department")

    all_departments = sorted(df["Department"].dropna().unique())

    selected_departments = st.multiselect(
        "Select Departments",
        options=all_departments,
        default=all_departments
    )

    st.markdown("### ⭐ Performance Score")

    performance_range = st.slider(
        "Select Performance Range",
        min_value=float(df["Performance_Score"].min()),
        max_value=float(df["Performance_Score"].max()),
        value=(
            float(df["Performance_Score"].min()),
            float(df["Performance_Score"].max())
        )
    )

    st.markdown("### 📅 Attendance")

    attendance_range = st.slider(
        "Select Attendance Range",
        min_value=float(df["Attendance_Percentage"].min()),
        max_value=float(df["Attendance_Percentage"].max()),
        value=(
            float(df["Attendance_Percentage"].min()),
            float(df["Attendance_Percentage"].max())
        )
    )

    st.divider()

    st.markdown("### 📋 Dataset Summary")

    st.write(f"**Total Records:** {len(df)}")
    st.write(f"**Departments:** {df['Department'].nunique()}")

    st.caption("Employee Performance Intelligence System")


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df["Department"].isin(selected_departments))
    &
    (df["Performance_Score"].between(
        performance_range[0],
        performance_range[1]
    ))
    &
    (df["Attendance_Percentage"].between(
        attendance_range[0],
        attendance_range[1]
    ))
].copy()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Employee Performance Intelligence</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Interactive analytics for employee performance, attendance, '
    'department insights and workforce trends.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No employees match the selected filters. "
        "Please adjust the sidebar filters."
    )

    st.stop()


# ============================================================
# KPI METRICS
# ============================================================

total_employees = len(filtered_df)

avg_performance = filtered_df["Performance_Score"].mean()

avg_attendance = filtered_df["Attendance_Percentage"].mean()

low_attendance_count = len(
    filtered_df[
        filtered_df["Attendance_Percentage"] < 75
    ]
)

top_employee = filtered_df.loc[
    filtered_df["Performance_Score"].idxmax()
]

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "👥 Employees",
    f"{total_employees}"
)

col2.metric(
    "⭐ Avg Performance",
    f"{avg_performance:.1f}"
)

col3.metric(
    "📅 Avg Attendance",
    f"{avg_attendance:.1f}%"
)

col4.metric(
    "⚠️ Low Attendance",
    f"{low_attendance_count}"
)

col5.metric(
    "🏆 Top Performer",
    top_employee["Employee_Name"]
)


st.divider()


# ============================================================
# TABS
# ============================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "🏢 Department Analysis",
    "👥 Employee Insights",
    "📈 Attendance Analysis",
    "📥 Reports"
])


# ============================================================
# TAB 1 — OVERVIEW
# ============================================================

with tab1:

    st.markdown(
        '<div class="section-title">📊 Workforce Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # Department Performance
    department_performance = (
        filtered_df
        .groupby("Department")["Performance_Score"]
        .mean()
        .reset_index()
        .sort_values(
            "Performance_Score",
            ascending=False
        )
    )

    fig_department = px.bar(
        department_performance,
        x="Department",
        y="Performance_Score",
        text_auto=".1f",
        title="Average Performance by Department",
        template="plotly_dark"
    )

    fig_department.update_layout(
        height=420,
        paper_bgcolor="#0e1626",
        plot_bgcolor="#0e1626",
        xaxis_title="Department",
        yaxis_title="Average Performance"
    )

    col1.plotly_chart(
        fig_department,
        use_container_width=True
    )

    # Performance Category
    performance_category_counts = (
        filtered_df["Performance_Category"]
        .value_counts()
        .reset_index()
    )

    performance_category_counts.columns = [
        "Category",
        "Employees"
    ]

    fig_category = px.pie(
        performance_category_counts,
        names="Category",
        values="Employees",
        hole=0.55,
        title="Employee Performance Categories",
        template="plotly_dark"
    )

    fig_category.update_layout(
        height=420,
        paper_bgcolor="#0e1626"
    )

    col2.plotly_chart(
        fig_category,
        use_container_width=True
    )


    st.markdown("### 🎯 Key Insights")

    best_department = department_performance.iloc[0]["Department"]

    best_department_score = (
        department_performance.iloc[0]["Performance_Score"]
    )

    lowest_department = department_performance.iloc[-1]["Department"]

    insight_col1, insight_col2, insight_col3 = st.columns(3)

    insight_col1.markdown(
        f"""
        <div class="insight-box">
        🏆 <b>Best Performing Department</b><br><br>
        <h3>{best_department}</h3>
        Average Score: {best_department_score:.1f}
        </div>
        """,
        unsafe_allow_html=True
    )

    insight_col2.markdown(
        f"""
        <div class="insight-box">
        ⚠️ <b>Needs Attention</b><br><br>
        <h3>{lowest_department}</h3>
        Lowest average performance among selected departments.
        </div>
        """,
        unsafe_allow_html=True
    )

    insight_col3.markdown(
        f"""
        <div class="insight-box">
        📅 <b>Attendance Health</b><br><br>
        <h3>{avg_attendance:.1f}%</h3>
        Overall average attendance of selected employees.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# TAB 2 — DEPARTMENT ANALYSIS
# ============================================================

with tab2:

    st.markdown(
        '<div class="section-title">🏢 Department Analysis</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    department_summary = (
        filtered_df
        .groupby("Department")
        .agg(
            Employees=("Employee_ID", "count"),
            Avg_Performance=("Performance_Score", "mean"),
            Avg_Attendance=("Attendance_Percentage", "mean")
        )
        .reset_index()
    )

    fig_attendance = px.bar(
        department_summary,
        x="Department",
        y="Avg_Attendance",
        text_auto=".1f",
        title="Average Attendance by Department",
        template="plotly_dark"
    )

    fig_attendance.update_layout(
        height=420,
        paper_bgcolor="#0e1626",
        plot_bgcolor="#0e1626",
        yaxis_title="Attendance (%)"
    )

    col1.plotly_chart(
        fig_attendance,
        use_container_width=True
    )

    fig_employee_count = px.bar(
        department_summary,
        x="Department",
        y="Employees",
        text_auto=True,
        title="Employee Distribution by Department",
        template="plotly_dark"
    )

    fig_employee_count.update_layout(
        height=420,
        paper_bgcolor="#0e1626",
        plot_bgcolor="#0e1626"
    )

    col2.plotly_chart(
        fig_employee_count,
        use_container_width=True
    )

    st.markdown("### 📋 Department Summary")

    display_summary = department_summary.copy()

    display_summary["Avg_Performance"] = (
        display_summary["Avg_Performance"].round(2)
    )

    display_summary["Avg_Attendance"] = (
        display_summary["Avg_Attendance"].round(2)
    )

    st.dataframe(
        display_summary,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# TAB 3 — EMPLOYEE INSIGHTS
# ============================================================

with tab3:

    st.markdown(
        '<div class="section-title">👥 Employee Performance Insights</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1.4, 1])

    # Top Performers
    top_10 = (
        filtered_df
        .sort_values(
            "Performance_Score",
            ascending=False
        )
        .head(10)
    )

    col1.markdown("### 🏆 Top 10 Performers")

    col1.dataframe(
        top_10[
            [
                "Employee_ID",
                "Employee_Name",
                "Department",
                "Performance_Score",
                "Attendance_Percentage"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    # Performance vs Attendance
    fig_scatter = px.scatter(
        filtered_df,
        x="Attendance_Percentage",
        y="Performance_Score",
        color="Department",
        hover_data=[
            "Employee_Name",
            "Employee_ID"
        ],
        title="Performance vs Attendance",
        template="plotly_dark"
    )

    fig_scatter.update_layout(
        height=500,
        paper_bgcolor="#0e1626",
        plot_bgcolor="#0e1626"
    )

    col2.plotly_chart(
        fig_scatter,
        use_container_width=True
    )


# ============================================================
# TAB 4 — ATTENDANCE ANALYSIS
# ============================================================

with tab4:

    st.markdown(
        '<div class="section-title">📈 Attendance & Workforce Risk Analysis</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    fig_histogram = px.histogram(
        filtered_df,
        x="Attendance_Percentage",
        nbins=15,
        title="Attendance Distribution",
        template="plotly_dark"
    )

    fig_histogram.update_layout(
        height=420,
        paper_bgcolor="#0e1626",
        plot_bgcolor="#0e1626"
    )

    col1.plotly_chart(
        fig_histogram,
        use_container_width=True
    )

    attendance_status_counts = (
        filtered_df["Attendance_Status"]
        .value_counts()
        .reset_index()
    )

    attendance_status_counts.columns = [
        "Status",
        "Employees"
    ]

    fig_status = px.pie(
        attendance_status_counts,
        names="Status",
        values="Employees",
        hole=0.55,
        title="Attendance Risk Categories",
        template="plotly_dark"
    )

    fig_status.update_layout(
        height=420,
        paper_bgcolor="#0e1626"
    )

    col2.plotly_chart(
        fig_status,
        use_container_width=True
    )

    st.markdown("### ⚠️ Employees Requiring Attention")

    low_attendance = (
        filtered_df[
            filtered_df["Attendance_Percentage"] < 75
        ]
        .sort_values("Attendance_Percentage")
    )

    if low_attendance.empty:

        st.success(
            "🎉 Great! No employees have attendance below 75% "
            "under the selected filters."
        )

    else:

        st.dataframe(
            low_attendance[
                [
                    "Employee_ID",
                    "Employee_Name",
                    "Department",
                    "Attendance_Percentage",
                    "Performance_Score"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# TAB 5 — REPORTS
# ============================================================

with tab5:

    st.markdown(
        '<div class="section-title">📥 Export Analytics Report</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Download the currently filtered employee dataset "
        "for further analysis."
    )

    csv = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Filtered Employee Report",
        data=csv,
        file_name="filtered_employee_performance_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("### 📌 Current Filter Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    summary_col1.info(
        f"**Employees Included:** {len(filtered_df)}"
    )

    summary_col2.info(
        f"**Departments Selected:** "
        f"{filtered_df['Department'].nunique()}"
    )

    summary_col3.info(
        f"**Average Performance:** "
        f"{filtered_df['Performance_Score'].mean():.2f}"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        📊 Employee Performance Intelligence Dashboard |
        Built with Python, Streamlit, Pandas & Plotly
    </div>
    """,
    unsafe_allow_html=True
)