import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static

def main():
    st.title("Soil Status Map")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read data from uploaded CSV file
        data = pd.read_csv(uploaded_file)

        # Check if the required columns are present
        if 'Latitute' in data.columns and 'Longititude' in data.columns and 'Code' in data.columns:
            # Create a base map
            m = folium.Map(location=[data['Latitute'].mean(), data['Longititude'].mean()], zoom_start=10)

            # Add markers to the map based on the data
            for index, row in data.iterrows():
                folium.Marker(
                    location=[row['Latitute'], row['Longititude']],
                    popup=f"Code: {row['Code']}",
                    icon=folium.Icon(color='red' if row['Code'] == 1 else 'blue' if row['Code'] == 2 else 'green')
                ).add_to(m)

            # Display the map using folium_static
            folium_static(m)
        else:
            st.warning("The uploaded CSV file does not contain the required columns: 'Latitute', 'Longititude', 'Code'.")

if __name__ == "__main__":
    main()
