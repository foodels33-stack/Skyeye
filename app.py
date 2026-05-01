import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# הגדרות דף
st.set_page_config(page_title="SkyEye", layout="wide")

# עיצוב
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1, h3 { color: #22d3ee; text-align: right; }
    p { text-align: right; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔭 SkyEye")
st.subheader("מפת שידורים חיים מהחלל")

col1, col2 = st.columns([2, 1])

with col1:
    # יצירת מפה
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
    
    # רשימת מצפים עם קישורים יציבים (Direct Links)
    locations = [
        {
            "name": "תחנת החלל הבינלאומית (ISS)", 
            "lat": 0, "lon": 0, 
            "info": "שידור חי ישיר מנאס''א ביוטיוב - עובד תמיד!",
            "link": "https://www.youtube.com/embed/jPTD2gnZFUw"
        },
        {
            "name": "מצפה רמון - ישראל", 
            "lat": 30.597, "lon": 34.762, 
            "info": "האתר הרשמי של מצפה הכוכבים וייז.",
            "link": "https://wise-obs.tau.ac.il/"
        },
        {
            "name": "מצפה קק - הוואי", 
            "lat": 19.826, "lon": -155.474, 
            "info": "מצלמות בשידור חי מפסגת ההר.",
            "link": "https://www.keckobservatory.org/summit-webcams/"
        }
    ]
    
    for loc in locations:
        # יצירת חלונית עם קישור ברור
        html = f"""
        <div style='font-family: sans-serif; text-align: right; direction: rtl; color: black;'>
            <h4 style='margin:0;'>{loc['name']}</h4>
            <p style='font-size:12px;'>{loc['info']}</p>
            <a href='{loc['link']}' target='_blank' style='
                display: block;
                padding: 8px;
                background-color: #22d3ee;
                color: black;
                text-decoration: none;
                border-radius: 5px;
                text-align: center;
                font-weight: bold;'>לחצו כאן לצפייה 🚀</a>
        </div>
        """
        folium.Marker(
            [loc["lat"], loc["lon"]], 
            popup=folium.Popup(html, max_width=250),
            tooltip=loc["name"]
        ).add_to(m)
    
    st_folium(m, width=700, height=500)

with col2:
    st.write("### הרשמה למסע")
    name = st.text_input("שם")
    if st.button("שלח"):
        st.success(f"שלום {name}!")

# תמונת היום של נאס"א
st.write("---")
try:
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = res.json()
    st.image(data['url'], caption=data.get('title', ''), use_container_width=True)
except:
    st.write("מנסה להתחבר ללוויין...")
