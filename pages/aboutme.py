import streamlit as st

st.title("Facts about Mariane G. Tumbagahan 📚 ")



st.title("Profile Gallery 👸")


image_paths = ["./picture/m2.jpg", "./picture/m1.jpg", "./picture/m3.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 TUMBAGAHAN, MARIANE G.")

# st.markdown("""
# ##### 👨‍👦‍👦 Family Members

# * 🤱 **Mother's Name:** Ma. Grace G. Tumbagahan
# * 👨 **Father's Name:** Mariano G. Tumbagahan Jr.
# * 👧 **Sister's Name:** Marnie Tumbagahan
# * 👦 **Brothers' Names:** Kenneth, Marjun, Carlo, Bengie
# ### 🔎 Overview
# """, unsafe_allow_html=True)

# Personal Information
st.header("✨ Personal Information ✨")
st.write("**Name:** MARIANE G. TUMBAGAHAN 💁‍♀️")
st.write("**Date of Birth:** November 23, 2002 🎂")
st.write("**Age:** 21 years old 🌸")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY 🎓")
st.write("**Program:** Bachelor of Science in Information Systems 💻")
st.write("**Year:** 3rd year 📚")
st.write("**Location:** Villa Hergon, Brgy. Rizal, Silay City, Negros Occidental 🏡")


with st.expander("My Vision for the Future: A 10-Year Forecast"):
    st.markdown("""
    
    #
    ### ✨ Ten Years From Now: A Journey of Resilience and Success ✨
    
            In the year 2034, I see myself as a strong and successful person who has overcome many challenges. My journey from a curious student to a successful professional will be marked by personal growth, determination, and a desire for excellence. This narrative explores my goals, milestones, and envisioned achievements in the field of information science ten years from now.

    #### 🌟 Personal Growth and Vision 🌟

           My path to becoming an accomplished information professional will involve continuous learning, resilience, and an unwavering spirit. Despite the profound loss of my beloved parents, I will turn my grief into motivation, determined to honor their memory through my achievements. Together with my siblings, we will build a future filled with hope, strength, and unity.

           In 2034, I will be proof of the power of education, perseverance, and a forward-thinking vision. My career will combine research excellence, teaching, industry leadership, and making a positive impact on society. Reflecting on my journey from an eager student to a leading professional, I will be proud of my contributions to the field and the legacy I am building.

    #### 🌏 Dreams and Aspirations 🌏

             Ten years from now, I see myself as not only a successful person but also a world traveler. My success will show that it is possible to overcome challenges and succeed. I will have broken free from poverty, using my achievements to help my family and community.

             My story will be one of continuous learning, creative thinking, and a strong commitment to making a difference in the world. I will carry with me the spirit of my parents and the dreams of my siblings, all of us united in our quest for a better life.

             In conclusion, my journey over the next decade will demonstrate resilience, ambition, and the limitless potential within each of us. I will emerge as a leader, educator, and visionary, dedicated to advancing the field of information science and using data to benefit society. My life will be a celebration of success, travel, and triumph over adversity.
    """, unsafe_allow_html=True)
# Quotes
st.header("Quotes for LIFE")
st.write(" *\"Every day is a new opportunity to learn and grow.\"* - Oprah Winfrey")
st.write(" *\"Embrace the challenges, for they are the stepping stones to success.\"* - Malala Yousafzai")
st.write(" *\"Dream big, work hard, stay focused, and surround yourself with good people.\"* - Michelle Obama")
st.write(" *\"In a world where you can be anything, be yourself.\"* - Beyoncé")



import streamlit as st


images = [
    {"path": "./picture/us1.jpg", "caption": "MY ACADEMIC JOURNEY!!!"},
    {"path": "./picture/us2.jpg", "caption": "IT HELPS ME GROW AND KEEP FIGHTING IN LIFE."},
    {"path": "./picture/us3.jpg", "caption": "the support of my classmates has been an indispensable aspect of my academic journey."}
]


st.title("🖼️Gallery")


for image in images:
    st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: black; /* Light grey background */
        padding: 2em;
        font-family: "Arial", sans-serif; /* Elegant font */
    }
    h1, h2 {
        color: #ff69b4; /* Pinkish color for headings */
    }
    .stText {
        font-size: 1.2em;
        color: #333; /* Dark text color */
    }
</style>

    """,
    unsafe_allow_html=True
)


st.write("### Thank you for visiting my profile!")
