import streamlit as st

st.title("Shawaiz Crashout")

audio_file = "shawaiz.ogg"  # Replace with your file name
try:
    # Open and read the audio file
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
    
    # Display the audio player
    st.audio(audio_bytes, format="audio/ogg")
    
    # Optional: Check file size to confirm it's loaded
    st.write(f"✅ Audio file size: {len(audio_bytes)} bytes")

except FileNotFoundError:
    st.error(f"❌ Audio file not found: {audio_file}")
    st.write("Please ensure the file is in the same directory as this script.")