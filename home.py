import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/aboutme.py", "ABOUT MARIANE", "1️⃣", in_section=True),
        Page("pages/discription.py", "APP DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/learnings.py", "WHAT I HAVE LEARN?", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/predict.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),


         Section("SOURCE CODE", "💾"),
        Page("pages/predict_src.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image_src.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 FINAL PROJECT IN ITEQMT:")
st.header("TUMBAGAHAN, MARIANE G. - BSIS 3B")

st.image("./picture/g1.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/koalatech/streamlit_web_app)")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("QUANTITATIVE METHOD"):
    st.markdown("""
    
    <a href=""><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

        HISTORY, PURPOSE AND USAGE
       The quantitative method, rooted in the early 20th century, evolved from the need for empirical, statistical analysis in research, particularly in fields like psychology, sociology, and economics. Its primary purpose is to quantify data and generalize results from a sample to the population of interest, providing a means to measure and analyze variables systematically. This method employs tools such as surveys, experiments, and statistical models to test hypotheses and make predictions. Widely used in both academic research and industry, it facilitates objective and replicable findings that inform policy, business strategies, and scientific advancements.



    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Quantitative Method





##### 👨‍🔧 More Content

   PURPOSE AND USAGE
        The quantitative method in education emerged in the mid-20th century as a way to apply statistical analysis to educational research, aiming to improve educational practices and outcomes. It focuses on measuring variables such as student achievement, teacher effectiveness, and educational equity through standardized tests, surveys, and longitudinal studies. By employing statistical techniques, researchers can identify trends, compare groups, and establish causal relationships. The purpose is to provide objective, data-driven insights that can inform policy decisions, curriculum development, and teaching strategies. This method is essential for evaluating the efficacy of educational interventions and programs. Its widespread use ensures that educational practices are based on empirical evidence, promoting continuous improvement in the field.
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./p1.jpg")


st.markdown("""
            
* Benefits of Quantitative Methods in Contemporary Research
    Quantitative methods have become increasingly vital in modern research across various fields, including education, social sciences, healthcare, and business. Here are some key benefits that highlight their importance today:

* Objective and Reliable Data
    Quantitative methods provide objective data that can be measured and analyzed statistically. This objectivity reduces biases and allows for more reliable and valid results, ensuring that findings are based on concrete evidence rather than subjective interpretation.

* Generalization of Results
    By using large sample sizes and rigorous sampling techniques, quantitative research allows for the generalization of results to larger populations. This ability to generalize enhances the applicability of research findings, making them more useful for policymakers, educators, and practitioners.

* Precision and Accuracy
    Quantitative methods use precise measurements and statistical tools to analyze data. This precision leads to accurate results that can be replicated in subsequent studies, reinforcing the credibility and trustworthiness of the research.

* Identification of Patterns and Trends
    Through the use of statistical analysis, quantitative methods can identify patterns and trends within data. This capability is crucial for making informed decisions, predicting future outcomes, and understanding complex phenomena across various domains.

* Enhanced Decision Making
    Data-driven insights provided by quantitative research support evidence-based decision making. In fields like education, healthcare, and business, such insights are essential for developing effective strategies, policies, and interventions that address specific needs and challenges.

* Efficiency in Data Analysis
    Quantitative research often involves the use of sophisticated software and analytical tools, making the data analysis process more efficient





### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
