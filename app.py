import streamlit as st
import requests

# הגדרות דף
st.set_page_config(page_title="SkyEye - צופים ביקום", layout="wide")

# עיצוב בסיסי ללא שגיאות
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    h1 { color: #22d3ee; }
    </style>
    """, unsafe_allow_html=True)

# כותרת
st.title("🔭 SkyEye")
st.subheader("השער שלכם ושל הילדים לטלסקופים הגדולים בעולם")

# עמודות
col1, col2 = st.columns([2, 1])

with col1:
    st.info("כאן תופיע בקרוב מפת הטלסקופים האינטראקטיבית!")
    st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=800", caption="היקום מחכה לכם")

with col2:
    st.write("### הצטרפו למסע")
    name = st.text_input("שם הילד/ה")
    email = st.text_input("אימייל לעדכונים")
    if st.button("אני רוצה להירשם"):
        st.success(f"איזה כיף, {name}! נרשמת בהצלחה.")

# תמונת היום מנאס"א
st.write("---")
st.header("📸 תמונת היום מהחלל")
try:
    # שימוש ב-DEMO_KEY של נאס"א
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = res.json()
    if "url" in data:
        st.image(data['url'], use_container_width=True)
        st.write(f"**{data['title']}**")
except:
    st.write("טוען נתונים מהגלקסיה...")
