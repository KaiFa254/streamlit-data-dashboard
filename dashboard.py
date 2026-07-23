"""
Bank Loan Portfolio Dashboard - Streamlit Sample App
Run with: streamlit run dashboard.py

This uses the same data and calculations walked through step by step in
bank_dashboard_training.ipynb - open that notebook first if you want the
commented, cell-by-cell explanation of how each piece works.
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------------------------------------------
# 1. PAGE CONFIG (must be the first Streamlit command)
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Bank Loan Portfolio Dashboard",
    page_icon="🏦",
    layout="wide",
)

# ----------------------------------------------------------------------
# 2. LOAD DATA
# ----------------------------------------------------------------------
# @st.cache_data means the CSV is only read from disk once, not on every
# click/filter change - this is what keeps dashboards fast.
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/bank_loan_portfolio.csv", parse_dates=["Disbursement_Date"]
    )
    return df

df = load_data()

# ----------------------------------------------------------------------
# 3. SIDEBAR FILTERS
# ----------------------------------------------------------------------
st.sidebar.header("Filters")

branch_filter = st.sidebar.multiselect(
    "Branch",
    options=sorted(df["Branch"].unique()),
    default=sorted(df["Branch"].unique()),
)

product_filter = st.sidebar.multiselect(
    "Product",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique()),
)

segment_filter = st.sidebar.multiselect(
    "Customer Segment",
    options=sorted(df["Customer_Segment"].unique()),
    default=sorted(df["Customer_Segment"].unique()),
)

# Apply filters to the dataframe
filtered_df = df[
    df["Branch"].isin(branch_filter)
    & df["Product"].isin(product_filter)
    & df["Customer_Segment"].isin(segment_filter)
]

# ----------------------------------------------------------------------
# 4. TITLE
# ----------------------------------------------------------------------
st.title("🏦 Bank Loan Portfolio Dashboard")
st.caption("Sample dashboard — synthetic training data, not real customer data")

# ----------------------------------------------------------------------
# 5. KPI METRICS (top row)
# ----------------------------------------------------------------------
total_book = filtered_df["Outstanding_Balance"].sum()
num_loans = len(filtered_df)
default_rate = (
    (filtered_df["DPD"] > 30).sum() / len(filtered_df) if len(filtered_df) > 0 else 0
)
npl_balance = filtered_df.loc[
    filtered_df["IFRS9_Stage"] == "Stage 3 - Non-Performing", "Outstanding_Balance"
].sum()
npl_ratio = npl_balance / total_book if total_book > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Loan Book", f"KES {total_book:,.0f}")
col2.metric("Number of Loans", f"{num_loans:,}")
col3.metric("Default Rate (>30 DPD)", f"{default_rate:.1%}")
col4.metric("NPL Ratio", f"{npl_ratio:.1%}")

st.divider()

# ----------------------------------------------------------------------
# 6. CHARTS (side by side)
# ----------------------------------------------------------------------
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Outstanding Balance by Product")
    product_summary = (
        filtered_df.groupby("Product")["Outstanding_Balance"].sum().reset_index()
    )
    fig1 = px.bar(
        product_summary,
        x="Product",
        y="Outstanding_Balance",
        color="Product",
        text_auto=".2s",
    )
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with chart_col2:
    st.subheader("Portfolio Mix by IFRS9 Stage")
    stage_summary = (
        filtered_df.groupby("IFRS9_Stage")["Outstanding_Balance"].sum().reset_index()
    )
    fig2 = px.pie(
        stage_summary,
        names="IFRS9_Stage",
        values="Outstanding_Balance",
        hole=0.4,
        color="IFRS9_Stage",
        color_discrete_map={
            "Stage 1 - Performing": "#2E7D32",
            "Stage 2 - Underperforming": "#F9A825",
            "Stage 3 - Non-Performing": "#C62828",
        },
    )
    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------------------------------------------
# 7. TREND OVER TIME
# ----------------------------------------------------------------------
st.subheader("Monthly Disbursement Trend")
trend = (
    filtered_df.set_index("Disbursement_Date")
    .resample("ME")["Disbursed_Amount"]
    .sum()
    .reset_index()
)
fig3 = px.line(trend, x="Disbursement_Date", y="Disbursed_Amount", markers=True)
st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------------------------------------------
# 8. BRANCH PERFORMANCE TABLE
# ----------------------------------------------------------------------
st.subheader("Branch Performance Summary")
branch_perf = (
    filtered_df.groupby("Branch")
    .agg(
        Number_of_Loans=("Customer_ID", "count"),
        Outstanding_Balance=("Outstanding_Balance", "sum"),
        Avg_DPD=("DPD", "mean"),
    )
    .reset_index()
    .sort_values("Outstanding_Balance", ascending=False)
)
st.dataframe(branch_perf, use_container_width=True, hide_index=True)

# ----------------------------------------------------------------------
# 9. LOAN-LEVEL DETAIL TABLE
# ----------------------------------------------------------------------
st.subheader("Loan-Level Detail")
st.dataframe(
    filtered_df.sort_values("Outstanding_Balance", ascending=False),
    use_container_width=True,
    hide_index=True,
)

# ----------------------------------------------------------------------
# 10. DOWNLOAD BUTTON
# ----------------------------------------------------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_loans.csv",
    mime="text/csv",
)
