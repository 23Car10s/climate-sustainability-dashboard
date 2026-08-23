# Regional Carbon Footprint & Sustainability Tracker

## Project Overview
This Streamlit application provides an interactive analytics interface for monitoring carbon emissions across key industrial and societal sectors (Energy, Transport, Agriculture, Industry). The tool allows sustainability managers to track emission trends over time and evaluate sector contributions to regional footprints.

## Business Case & Assessment
- **Problem Statement:** Environmental officers lack accessible, real-time visual tools to identify high-emission sectors quickly.
- **Value Delivered:** Enables data-driven policy decisions by allowing non-technical users to filter trends dynamically by year and sector.
- **Dataset Information:** The dataset uses synthetic monthly emissions records (2018–2024) generated using Python standard distribution models to ensure privacy compliance and public accessibility.

## User Interface & UX Design
- **Information Hierarchy:** High-level key metric indicators (KPIs) are displayed prominently at the top, followed by interactive Plotly charts, ending with raw tabular data.
- **Navigation:** All controls (Year sliders and Sector checkboxes) are located in the left sidebar for clean visual flow.

## Setup & Installation
1. Install requirements:
   ```bash
   pip install streamlit pandas numpy plotly