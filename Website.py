import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

img_diss = Image.open("Images/Images - Copy/diss.png")
img_me = Image.open("Images/Images - Copy/me.jpg")

st.set_page_config(page_title="My Webpage", page_icon=":fire:", layout="wide")

#sidebar menu

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options = ["Home", "Projects", "???"],
        icons=["house", "book", "arrow-through-heart"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

if selected == "Home":
    st.title(f'Hi, my name is Xiu Yang Kooi (Lucas)')

    with st.container():
        st.subheader("Hi, my name is Xiu Yang Kooi (Lucas)")
        st.image(img_me, width=400)
        st.write("---")
        st.title("A psychology graduate from the University of St Andrews")
        st.write("Aspiring researcher in cyberpsychology")
        st.write("[LinkedIn >](https://www.linkedin.com/in/xiu-yang-kooi-60473620b/)")





if selected == "Projects":
    st.title(f"My Projects")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns((2, 1))
        with left_column:
            st.header("My projects")
            st.write("##")
            st.write(
                """
                For my undergraduate dissertation, I examined how
                specific media formats (short-form video content in TikTok, long-form content in
                YouTube affected recognition memory performance in individuals. The results
                showed that contrary to popular belief that TikTok is more ‘harmful’ than other apps.
               ___

                Technical skills:

                >Administering cognitive tests (Old/New recognition, Internet Addiction Test etc)

                >Basic MATLAB programming

                >Data analysis using SPSS and Microsoft Excel (ANOVA, Post-hoc, G*Power)

                >Experimental design (within-subjects, multi-conditional)

                """

            )

        with right_column:
            st.image(img_diss)
            st.write("[PDF](https://drive.google.com/file/d/1iY9maNEi-Bt4euodX8lOxB6ipwcws6bV/view)")


if selected == "???":
    st.title(f"Uh Oh")


#for style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Images/Style/style.css")

#Intro



#What I do



#message me

with st.container():
    st.write("---")
    st.header("Contact me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/xiuyang38@gmail.com" method="POST">
        <input type= "hidden" name="_captcha" value="false"> 
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name = "message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()