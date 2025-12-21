import streamlit as st

#Displaying and playing a video file with audio via streamlits
video_file = open("MONGO_Test_endpoint.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)