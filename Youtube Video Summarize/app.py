import streamlit as st
from dotenv load_dotenv
load_dotenv()

import google.generative as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
prompt="""please summarize this video
transcript into 250 words or less, highlighting key points"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t["text"] for t in transcript_text])
        return transcript
    except Exception as e:
        raise e

# Function to generate a summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text 

# Button to fetch and display the detailed notes
