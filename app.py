import streamlit as st
from  streamlit_option_menu import option_menu
from streamlit_extras.stateful_button import button
from pytube import YouTube

select = option_menu(
    menu_title=None,
    options=["Yt video Download","Video to Audio","About"],
    default_index=0,
    orientation='horizontal'
        )
def center_button():
    st.markdown("""
<style>
.stButton {
  text-align: center;
}
</style>
""", unsafe_allow_html=True)

def high():
    yt = YouTube(url)
    stream = yt.streams.filter(resolution="720p").first()
    st.markdown(f'<a href = "{stream.url}">download</a>',unsafe_allow_html=True)

def low():
    yt = YouTube(url)
    stream = yt.streams.filter(resolution="144p").first()
    st.markdown(f'<a href = "{stream.url}">download</a>',unsafe_allow_html=True)

def medium():
    yt = YouTube(url)
    stream = yt.streams.filter(resolution="360p").first()
    st.markdown(f'<a href = "{stream.url}">download</a>',unsafe_allow_html=True)


        



def title():
    yt = YouTube(url)
    st.write(yt.title)
    st.image(yt.thumbnail_url,width=250)
    

try:
    if select == "Yt video Download":
       st.header("YT Video Downloader")
       center_button()
       url = st.text_input("Enter Video Url Here:")
       if button("Download", key="Download"):
            title()
            with st.expander("Select Resolution",):
                if button("High Quality",key="High"):
                    high()
                if button("Medium Quality ", key="medium"):
                    medium()
                if button("Low Quality",key="Low"):
                    low()



except Exception as e:
    st.warning("Enter Valid Link")

if select =='Video to Audio':
    st.header("Yt video to Audio Downloader")
    try:
        center_button()
        url = st.text_input("Enter Url Here:")
        if button('Convert',key='Convert'):
            yt = YouTube(url)
            title()
            stream = yt.streams.filter(only_audio=True, abr="128kbps").first()
            st.markdown(f'<a href = "{stream.url}">download audio 128Kbps</a>',unsafe_allow_html=True)

    except Exception as e:
        st.warning("Enter Valid link")
        if button("Check Error",key="error"):
            st.write(e)


