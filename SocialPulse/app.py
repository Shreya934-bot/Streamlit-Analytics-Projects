import streamlit as st
import pandas as pd
import plotly.express as px
import re
import io
from pathlib import Path

# ============================================================
# SOCIALPULSE — SOCIAL MEDIA INTELLIGENCE
# Designed & built by Shreya Verma
# ============================================================

st.set_page_config(
    page_title="SocialPulse | Social Intelligence",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------
# THEME
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg: #080D19;
        --panel: #111827;
        --panel-2: #151F33;
        --border: rgba(148, 163, 184, 0.18);
        --text: #F8FAFC;
        --muted: #94A3B8;
        --cyan: #22D3EE;
        --purple: #8B5CF6;
        --pink: #F472B6;
        --green: #34D399;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 0%, rgba(34,211,238,.08), transparent 28%),
            radial-gradient(circle at 90% 5%, rgba(139,92,246,.11), transparent 25%),
            #080D19;
        color: var(--text);
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.25rem;
        padding-bottom: 3rem;
    }

    header[data-testid="stHeader"] {
        background: rgba(8,13,25,.75);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0C1322 0%, #0A101D 100%);
        border-right: 1px solid var(--border);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.25rem;
    }

    .brand-lockup {
        display:flex;
        align-items:center;
        gap:12px;
        margin-bottom: 1.1rem;
    }

    .brand-mark {
        width:46px;
        height:46px;
        display:flex;
        align-items:center;
        justify-content:center;
        border-radius:15px;
        font-size:1.45rem;
        background: linear-gradient(135deg, var(--purple), var(--cyan));
        box-shadow: 0 10px 30px rgba(34,211,238,.18);
    }

    .brand-name {
        font-size:1.22rem;
        font-weight:800;
        letter-spacing:-.4px;
        color:#fff;
    }

    .brand-tag {
        font-size:.74rem;
        color:var(--muted);
        margin-top:2px;
    }

    .sidebar-caption {
        color:#94A3B8;
        line-height:1.55;
        font-size:.88rem;
    }

    .sidebar-section {
        margin: 1.35rem 0 .55rem;
        color:#CBD5E1;
        font-size:.76rem;
        font-weight:800;
        letter-spacing:1.2px;
        text-transform:uppercase;
    }

    .hero {
        position:relative;
        overflow:hidden;
        padding:2.2rem 2.35rem;
        border-radius:28px;
        border:1px solid rgba(148,163,184,.18);
        background:
            linear-gradient(115deg, rgba(124,58,237,.28), rgba(8,13,25,.78) 48%, rgba(6,182,212,.18)),
            #111827;
        box-shadow: 0 24px 80px rgba(0,0,0,.22);
        margin-bottom:1.4rem;
    }

    .hero:after {
        content:"";
        position:absolute;
        width:260px;
        height:260px;
        border-radius:50%;
        right:-80px;
        top:-130px;
        background:rgba(34,211,238,.12);
        filter:blur(10px);
    }

    .eyebrow {
        color:#67E8F9;
        font-size:.76rem;
        font-weight:800;
        letter-spacing:1.4px;
        text-transform:uppercase;
        margin-bottom:.6rem;
    }

    .hero-title {
        font-size:clamp(2.2rem, 5vw, 4.1rem);
        line-height:1;
        font-weight:850;
        letter-spacing:-2px;
        color:#fff;
        margin:0;
    }

    .hero-title span {
        background:linear-gradient(90deg,#A78BFA,#67E8F9);
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    .hero-copy {
        color:#B6C2D9;
        font-size:1rem;
        max-width:720px;
        line-height:1.65;
        margin-top:.9rem;
    }

    .hero-chips {
        display:flex;
        flex-wrap:wrap;
        gap:.55rem;
        margin-top:1.15rem;
    }

    .chip {
        padding:.38rem .72rem;
        border-radius:999px;
        border:1px solid rgba(148,163,184,.2);
        background:rgba(255,255,255,.05);
        color:#DDE7F7;
        font-size:.78rem;
    }

    .section-kicker {
        color:#67E8F9;
        font-size:.72rem;
        font-weight:800;
        letter-spacing:1.2px;
        text-transform:uppercase;
        margin-top:1.4rem;
    }

    .section-title {
        font-size:1.45rem;
        font-weight:800;
        letter-spacing:-.4px;
        color:#F8FAFC;
        margin:.2rem 0 .8rem;
    }

    div[data-testid="stMetric"] {
        background:linear-gradient(180deg, rgba(21,31,51,.96), rgba(13,20,35,.96));
        border:1px solid var(--border);
        border-radius:18px;
        padding:1rem 1.05rem;
        min-height:126px;
    }

    div[data-testid="stMetricLabel"] {
        color:#94A3B8;
        font-size:.78rem;
        text-transform:uppercase;
        letter-spacing:.7px;
    }

    div[data-testid="stMetricValue"] {
        color:#F8FAFC;
        font-size:1.65rem;
        font-weight:800;
    }

    .insight-card {
        height:100%;
        min-height:130px;
        box-sizing:border-box;
        padding:1.15rem;
        border-radius:18px;
        border:1px solid var(--border);
        background:rgba(17,24,39,.78);
    }

    .insight-icon { font-size:1.3rem; }
    .insight-label {
        color:#94A3B8;
        font-size:.76rem;
        text-transform:uppercase;
        letter-spacing:.8px;
        margin-top:.55rem;
    }
    .insight-value {
        color:#fff;
        font-size:1.38rem;
        font-weight:800;
        margin-top:.35rem;
        word-break:break-word;
    }
    .insight-sub {
        color:#64748B;
        font-size:.78rem;
        margin-top:.35rem;
    }

    .welcome-card {
        padding:1.7rem;
        border-radius:22px;
        border:1px dashed rgba(103,232,249,.35);
        background:linear-gradient(135deg, rgba(34,211,238,.07), rgba(139,92,246,.08));
        margin-top:1rem;
    }

    .welcome-title {
        font-size:1.55rem;
        font-weight:800;
        color:#fff;
    }

    .welcome-copy {
        color:#B6C2D9;
        line-height:1.7;
        margin-top:.6rem;
    }

    .footer {
        margin-top:2.5rem;
        padding:1.5rem 0 .3rem;
        border-top:1px solid var(--border);
        text-align:center;
        color:#64748B;
        font-size:.84rem;
    }

    .footer strong { color:#CBD5E1; }

    .stButton > button,
    .stDownloadButton > button {
        border-radius:11px;
        font-weight:700;
        border:1px solid rgba(148,163,184,.25);
    }

    div[data-testid="stFileUploader"] {
        border:1px dashed rgba(103,232,249,.32);
        border-radius:14px;
        padding:.35rem;
        background:rgba(34,211,238,.025);
    }

    div[data-testid="stDataFrame"] {
        border:1px solid var(--border);
        border-radius:14px;
        overflow:hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------
POSITIVE_WORDS = {
    "love", "loved", "amazing", "fantastic", "great", "happy", "excited",
    "wonderful", "excellent", "inspiring", "achievement", "awesome",
    "brilliant", "best", "good", "win", "successful", "success",
}

NEGATIVE_WORDS = {
    "disappointing", "frustrating", "poor", "problems", "issues", "bad",
    "worst", "hate", "terrible", "failed", "failure", "awful", "angry",
    "annoying", "broken",
}


def analyze_sentiment(text):
    text = str(text).lower()
    positive = sum(bool(re.search(rf"\b{re.escape(word)}\b", text)) for word in POSITIVE_WORDS)
    negative = sum(bool(re.search(rf"\b{re.escape(word)}\b", text)) for word in NEGATIVE_WORDS)
    if positive > negative:
        return "Positive"
    if negative > positive:
        return "Negative"
    return "Neutral"


@st.cache_data(show_spinner=False)
def process_data(source_bytes):
    # Streamlit uploads and bundled files are handled as raw bytes.
    # Pandas needs a file-like object, so wrap the bytes in BytesIO.
    df = pd.read_csv(io.BytesIO(source_bytes))

    if "Post_ID" in df.columns:
        df = df.drop_duplicates(subset="Post_ID").copy()
    else:
        df = df.drop_duplicates().copy()

    for col in ["Likes", "Comments", "Shares"]:
        if col not in df.columns:
            df[col] = 0
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).clip(lower=0)

    if "Date" not in df.columns:
        df["Date"] = pd.NaT
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    if "Time" in df.columns:
        parsed_time = pd.to_datetime(df["Time"].astype(str), errors="coerce")
        df["Posting_Hour"] = parsed_time.dt.hour.fillna(0).astype(int)
    else:
        df["Posting_Hour"] = 0

    for col in ["User", "Category", "Content", "Hashtags"]:
        if col not in df.columns:
            df[col] = ""
        df[col] = df[col].fillna("").astype(str)

    df["Total_Engagement"] = df["Likes"] + df["Comments"] + df["Shares"]
    df["Sentiment"] = df["Content"].apply(analyze_sentiment)
    return df


def get_hashtag_data(data):
    tags = []
    for value in data.get("Hashtags", pd.Series(dtype=str)).dropna():
        tags.extend(re.findall(r"#\w+", str(value).lower()))
    if not tags:
        return pd.DataFrame(columns=["Hashtag", "Count"])
    result = pd.Series(tags).value_counts().rename_axis("Hashtag").reset_index(name="Count")
    return result


def chart_layout(fig, height=390):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        margin=dict(l=18, r=18, t=35, b=18),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(17,24,39,.25)",
        font=dict(color="#CBD5E1"),
        legend_title_text="",
    )
    fig.update_xaxes(gridcolor="rgba(148,163,184,.10)", zerolinecolor="rgba(148,163,184,.15)")
    fig.update_yaxes(gridcolor="rgba(148,163,184,.10)", zerolinecolor="rgba(148,163,184,.15)")
    return fig


def safe_top(series, default="N/A"):
    clean = series.replace("", pd.NA).dropna()
    return clean.value_counts().index[0] if not clean.empty else default


def format_hour(hour):
    hour = int(hour)
    return f"{hour:02d}:00 – {(hour + 1) % 24:02d}:00"


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand-lockup">
            <div class="brand-mark">📡</div>
            <div>
                <div class="brand-name">SocialPulse</div>
                <div class="brand-tag">Trend Intelligence</div>
            </div>
        </div>
        <div class="sidebar-caption">
            Turn social conversations into trends, engagement signals and actionable insights.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-section">Data Source</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload social media data",
        type=["csv"],
        label_visibility="collapsed",
    )

    use_demo = st.toggle("Use bundled demo dataset", value=uploaded_file is None)

    st.markdown('<div class="sidebar-section">Explore & Filter</div>', unsafe_allow_html=True)


# ------------------------------------------------------------
# HERO
# ------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Shreya Verma · Analytics Lab</div>
        <div class="hero-title">See the signal.<br><span>Understand the conversation.</span></div>
        <div class="hero-copy">
            SocialPulse is an interactive intelligence workspace for exploring social activity,
            discovering emerging trends and understanding what drives engagement.
        </div>
        <div class="hero-chips">
            <div class="chip">🔥 Trend Discovery</div>
            <div class="chip">💬 Engagement Analytics</div>
            <div class="chip">😊 Sentiment Signals</div>
            <div class="chip">🔎 Interactive Exploration</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------
raw_bytes = None
source_name = None

if uploaded_file is not None:
    raw_bytes = uploaded_file.getvalue()
    source_name = uploaded_file.name
elif use_demo:
    demo_path = Path(__file__).with_name("social_media_posts.csv")
    if demo_path.exists():
        raw_bytes = demo_path.read_bytes()
        source_name = "social_media_posts.csv · bundled demo"

if raw_bytes is None:
    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-title">Your intelligence workspace is ready.</div>
            <div class="welcome-copy">
                Upload a CSV from the sidebar to analyze hashtags, users, engagement,
                posting behavior, categories and sentiment. If your repository includes
                <code>social_media_posts.csv</code>, enable the bundled demo dataset.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()

try:
    df = process_data(raw_bytes)
except Exception as exc:
    st.error(f"Unable to read this CSV: {exc}")
    st.stop()

if df.empty:
    st.warning("The selected dataset does not contain any rows.")
    st.stop()


# ------------------------------------------------------------
# SIDEBAR FILTERS
# ------------------------------------------------------------
with st.sidebar:
    users = sorted([u for u in df["User"].unique() if u])
    categories = sorted([c for c in df["Category"].unique() if c])
    sentiments = ["Positive", "Neutral", "Negative"]

    selected_users = st.multiselect("Users", users, default=users)
    selected_categories = st.multiselect("Categories", categories, default=categories)
    selected_sentiments = st.multiselect("Sentiment", sentiments, default=sentiments)

    valid_dates = df["Date"].dropna()
    if not valid_dates.empty:
        min_date, max_date = valid_dates.min().date(), valid_dates.max().date()
        date_range = st.date_input(
            "Date range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
        )
    else:
        date_range = None

    st.markdown("---")
    st.caption("Designed & built by Shreya Verma")
    st.caption("AI · ML · Data Analytics")


# ------------------------------------------------------------
# APPLY FILTERS
# ------------------------------------------------------------
filtered_df = df.copy()

if users and selected_users:
    filtered_df = filtered_df[filtered_df["User"].isin(selected_users)]
elif users and not selected_users:
    filtered_df = filtered_df.iloc[0:0]

if categories and selected_categories:
    filtered_df = filtered_df[filtered_df["Category"].isin(selected_categories)]
elif categories and not selected_categories:
    filtered_df = filtered_df.iloc[0:0]

if selected_sentiments:
    filtered_df = filtered_df[filtered_df["Sentiment"].isin(selected_sentiments)]
else:
    filtered_df = filtered_df.iloc[0:0]

if date_range and len(date_range) == 2:
    start_date = pd.Timestamp(date_range[0])
    end_date = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)
    filtered_df = filtered_df[
        filtered_df["Date"].isna()
        | ((filtered_df["Date"] >= start_date) & (filtered_df["Date"] <= end_date))
    ]

# Search
st.markdown('<div class="section-kicker">Live Exploration</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Search the conversation</div>', unsafe_allow_html=True)

search_query = st.text_input(
    "Search",
    placeholder="Search content, user, hashtag or category...",
    label_visibility="collapsed",
)

if search_query.strip():
    mask = pd.Series(False, index=filtered_df.index)
    for col in ["Content", "User", "Hashtags", "Category"]:
        mask |= filtered_df[col].str.contains(search_query, case=False, na=False, regex=False)
    filtered_df = filtered_df[mask]

if filtered_df.empty:
    st.warning("No posts match the current filters. Try broadening your selection.")
    st.stop()


# ------------------------------------------------------------
# SNAPSHOT
# ------------------------------------------------------------
hashtag_df = get_hashtag_data(filtered_df)
top_hashtag = hashtag_df.iloc[0]["Hashtag"] if not hashtag_df.empty else "N/A"
most_active_user = safe_top(filtered_df["User"])
most_popular_hour = int(filtered_df["Posting_Hour"].value_counts().index[0])

total_posts = len(filtered_df)
total_engagement = int(filtered_df["Total_Engagement"].sum())
avg_engagement = filtered_df["Total_Engagement"].mean()
engagement_per_post = round(avg_engagement, 1)

st.markdown('<div class="section-kicker">Intelligence Snapshot</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">What is happening right now?</div>', unsafe_allow_html=True)

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Posts", f"{total_posts:,}")
m2.metric("Total Engagement", f"{total_engagement:,}")
m3.metric("Avg. / Post", f"{engagement_per_post:,.1f}")
m4.metric("Top Trend", top_hashtag)
m5.metric("Most Active", most_active_user)


# ------------------------------------------------------------
# INSIGHTS
# ------------------------------------------------------------
positive_pct = filtered_df["Sentiment"].eq("Positive").mean() * 100
top_category = safe_top(filtered_df["Category"])
peak_window = format_hour(most_popular_hour)

st.markdown('<div class="section-kicker">At a Glance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Key signals from the data</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-icon">🕒</div>
            <div class="insight-label">Peak Posting Window</div>
            <div class="insight-value">{peak_window}</div>
            <div class="insight-sub">The most active publishing hour in the selected data.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-icon">😊</div>
            <div class="insight-label">Positive Conversation</div>
            <div class="insight-value">{positive_pct:.1f}%</div>
            <div class="insight-sub">Posts classified with a positive sentiment signal.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""
        <div class="insight-card">
            <div class="insight-icon">🏷️</div>
            <div class="insight-label">Leading Category</div>
            <div class="insight-value">{top_category}</div>
            <div class="insight-sub">The category with the highest conversation volume.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------
# DASHBOARD TABS
# ------------------------------------------------------------
st.markdown('<div class="section-kicker">Analytics Workspace</div>', unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(
    ["🔥 Trends", "💬 Engagement", "😊 Sentiment", "📋 Explorer & Export"]
)

with tab1:
    left, right = st.columns([1.05, 1])

    with left:
        st.markdown('<div class="section-title">Trending hashtags</div>', unsafe_allow_html=True)
        top_10 = hashtag_df.head(10).sort_values("Count", ascending=True)

        if top_10.empty:
            st.info("No hashtags were detected in the selected posts.")
        else:
            fig = px.bar(
                top_10,
                x="Count",
                y="Hashtag",
                orientation="h",
                text="Count",
                color="Count",
                color_continuous_scale="Viridis",
            )
            fig.update_coloraxes(showscale=False)
            chart_layout(fig, 420)
            st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown('<div class="section-title">Content category mix</div>', unsafe_allow_html=True)
        category_data = (
            filtered_df["Category"]
            .replace("", "Uncategorised")
            .value_counts()
            .rename_axis("Category")
            .reset_index(name="Posts")
        )
        fig = px.pie(
            category_data,
            names="Category",
            values="Posts",
            hole=.62,
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        chart_layout(fig, 420)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Most active voices</div>', unsafe_allow_html=True)
    active_users = (
        filtered_df["User"]
        .replace("", "Unknown")
        .value_counts()
        .head(10)
        .sort_values(ascending=True)
        .rename_axis("User")
        .reset_index(name="Posts")
    )
    fig = px.bar(
        active_users,
        x="Posts",
        y="User",
        orientation="h",
        text="Posts",
        color="Posts",
        color_continuous_scale="Teal",
    )
    fig.update_coloraxes(showscale=False)
    chart_layout(fig, 400)
    st.plotly_chart(fig, use_container_width=True)


with tab2:
    left, right = st.columns(2)

    with left:
        st.markdown('<div class="section-title">Daily engagement</div>', unsafe_allow_html=True)
        daily = (
            filtered_df.dropna(subset=["Date"])
            .groupby("Date", as_index=False)["Total_Engagement"]
            .sum()
            .sort_values("Date")
        )
        if daily.empty:
            st.info("No valid dates are available for a daily trend.")
        else:
            fig = px.area(
                daily,
                x="Date",
                y="Total_Engagement",
                markers=True,
            )
            chart_layout(fig, 410)
            st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown('<div class="section-title">Engagement composition</div>', unsafe_allow_html=True)
        breakdown = pd.DataFrame(
            {
                "Metric": ["Likes", "Comments", "Shares"],
                "Count": [
                    filtered_df["Likes"].sum(),
                    filtered_df["Comments"].sum(),
                    filtered_df["Shares"].sum(),
                ],
            }
        )
        fig = px.bar(
            breakdown,
            x="Metric",
            y="Count",
            text="Count",
            color="Metric",
        )
        chart_layout(fig, 410)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Posting time intelligence</div>', unsafe_allow_html=True)
    hourly = (
        filtered_df["Posting_Hour"]
        .value_counts()
        .reindex(range(24), fill_value=0)
        .rename_axis("Hour")
        .reset_index(name="Posts")
    )
    hourly["Label"] = hourly["Hour"].map(lambda x: f"{int(x):02d}:00")
    fig = px.bar(
        hourly,
        x="Label",
        y="Posts",
        color="Posts",
        color_continuous_scale="Bluered",
    )
    fig.update_coloraxes(showscale=False)
    chart_layout(fig, 390)
    st.plotly_chart(fig, use_container_width=True)


with tab3:
    left, right = st.columns([1, 1.1])

    with left:
        st.markdown('<div class="section-title">Conversation sentiment</div>', unsafe_allow_html=True)
        sentiment_data = (
            filtered_df["Sentiment"]
            .value_counts()
            .reindex(["Positive", "Neutral", "Negative"], fill_value=0)
            .rename_axis("Sentiment")
            .reset_index(name="Posts")
        )
        fig = px.bar(
            sentiment_data,
            x="Sentiment",
            y="Posts",
            text="Posts",
            color="Sentiment",
            color_discrete_map={
                "Positive": "#34D399",
                "Neutral": "#94A3B8",
                "Negative": "#FB7185",
            },
        )
        chart_layout(fig, 410)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown('<div class="section-title">Sentiment distribution</div>', unsafe_allow_html=True)
        fig = px.pie(
            sentiment_data,
            names="Sentiment",
            values="Posts",
            hole=.68,
            color="Sentiment",
            color_discrete_map={
                "Positive": "#34D399",
                "Neutral": "#94A3B8",
                "Negative": "#FB7185",
            },
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        chart_layout(fig, 410)
        st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Sentiment is generated with a lightweight rule-based NLP approach. "
        "It is useful for exploratory analysis, not as a replacement for a production-grade language model."
    )


with tab4:
    st.markdown('<div class="section-title">Explore individual posts</div>', unsafe_allow_html=True)

    display_columns = [
        col for col in [
            "Post_ID", "Date", "Time", "User", "Content", "Hashtags",
            "Category", "Likes", "Comments", "Shares",
            "Total_Engagement", "Sentiment",
        ]
        if col in filtered_df.columns
    ]

    explorer_df = filtered_df[display_columns].sort_values(
        "Total_Engagement", ascending=False
    )

    st.dataframe(explorer_df, use_container_width=True, height=460, hide_index=True)

    st.markdown('<div class="section-title">Export your analysis</div>', unsafe_allow_html=True)

    sentiment_counts = filtered_df["Sentiment"].value_counts()
    report = pd.DataFrame(
        {
            "Metric": [
                "Dataset Source",
                "Filtered Posts",
                "Total Likes",
                "Total Comments",
                "Total Shares",
                "Total Engagement",
                "Average Engagement per Post",
                "Top Trending Hashtag",
                "Most Active User",
                "Peak Posting Window",
                "Leading Content Category",
                "Positive Posts",
                "Neutral Posts",
                "Negative Posts",
            ],
            "Value": [
                source_name,
                len(filtered_df),
                int(filtered_df["Likes"].sum()),
                int(filtered_df["Comments"].sum()),
                int(filtered_df["Shares"].sum()),
                int(filtered_df["Total_Engagement"].sum()),
                round(float(filtered_df["Total_Engagement"].mean()), 2),
                top_hashtag,
                most_active_user,
                peak_window,
                top_category,
                int(sentiment_counts.get("Positive", 0)),
                int(sentiment_counts.get("Neutral", 0)),
                int(sentiment_counts.get("Negative", 0)),
            ],
        }
    )

    d1, d2 = st.columns(2)
    with d1:
        st.download_button(
            "📊 Download Intelligence Report",
            report.to_csv(index=False).encode("utf-8"),
            "socialpulse_intelligence_report.csv",
            "text/csv",
            use_container_width=True,
        )
    with d2:
        st.download_button(
            "📥 Download Filtered Posts",
            filtered_df.to_csv(index=False).encode("utf-8"),
            "socialpulse_filtered_posts.csv",
            "text/csv",
            use_container_width=True,
        )


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        <strong>SocialPulse</strong> · Social Media Intelligence
        <br><br>
        Designed & built by <strong>Shreya Verma</strong>
        <br>
        Python · Pandas · Plotly · Streamlit · NLP
    </div>
    """,
    unsafe_allow_html=True,
)
