import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="SkyEye - צופים ביקום", layout="wide")

st.markdown("""<style>.main { background-color: #0e1117; color: white; } h1 { color: #22d3ee; }</style>""", unsafe_allow_html=True)

st.title("🔭 SkyEye")
st.subheader("גלו איפה נמצאים הטלסקופים הגדולים בעולם")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### מפת הטלסקופים העולמית")
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
    
    locations = [
        {"name": "מצפה רמון - ישראל", "lat": 30.597, "lon": 34.762, "info": "המצפה הגדול בישראל!"},
        {"name": "VLT - צ'ילה", "lat": -24.627, "lon": -70.404, "info": "במדבר אטקמה."},
        {"name": "מצפה קק - הוואי", "lat": 19.826, "lon": -155.474, "info": "בגובה 4,200 מטר."}
    ]
    
    for loc in locations:
        folium.Marker(
            [loc["lat"], loc["lon"]], 
            popup=f"<b>{loc['name']}</b><br>{loc['info']}",
            tooltip=loc["name"]
        ).add_to(m)
    
    st_folium(m, width=700, height=450)

with col2:
    st.write("### הצטרפו למסע")
    name = st.text_input("שם הילד/ה")
    email = st.text_input("אימייל")
    if st.button("רישום"):
        st.success(f"ברוך הבא, {name}!")

st.write("---")
st.header("📸 תמונת היום מנאס''א")
try:
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = res.json()
    st.image(data['url'], use_container_width=True)
    st.write(f"**{data['title']}**")
except:
    st.write("טוען נתונים...")
