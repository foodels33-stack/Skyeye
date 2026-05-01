import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# הגדרות דף
st.set_page_config(page_title="SkyEye - צופים ביקום", layout="wide")

# עיצוב דף
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1, h2, h3 { color: #22d3ee; text-align: right; }
    p { text-align: right; }
    .stButton > button { width: 100%; background-color: #22d3ee; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔭 SkyEye")
st.subheader("שידורים חיים מהחלל ומהמצפים הגדולים")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### מפת שידורי חלל פעילים")
    
    # יצירת המפה
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
    
    # רשימת מקורות עם קישורים בדוקים
    locations = [
        {
            "name": "תחנת החלל הבינלאומית (ISS)", 
            "lat": 0, "lon": 0, 
            "info": "שידור חי מכדור הארץ כפי שהוא נראה מהחלל!",
            "link": "https://www.youtube.com/watch?v=jPTD2gnZFUw"
        },
        {
            "name": "מצפה קק (Keck) - הוואי", 
            "lat": 19.826, "lon": -155.474, 
            "info": "מצלמות פסגת המאונה קיאה בהוואי.",
            "link": "https://www.keckobservatory.org/summit-webcams/"
        },
        {
            "name": "מצפה רמון - ישראל", 
            "lat": 30.597, "lon": 34.762, 
            "info": "אתר המצפה הרשמי ומידע על השמיים בישראל.",
            "link": "https://wise-obs.tau.ac.il/"
        },
        {
            "name": "מצפה קנרי - ספרד", 
            "lat": 28.760, "lon": -17.881, 
            "info": "שידורי מזג אוויר וחלל מהאיים הקנריים.",
            "link": "https://www.iac.es/en/observatorios-de-canarias/roque-de-los-muchachos-observatory/webcams"
        }
    ]
    
    for loc in locations:
        html = f"""
        <div style='font-family: sans-serif; text-align: right; direction: rtl; color: black; min-width: 200px;'>
            <h4 style='margin: 0 0 5px 0;'>{loc['name']}</h4>
            <p style='font-size: 13px; margin-bottom: 10px;'>{loc['info']}</p>
            <a href='{loc['link']}' target='_blank' style='
                display: block;
                text-align: center;
                padding: 10px;
                background-color: #22d3ee;
                color: black;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;'>לחצו לצפייה בשידור 🚀</a>
        </div>
        """
        folium.Marker(
            [loc["lat"], loc["lon"]], 
            popup=folium.Popup(html, max_width=250),
            tooltip=loc["name"]
        ).add_to(m)
    
    st_folium(m, width=700, height=500)

with col2:
    st.write("### הרשמה לעדכונים")
    name = st.text_input("שם")
    if st.button("שלח"):
        st.success(f"תודה {name}!")
    
    st.write("---")
    st.write("### טיפ לצפייה:")
    st.info("חלק מהמצפים מפעילים את המצלמות רק בשעות הלילה המקומיות שלהם. אם חשוך - סימן שרואים כוכבים!")

# תמונת נאס"א
st.write("---")
try:
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = res.json()
    st.image(data['url'], caption=data.get('title', 'NASA Picture of the Day'), use_container_width=True)
except:
    st.write("טוען תמונות מהחלל...")
