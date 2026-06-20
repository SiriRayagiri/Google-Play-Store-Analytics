import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pytz

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Google Play Store Analytics",
    layout="wide"
)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose Dashboard",
    [
        "Home",
        "Task 1",
        "Task 2",
        "Task 3",
        "Task 4",
        "Task 5",
        "Task 6"
    ]
)

# =====================================
# LOAD DATA
# =====================================

apps_df = pd.read_csv("Play Store Data.csv")

# =====================================
# PREPROCESSING
# =====================================

apps_df["Reviews"] = pd.to_numeric(
    apps_df["Reviews"],
    errors="coerce"
)

apps_df["Rating"] = pd.to_numeric(
    apps_df["Rating"],
    errors="coerce"
)

apps_df["Installs"] = (
    apps_df["Installs"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("+", "", regex=False)
)

apps_df["Installs"] = pd.to_numeric(
    apps_df["Installs"],
    errors="coerce"
)

apps_df["Last Updated"] = pd.to_datetime(
    apps_df["Last Updated"],
    errors="coerce"
)

apps_df["Month"] = apps_df["Last Updated"].dt.month


def convert_size(size):
    try:
        size = str(size)

        if "M" in size:
            return float(size.replace("M", ""))

        elif "k" in size:
            return float(size.replace("k", "")) / 1024

        else:
            return None

    except:
        return None


apps_df["Size_MB"] = apps_df["Size"].apply(convert_size)

# =====================================
# IST TIME
# =====================================

ist = pytz.timezone("Asia/Kolkata")
current_hour = datetime.now(ist).hour

# =====================================
# HOME PAGE
# =====================================

if page == "Home":

    st.title("Google Play Store Analytics Dashboard")

    st.markdown("""
    ### Project Overview

    This dashboard analyzes Google Play Store applications using:

    - Ratings
    - Reviews
    - Installs
    - Revenue
    - Categories
    - User Sentiment

    Internship Tasks:
    - Task 1
    - Task 2
    - Task 3
    - Task 4
    - Task 5
    - Task 6
    """)

    st.write("Dataset Preview")

    st.dataframe(apps_df.head())

# =====================================
# TASK 1
# =====================================

elif page == "Task 1":

    st.title("Task 1 Dashboard")

    st.markdown("""
    ### Requirements

    - Top 10 categories by installs
    - Average Rating >= 4.0
    - Size > 10 MB
    - Last Updated Month = January
    - Compare Average Rating vs Total Reviews
    - Visible only between 3 PM and 5 PM IST
    """)

    if 15 <= current_hour < 17:

        task1_df = apps_df.copy()

        task1_df = task1_df[
            (task1_df["Rating"] >= 4.0)
            & (task1_df["Size_MB"] > 10)
            & (task1_df["Month"] == 1)
        ]

        top_categories = (
            task1_df.groupby("Category")["Installs"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .index
        )

        task1_df = task1_df[
            task1_df["Category"].isin(top_categories)
        ]

        task1_summary = (
            task1_df.groupby("Category")
            .agg(
                Average_Rating=("Rating", "mean"),
                Total_Reviews=("Reviews", "sum")
            )
            .reset_index()
        )

        fig, ax = plt.subplots(figsize=(12, 6))

        x = range(len(task1_summary))
        width = 0.4

        ax.bar(
            [i - width/2 for i in x],
            task1_summary["Average_Rating"],
            width,
            label="Average Rating"
        )

        ax.bar(
            [i + width/2 for i in x],
            task1_summary["Total_Reviews"],
            width,
            label="Total Reviews"
        )

        ax.set_xticks(list(x))
        ax.set_xticklabels(
            task1_summary["Category"],
            rotation=45
        )

        ax.set_title(
            "Average Rating vs Total Reviews"
        )

        ax.legend()

        st.pyplot(fig)

    else:

        st.info(
            "Task 1 chart available only between 3 PM and 5 PM IST"
        )

# =====================================
# TASK 2
# =====================================

elif page == "Task 2":

    st.title("Task 2 Dashboard")
    st.info("Task 2 not implemented yet")

# =====================================
# TASK 3
# =====================================

elif page == "Task 3":

    st.title("Task 3 Dashboard")
    st.info("Task 3 not implemented yet")

# =====================================
# TASK 4
# =====================================

elif page == "Task 4":

    st.title("Task 4 Dashboard")
    st.info("Task 4 not implemented yet")

# =====================================
# TASK 5
# =====================================

elif page == "Task 5":

    st.title("Task 5 Dashboard")
    st.info("Task 5 not implemented yet")

# =====================================
# TASK 6
# =====================================

elif page == "Task 6":

    st.title("Task 6 Dashboard")
    st.info("Task 6 not implemented yet")