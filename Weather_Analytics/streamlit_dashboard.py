# Fixed Weather Intelligence Dashboard
# Replace your current dashboard file with this version.
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Weather Intelligence Dashboard", page_icon="🌦️", layout="wide", initial_sidebar_state="expanded")

PRIMARY="#38bdf8"; SECONDARY="#60a5fa"; ACCENT="#2dd4bf"; DANGER="#fb7185"
APP_BG="#0b1220"; SURFACE="#111827"; CARD_BG="#162235"; TEXT="#e5eef8"; MUTED="#94a3b8"; BORDER="#26364d"
SUNNY="#fbbf24"; RAINY="#38bdf8"; CLOUDY="#a5b4c8"

st.markdown("""
<style>
.stApp{background:radial-gradient(circle at top right,rgba(56,189,248,.08),transparent 30%),linear-gradient(180deg,#0b1220 0%,#0d1626 100%);color:#e5eef8}
[data-testid="stHeader"]{background:rgba(11,18,32,.92)}
.block-container{max-width:1500px;padding-top:2rem;padding-bottom:2rem}
.hero-box{background:linear-gradient(135deg,#172554 0%,#0f3f68 52%,#115e59 100%);border:1px solid rgba(125,211,252,.22);border-radius:22px;padding:2.2rem 2.5rem;margin-bottom:1.8rem;box-shadow:0 18px 45px rgba(0,0,0,.28)}
.hero-title{color:#f8fafc!important;font-size:2.45rem;font-weight:800;letter-spacing:-.7px;line-height:1.15;margin-bottom:.55rem}
.hero-subtitle{color:#cbd5e1!important;font-size:1.05rem;line-height:1.6}
.section-title{color:#f1f5f9!important;font-size:1.35rem;font-weight:750;margin:.5rem 0 1rem}
div[data-testid="stMetric"]{background:linear-gradient(145deg,#162235,#131e30);border:1px solid #26364d;border-radius:16px;padding:1rem 1.15rem;min-height:125px;box-shadow:0 8px 20px rgba(0,0,0,.16)}
div[data-testid="stMetricLabel"]{color:#9fb0c7!important;font-weight:600}
div[data-testid="stMetricValue"]{color:#f8fafc!important;font-weight:750}
section[data-testid="stSidebar"],section[data-testid="stSidebar"]>div{background:#0e1726}
section[data-testid="stSidebar"]{border-right:1px solid #26364d}
section[data-testid="stSidebar"] *{color:#dbeafe}
section[data-testid="stSidebar"] .stCaption{color:#94a3b8!important}
div[data-baseweb="select"]>div,div[data-baseweb="input"]>div{background:#111827!important;border-color:#334155!important;color:#e5eef8!important}
div[data-baseweb="select"] span,div[data-baseweb="input"] input{color:#e5eef8!important}
[data-baseweb="tag"]{background:#1d4ed8!important;color:#fff!important}[data-baseweb="tag"] span{color:#fff!important}
.stButton>button{background:linear-gradient(135deg,#0284c7,#2563eb);color:#fff!important;border:1px solid #38bdf8;border-radius:10px;font-weight:650}
.stDownloadButton>button{background:#162235;color:#e0f2fe!important;border:1px solid #334e68;border-radius:10px;font-weight:650}
.stDownloadButton>button:hover{background:#1b2a40;border-color:#38bdf8;color:#fff!important}
button[data-baseweb="tab"]{color:#94a3b8!important;font-weight:650}button[data-baseweb="tab"][aria-selected="true"]{color:#7dd3fc!important}
div[data-testid="stDataFrame"]{border:1px solid #26364d;border-radius:14px;overflow:hidden}
div[data-testid="stAlert"]{background:#162235;border:1px solid #334155;color:#dbeafe;border-radius:14px}
hr{border-color:#26364d!important}.footer{text-align:center;padding:1.7rem 1rem .5rem;color:#94a3b8;font-size:.92rem}.footer b{color:#e0f2fe}
</style>
""", unsafe_allow_html=True)

def chart_theme(fig,height=450):
    fig.update_layout(template="plotly_dark",height=height,paper_bgcolor=SURFACE,plot_bgcolor=SURFACE,font=dict(color=TEXT),title=dict(font=dict(size=18,color="#f1f5f9")),legend=dict(bgcolor="rgba(0,0,0,0)",font=dict(color="#cbd5e1")),margin=dict(l=30,r=30,t=65,b=35),hoverlabel=dict(bgcolor="#1e293b",font_color="#f8fafc",bordercolor=PRIMARY))
    fig.update_xaxes(showgrid=True,gridcolor=BORDER,linecolor="#334155",tickfont=dict(color="#b8c5d6"),title_font=dict(color="#dbeafe"))
    fig.update_yaxes(showgrid=True,gridcolor=BORDER,linecolor="#334155",tickfont=dict(color="#b8c5d6"),title_font=dict(color="#dbeafe"))
    return fig

@st.cache_data
def load_data():
    data_path = Path(__file__).resolve().parent / "weather_data.csv"
    df = pd.read_csv(data_path).drop_duplicates()
    df["Date"]=pd.to_datetime(df["Date"],errors="coerce"); df=df.dropna(subset=["Date"])
    df["Temperature"]=pd.to_numeric(df["Temperature"],errors="coerce")
    df["Humidity"]=pd.to_numeric(df["Humidity"],errors="coerce")
    df["Temperature"]=df["Temperature"].fillna(df["Temperature"].median())
    df["Humidity"]=df["Humidity"].fillna(df["Humidity"].median())
    df["City"]=df["City"].fillna("Unknown").astype(str).str.strip()
    df["Weather"]=df["Weather"].fillna(df["Weather"].mode()[0] if not df["Weather"].dropna().empty else "Unknown").astype(str).str.strip().str.title()
    return df.sort_values("Date")

df=load_data()

with st.sidebar:
    st.title("🌦️ Dashboard Controls"); st.caption("Customize the analytics using the filters below."); st.divider()
    cities=sorted(df["City"].unique()); weather_types=sorted(df["Weather"].unique())
    selected_cities=st.multiselect("🏙️ Select Cities",cities,default=cities)
    selected_weather=st.multiselect("🌤️ Select Weather Type",weather_types,default=weather_types)
    min_date,max_date=df["Date"].min().date(),df["Date"].max().date()
    selected_dates=st.date_input("📅 Select Date Range",value=(min_date,max_date),min_value=min_date,max_value=max_date)
    st.divider(); st.markdown("### 📊 Dataset Summary")
    st.write(f"**Total Records:** {len(df):,}"); st.write(f"**Cities Available:** {df['City'].nunique()}"); st.write(f"**Weather Types:** {df['Weather'].nunique()}")
    st.divider()
    if st.button("🔄 Reset Filters"): st.rerun()

filtered_df=df[df["City"].isin(selected_cities)&df["Weather"].isin(selected_weather)].copy()
if len(selected_dates)==2:
    start_date,end_date=selected_dates
    filtered_df=filtered_df[(filtered_df["Date"].dt.date>=start_date)&(filtered_df["Date"].dt.date<=end_date)]
if filtered_df.empty:
    st.warning("⚠️ No weather data is available for the selected filters."); st.stop()

avg_temp=filtered_df["Temperature"].mean(); avg_humidity=filtered_df["Humidity"].mean()
city_average=filtered_df.groupby("City")["Temperature"].mean().sort_values(ascending=False)
daily_temperature=filtered_df.groupby("Date")["Temperature"].mean().sort_index()
weather_counts=filtered_df["Weather"].value_counts()
hottest_city,hottest_temp=city_average.idxmax(),city_average.max()
coldest_city,coldest_temp=city_average.idxmin(),city_average.min()
rainy_count=filtered_df["Weather"].str.lower().eq("rainy").sum()
sunny_count=filtered_df["Weather"].str.lower().eq("sunny").sum()

# Single-line HTML avoids the literal-tag header issue.
st.markdown('<div class="hero-box"><div class="hero-title">🌦️ Weather Intelligence Dashboard</div><div class="hero-subtitle">Interactive weather analytics, city comparisons, temperature trends and forecasting</div></div>',unsafe_allow_html=True)

st.markdown('<div class="section-title">📊 Weather Overview</div>',unsafe_allow_html=True)
r1=st.columns(4)
r1[0].metric("📋 Records Analyzed",f"{len(filtered_df):,}")
r1[1].metric("🌡️ Average Temperature",f"{avg_temp:.1f} °C")
r1[2].metric("💧 Average Humidity",f"{avg_humidity:.1f}%")
r1[3].metric("🏙️ Cities Analyzed",filtered_df["City"].nunique())
st.write("")
r2=st.columns(4)
r2[0].metric("🔥 Hottest City",hottest_city,f"{hottest_temp:.1f} °C")
r2[1].metric("❄️ Coldest City",coldest_city,f"{coldest_temp:.1f} °C")
r2[2].metric("🌧️ Rainy Days",rainy_count)
r2[3].metric("☀️ Sunny Days",sunny_count)
st.divider()

tab1,tab2,tab3,tab4,tab5=st.tabs(["📊 Overview","🌡️ Temperature Analysis","🌦️ Weather Analysis","🏙️ City Insights","🔮 Forecast & Data"])

with tab1:
    c1,c2=st.columns(2)
    with c1:
        fig=px.line(x=daily_temperature.index,y=daily_temperature.values,markers=True,labels={"x":"Date","y":"Average Temperature (°C)"},title="🌡️ Average Temperature Trend")
        fig.update_traces(line=dict(color=PRIMARY,width=3),marker=dict(size=7,color=ACCENT))
        st.plotly_chart(chart_theme(fig,430),use_container_width=True)
    with c2:
        color_map={"Sunny":SUNNY,"Rainy":RAINY,"Cloudy":CLOUDY}
        fig=go.Figure(data=[go.Pie(labels=weather_counts.index,values=weather_counts.values,hole=.55,marker=dict(colors=[color_map.get(x,ACCENT) for x in weather_counts.index]),textinfo="percent+label",textfont=dict(color=TEXT))])
        fig.update_layout(title="🌦️ Weather Condition Distribution")
        st.plotly_chart(chart_theme(fig,430),use_container_width=True)
    st.markdown('<div class="section-title">💡 Quick Insights</div>',unsafe_allow_html=True)
    i1,i2,i3=st.columns(3)
    i1.info(f"🔥 **Warmest City**\n\n**{hottest_city}** has the highest average temperature of **{hottest_temp:.2f} °C**.")
    i2.info(f"❄️ **Coolest City**\n\n**{coldest_city}** has the lowest average temperature of **{coldest_temp:.2f} °C**.")
    i3.info(f"🌤️ **Most Common Weather**\n\n**{weather_counts.idxmax()}** appears **{weather_counts.max()} times** in the selected data.")

with tab2:
    st.markdown('<div class="section-title">🌡️ Temperature Analysis</div>',unsafe_allow_html=True)
    city_chart=city_average.reset_index(); city_chart.columns=["City","Average Temperature"]
    fig=px.bar(city_chart,x="City",y="Average Temperature",text_auto=".2f",title="Average Temperature Comparison by City",color_discrete_sequence=[PRIMARY])
    fig.update_layout(xaxis_title="City",yaxis_title="Average Temperature (°C)")
    st.plotly_chart(chart_theme(fig,500),use_container_width=True)
    summary=filtered_df.groupby("Date").agg(Minimum=("Temperature","min"),Average=("Temperature","mean"),Maximum=("Temperature","max")).reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=summary["Date"],y=summary["Maximum"],mode="lines+markers",name="Maximum Temperature",line=dict(color="#fb7185")))
    fig.add_trace(go.Scatter(x=summary["Date"],y=summary["Average"],mode="lines+markers",name="Average Temperature",line=dict(color=PRIMARY,width=3)))
    fig.add_trace(go.Scatter(x=summary["Date"],y=summary["Minimum"],mode="lines+markers",name="Minimum Temperature",line=dict(color=ACCENT)))
    fig.update_layout(title="Daily Temperature Range",xaxis_title="Date",yaxis_title="Temperature (°C)")
    st.plotly_chart(chart_theme(fig,500),use_container_width=True)

with tab3:
    st.markdown('<div class="section-title">🌦️ Weather Condition Analysis</div>',unsafe_allow_html=True)
    weather_df=weather_counts.reset_index(); weather_df.columns=["Weather","Count"]
    color_map={"Sunny":SUNNY,"Rainy":RAINY,"Cloudy":CLOUDY}
    c1,c2=st.columns(2)
    with c1:
        fig=px.bar(weather_df,x="Weather",y="Count",text="Count",title="Weather Condition Counts",color="Weather",color_discrete_map=color_map); fig.update_layout(showlegend=False)
        st.plotly_chart(chart_theme(fig,450),use_container_width=True)
    with c2:
        fig=px.pie(weather_df,values="Count",names="Weather",hole=.48,title="Weather Distribution",color="Weather",color_discrete_map=color_map)
        st.plotly_chart(chart_theme(fig,450),use_container_width=True)
    st.dataframe(weather_df,use_container_width=True,hide_index=True)

with tab4:
    st.markdown('<div class="section-title">🏙️ City-wise Insights</div>',unsafe_allow_html=True)
    city_summary=filtered_df.groupby("City").agg(Average_Temperature=("Temperature","mean"),Maximum_Temperature=("Temperature","max"),Minimum_Temperature=("Temperature","min"),Average_Humidity=("Humidity","mean"),Weather_Records=("Weather","count")).round(2).sort_values("Average_Temperature",ascending=False).reset_index()
    st.dataframe(city_summary,use_container_width=True,hide_index=True)
    fig=px.scatter(city_summary,x="Average_Humidity",y="Average_Temperature",size="Weather_Records",hover_name="City",title="Temperature vs Humidity by City",color_discrete_sequence=[SECONDARY])
    fig.update_layout(xaxis_title="Average Humidity (%)",yaxis_title="Average Temperature (°C)")
    st.plotly_chart(chart_theme(fig,500),use_container_width=True)

with tab5:
    st.markdown('<div class="section-title">🔮 Tomorrow Temperature Forecast</div>',unsafe_allow_html=True)
    if len(daily_temperature)>=7:
        rolling=daily_temperature.rolling(7).mean(); prediction=daily_temperature.tail(7).mean()
        c1,c2=st.columns([1,2])
        with c1:
            st.metric("🔮 Predicted Tomorrow's Temperature",f"{prediction:.2f} °C")
            st.info("This prediction is based on the average temperature from the most recent 7 days.")
        with c2:
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=daily_temperature.index,y=daily_temperature.values,mode="lines+markers",name="Actual Temperature",line=dict(color=PRIMARY,width=3)))
            fig.add_trace(go.Scatter(x=rolling.index,y=rolling.values,mode="lines",name="7-Day Moving Average",line=dict(color=ACCENT,width=3,dash="dash")))
            fig.add_hline(y=prediction,line_dash="dot",line_color=DANGER,annotation_text=f"Prediction: {prediction:.2f} °C",annotation_font_color=TEXT)
            fig.update_layout(title="Temperature Trend and Moving Average Forecast",xaxis_title="Date",yaxis_title="Temperature (°C)")
            st.plotly_chart(chart_theme(fig,450),use_container_width=True)
    else:
        st.warning("Not enough records are available for a 7-day moving average forecast.")
    st.divider()
    st.markdown('<div class="section-title">📋 Filtered Weather Data</div>',unsafe_allow_html=True)
    st.dataframe(filtered_df,use_container_width=True,hide_index=True)
    st.divider()
    st.markdown('<div class="section-title">📥 Download Your Analysis</div>',unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        st.download_button("📥 Download Filtered Weather Data",filtered_df.to_csv(index=False).encode("utf-8"),"filtered_weather_report.csv","text/csv")
    with c2:
        st.download_button("📊 Download City Analysis Report",city_summary.to_csv(index=False).encode("utf-8"),"city_weather_analysis.csv","text/csv")

st.markdown('<div class="footer">🌦️ <b>Weather Intelligence Dashboard</b><br>Built with Python, Pandas, Plotly and Streamlit</div>',unsafe_allow_html=True)
