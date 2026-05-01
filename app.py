import streamlit as st
import requests

# הגדרות דף - נותן תחושה של אפליקציה מקצועית
st.set_page_config(page_title="SkyEye - צופים ביקום", layout="wide")

# עיצוב אישי קצר כדי שהאתר יראה "חללי"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    stButton>button { width: 100%; border-radius: 20px; background-color: #22d3ee; color: black; }
    </style>
    """, unsafe_allow_status=True)

# כותרת האתר
st.title("🔭 SkyEye")
st.subheader("השער שלכם ושל הילדים לטלסקופים הגדולים בעולם")

# חלוקה לעמודות - מפה ורישום
col1, col2 = st.columns([2, 1])

with col1:
    st.info("כאן תופיע בקרוב מפת הטלסקופים האינטראקטיבית שלנו!")
    # כאן נכניס את המפה בשלב הבא
    st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&q=80&w=1000", caption="היקום מחכה לכם")

with col2:
    st.write("### הצטרפו למסע")
    with st.form("registration"):
        name = st.text_input("שם הילד/ה")
        parent_email = st.text_input("אימייל של אבא או אמא")
        submit = st.form_submit_button("שלחו לי עדכונים על מטר מטאורים!")
        if submit:
            st.success(f"ברוכים הבאים למסע, {name}!")

# תמונת היום מנאס"א
st.write("---")
st.header("📸 צילום חי מהחלל")
try:
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
    data = response.json()
    st.image(data['url'], width=700)
    st.write(f"**{data['title']}**")
except:
    st.write("טוען נתונים מנאס''א...")

