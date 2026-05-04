import streamlit as st
import pandas as pd
import mysql.connector

# Page config
st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

# Title
st.title("📊 PhonePe Transaction Insights Dashboard")

# DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nishu123",
    database="phonepe"
)

# Load data
df = pd.read_sql("SELECT * FROM aggregated_transaction", conn)
df_user = pd.read_sql("SELECT * FROM aggregated_user", conn)
df_map = pd.read_sql("SELECT * FROM map_transaction", conn)

# Fix datatype
df_map["amount"] = pd.to_numeric(df_map["amount"], errors="coerce")
df_map = df_map.dropna(subset=["amount"])

# -------------------------------
# 🎛️ SIDEBAR FILTER
# -------------------------------
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))

filtered_df = df[df["year"] == year]

# -------------------------------
# 📊 KPI METRICS
# -------------------------------
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Transaction", int(filtered_df["amount"].sum()))
col2.metric("Total Users", int(df_user["registeredUsers"].sum()))
col3.metric("App Opens", int(df_user["appOpens"].sum()))

# -------------------------------
# 📊 TOP STATES
# -------------------------------
st.subheader(f"Top States in {year}")

top_states = filtered_df.groupby("state")["amount"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_states)

# -------------------------------
# 📈 YEARLY TREND
# -------------------------------
st.subheader("Yearly Transaction Trend")

yearly = df.groupby("year")["amount"].sum()
st.line_chart(yearly)

# -------------------------------
# 📍 DISTRICT ANALYSIS
# -------------------------------
st.subheader("Top Districts")

if not df_map.empty:
    top_districts = df_map.groupby("district")["amount"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_districts)
else:
    st.warning("No district data available")

# -------------------------------
# 👥 USER ANALYSIS
# -------------------------------
st.subheader("Top States by Users")

top_users = df_user.groupby("state")["registeredUsers"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_users)

# -------------------------------
# 💡 INSIGHTS
# -------------------------------
st.subheader("Insights")

st.write("""
- Top states contribute majority of transactions  
- Digital payments show strong growth trend  
- High user engagement in metro states  
- Maharashtra leads transaction volume, indicating strong digital adoption and higher economic activity
- TRANSACTION INSIGHTS

Insight 1: Top Performing States
        States like Maharashtra, Karnataka, and Telangana dominate transaction volume
        Indicates higher digital payment adoption in urbanized regions
        
Insight 2: Payment Type Analysis
        UPI contributes the largest share of transactions
        Shows shift towards fast, low-cost digital payments
        
Insight 3: Growth Trend
        Significant increase in transactions after 2020
        Likely due to:
        Pandemic-driven digital adoption
        Government push for cashless economy
        
Insight 4: Quarterly Patterns
        Some quarters show spikes → possible seasonal trends
        Useful for:
        Marketing campaigns
        Resource allocation
""")