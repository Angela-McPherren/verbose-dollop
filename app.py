
import streamlit as st
import pandas as pd

# Load data from Excel file
df = pd.read_excel("RSG_CONFIGURATOR_CLEANED.xlsx")

# Title
st.title("CNG Configurator App")

# Sidebar filters
st.sidebar.header("Filter Options")
application = st.sidebar.selectbox("Application", df['Application'].dropna().unique())
body_mfg = st.sidebar.selectbox("Body Manufacturer", df['Body Manufacturer'].dropna().unique())
chassis_type = st.sidebar.selectbox("Chassis Type", df['Chassis Type'].dropna().unique())
system_type = st.sidebar.selectbox("System Type", df['System Type'].dropna().unique())

# Filter dataset
filtered_df = df[
    (df['Application'] == application) &
    (df['Body Manufacturer'] == body_mfg) &
    (df['Chassis Type'] == chassis_type) &
    (df['System Type'] == system_type)
]

# Display results
st.subheader("Filtered Configuration")
if filtered_df.empty:
    st.warning("No data found for selected filters.")
else:
    st.dataframe(filtered_df[[
        'Body Model', 'Chassis Manufacturer', 'Chassis Model', 'Chassis Cab',
        'CNG Mounting Inputs', 'System DGE',
        'Part Number 1', 'Part Number 2', 'Part Number 3',
        'Part Number 4', 'Part Number 5', 'Part Number 6',
        'System Cost', 'FET', 'Install', 'Kits Needed 1', 'Kits Needed 2', 'Kits Needed 3', 'Total'
    ]])
