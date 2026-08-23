import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Carbon Footprint Dashboard",
    page_icon="🌱",
    layout="wide"
)

# Title and description
st.title("🌱 Regional Carbon Footprint & Sustainability Tracker")
st.write("An interactive dashboard for analyzing carbon emissions across sectors.")

# Sidebar Controls
st.sidebar.header("Filter Options")
selected_year = st.sidebar.slider("Select Year", 2018, 2024, 2024)
sectors = ["Energy", "Transport", "Agriculture", "Industry"]
selected_sectors = st.sidebar.multiselect("Select Sectors", sectors, default=sectors)

# Generate synthetic dataset
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2018-01-01", end="2024-12-31", freq="ME")
    data = []
    for d in dates:
        for s in sectors:
            emissions = np.random.uniform(100, 500) + (d.year - 2018) * 15
            data.append({"Date": d, "Year": d.year, "Sector": s, "Emissions_Tons": emissions})
    return pd.DataFrame(data)

df = load_data()

# Filter data
filtered_df = df[(df["Year"] == selected_year) & (df["Sector"].isin(selected_sectors))]

# Metrics Section
col1, col2, col3 = st.columns(3)
total_emissions = filtered_df["Emissions_Tons"].sum()
avg_emissions = filtered_df["Emissions_Tons"].mean()

col1.metric("Total Emissions (Tons)", f"{total_emissions:,.2f}")
col2.metric("Average Monthly Sector Emission", f"{avg_emissions:,.2f}")
col3.metric("Selected Year", selected_year)

st.markdown("---")

# Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Emissions Distribution by Sector")
    if not filtered_df.empty:
        fig_pie = px.pie(filtered_df, values="Emissions_Tons", names="Sector", hole=0.4,
                         color_discrete_sequence=px.colors.sequential.Greens_r)
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("Select at least one sector in the sidebar.")

with col_right:
    st.subheader("Yearly Emissions Trend")
    trend_df = df[df["Sector"].isin(selected_sectors)].groupby(["Year", "Sector"])["Emissions_Tons"].sum().reset_index()
    fig_line = px.line(trend_df, x="Year", y="Emissions_Tons", color="Sector", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

# Data Table Display
st.subheader("Raw Data Sample")
st.dataframe(filtered_df.head(10), use_container_width=True)
