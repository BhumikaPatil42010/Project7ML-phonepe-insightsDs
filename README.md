1. Project Title
# 📊 PhonePe Transaction Insights Dashboard

## 📌 Overview

This project analyzes PhonePe transaction data to extract meaningful insights about user behavior, transaction trends, and geographical distribution. The project includes data extraction, SQL analysis, Python visualization, and an interactive Streamlit dashboard.

## 🎯 Objectives

- Analyze digital transaction patterns
- Identify top-performing states and districts
- Understand user engagement trends
- Provide actionable business insights

## 🛠️ Tech Stack

- Python (Pandas, Matplotlib, Seaborn)
- SQL (MySQL)
- Streamlit (Dashboard)
- Git & GitHub (Version Control)

## 📁 Project Structure

phonepe-insights/
│
├── data/
│   ├── raw/
│   └── processed/
├── sql/
├── notebooks/
├── app/
├── images/
├── README.md
└── requirements.txt

## 📂 Data Source

Dataset is taken from the official PhonePe Pulse GitHub repository, containing transaction, user, and insurance data in JSON format.

## 🔄 ETL Process

1. Extracted JSON data from dataset
2. Transformed data into structured format using Python
3. Loaded processed data into MySQL database

## 🗄️ Database Design

Tables used:
- aggregated_transaction
- aggregated_user
- map_transaction
- top_transaction

## 📊 Data Analysis

SQL queries were used to analyze:
- Top states by transactions
- Year-wise growth trends
- Payment type distribution
- District-level performance

## 📈 Visualizations

### Top States
![Top States](images/top_states.png)

### Yearly Trend
![Yearly Trend](images/yearly_trend.png)

## 📊 Streamlit Dashboard

An interactive dashboard was created using Streamlit to visualize insights dynamically with filters and charts.

## 💡 Key Insights

- Maharashtra and Karnataka dominate transaction volume
- UPI is the most used payment method
- Strong growth observed after 2020
- Urban areas show higher engagement
- Opportunity exists in rural regions


## 💼 Business Use Cases

- Customer segmentation
- Fraud detection
- Targeted marketing strategies
- Product development insights


## ⚠️ Challenges Faced

- Handling nested JSON data
- Fixing incorrect file paths
- Data cleaning and type conversion
- Debugging empty datasets


## ✅ Conclusion

The project demonstrates how data analytics can be used to extract valuable insights from digital payment systems. The dashboard enables better decision-making and highlights opportunities for growth.

## 🚀 Future Scope

- Add real-time data integration
- Build advanced predictive models
- Enhance dashboard UI with maps and filters

## Author
Bhumika Patil
