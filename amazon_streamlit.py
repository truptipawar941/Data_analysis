import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Amazon Dashboard", layout="wide")

st.title("🛒 Amazon Sales Dashboard (Mini Project)")

# ---------------- DATA ----------------
data = {
    "Product": ["Phone", "Laptop", "Headphones", "Watch", "Tablet", "Camera", "TV"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Electronics"],
    "Price": [20000, 60000, 2000, 5000, 30000, 40000, 55000],
    "Rating": [4.2, 4.5, 4.0, 3.8, 4.1, 4.3, 4.4],
    "Sales": [150, 80, 300, 120, 90, 60, 70]
}

df = pd.DataFrame(data)

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("Filter Data")
category = st.sidebar.selectbox("Select Category", ["All"] + list(df["Category"].unique()))

if category != "All":
    df = df[df["Category"] == category]

# ---------------- METRICS ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Avg Price", round(df["Price"].mean(), 2))
col2.metric("⭐ Avg Rating", round(df["Rating"].mean(), 2))
col3.metric("🏆 Top Sales Product", df.loc[df["Sales"].idxmax(), "Product"])

# ---------------- DATA TABLE ----------------
st.subheader("📦 Product Data")
st.dataframe(df)

# ---------------- CHART 1: SALES ----------------
st.subheader("📈 Sales by Product")
fig1, ax1 = plt.subplots()
sns.barplot(x=df["Product"], y=df["Sales"], ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# ---------------- CHART 2: PRICE ----------------
st.subheader("💰 Price Comparison")
fig2, ax2 = plt.subplots()
sns.barplot(x=df["Product"], y=df["Price"], ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---------------- CHART 3: RATING ----------------
st.subheader("⭐ Product Ratings")
fig3, ax3 = plt.subplots()
sns.barplot(x=df["Product"], y=df["Rating"], ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# ---------------- PIE CHART ----------------
st.subheader("📊 Sales Distribution")
fig4, ax4 = plt.subplots()
df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%", ax=ax4)
ax4.set_ylabel("")
st.pyplot(fig4)