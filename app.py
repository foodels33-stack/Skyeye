import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

# הגדרות דף - כותרת האתר שמופיעה בלשונית
st.set_page_config(page_title="SkyEye - צופים ביקום", layout="wide")

# עיצוב דף - צבע רקע כהה וטקסט בצבע תכלת (עיצוב חללי)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1, h2, h3 { color: #22d3ee; text-align: right; }
    div.stButton > button:first-child { background-color: #22d3ee; color: black; }
    p { text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# כותרות האתר
st.title("🔭 SkyEye")
st.subheader("השער שלכם ושל הילדים לטלסקופים הגדולים בעולם")

# חלוקה לעמודות: עמודה רחבה למפה ועמודה צרה לרישום
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### מפת הטלסקופים העולמית")
    st.write("לחצו על הסיכות במפה כדי לצפות בשידורים חיים מהמצפים")
    
    # יצירת מפת העולם עם רקע כהה
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
    
    # רשימת המצפים כולל קישורים למצלמות ומידע
    locations = [
        {
            "name": "מצפה רמון - ישראל", 
            "lat": 30.597, "lon": 34.762, 
            "info": "המצפה הגדול בישראל! כאן חוקרים את השמיים שלנו.",
            "link": "https://wise-obs.tau.ac.il/"
        },
        {
            "name": "מצפה קק (Keck) - הוואי", 
            "lat": 19.826, "lon": -155.474, 
            "info": "צפו במצלמות מזג האוויר מהפסגה הכי גבוהה בהוואי.",
            "link": "https://www.keckobservatory.org/summit-webcams/"
        },
        {
            "name": "מצפה צ'ילה (VLT)", 
            "lat": -24.627, "lon": -70.404, 
            "info": "כאן נמצאים הטלסקופים הכי חזקים בעולם.",
            "link": "https://www.eso.org/public/images/archive/category/webcams/"
        },
        {
            "name": "מצפה קנרי - ספרד", 
            "lat": 28.760, "lon": -17.881, 
            "info": "צפו בעננים ובכוכבים מעל האיים הקנריים.",
            "link": "https://www.iac.es/en/observatorios-de-canarias/roque-de-los-muchachos-observatory/webcams"
        }
    ]
    
    # הוספת הסיכות למפה עם עיצוב של כפתור בתוך הבלון
    for loc in locations:
        html = f"""
        <div style='font-family: sans-serif; text-align: right; direction: rtl; color: black;'>
            <h4 style='margin-bottom:5px;'>{loc['name']}</h4>
            <p style='font-size: 14px;'>{loc['info']}</p>
            <a href='{loc['link']}' target='_blank' style='
                display: inline-block;
                padding: 8px 12px;
                background-color: #22d3ee;
                color: black;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;'>לצפייה בשידור חי 🔭</a>
        </div>
        """
        folium.Marker(
            [loc["lat"], loc["lon"]], 
            popup=folium.Popup(html, max_width=250),
            tooltip=loc["name"]
        ).add_to(m)
    
    # הצגת המפה באתר
    st_folium(m, width=800, height=500)

with col2:
    st.write("### הצטרפו למסע")
    st.write("קבלו התראות על אירועים מיוחדים בחלל (ליקוי חמה, מטר מטאורים ועוד)")
    name = st.text_input("שם הילד/ה")
    email = st.text_input("אימייל של ההורים")
    
    if st.button("אני רוצה להירשם!"):
        if name and email:
            st.success(f"איזה כיף שאתה איתנו, {name}! ניצור קשר בקרוב.")
        else:
            st.warning("אנא מלאו שם ואימייל")

# חלק תחתון - תמונת היום של נאס"א
st.write("---")
st.header("📸 תמונת היום מהחלל (NASA)")
st.write("התמונה מתעדכנת בכל יום ישירות מהלוויינים של נאס''א")

try:
    # שליפת נתונים מ-NASA API
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = res.json()
    if "url" in data:
        st.image(data['url'], caption=data.get('title', 'NASA APOD'), use_container_width=True)
        with st.expander("קראו עוד על התמונה (באנגלית)"):
            st.write(data.get('explanation', 'אין הסבר זמין כרגע.'))
except:
    st.write("טוען נתונים מהגלקסיה... (נסו לרענן את הדף)")

st.write("---")
st.write("© 2026 SkyEye - כל הזכויות שמורות")
