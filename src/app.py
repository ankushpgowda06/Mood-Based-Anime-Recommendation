import streamlit as st
import requests
from backend import age_filter
import re

st.set_page_config(layout="wide")

mood_mapping = {
    "Nostalgic, Weird Humor": 0,
    "Emotional Rollercoaster": 1,
    "Curiosity, Suspense, Deep": 2,
    "Cool Characters with Edge": 3,
    "Adventurous, Unconventional Plots": 4,
    "Dark, Serious, Intense": 5,
    "Optimistic, Motivational": 6,
}

col1, col2, col3, col4 = st.columns([1, 1, 6, 1])  
with col3:  
    st.title("Mood Based Anime Recommendation System")
    st.markdown(" ")

col1, col2, col3 = st.columns([1, 1, 1])  
with col2:  
    with st.form("narrow_form"):
        age = st.number_input("**Age:**", min_value=5, max_value=100, step=1)
        format_options = ["TV", "Movie", "OVA", "ONA", "Special", "Music"]
        format_selection = st.segmented_control(
            "**Type:**", format_options, selection_mode="multi"
        )
        mood_options = [
            "Nostalgic, Weird Humor", "Emotional Rollercoaster", "Curiosity, Suspense, Deep", "Cool Characters with Edge",
            "Adventurous, Unconventional Plots", "Dark, Serious, Intense", "Optimistic, Motivational"
        ]
        mood_selection = st.segmented_control(
            "**Mood:**", mood_options, selection_mode="single"
        )
        submitted = st.form_submit_button("Recommend", type="primary")

st.header("Recommendation: ")
if submitted:
    df = age_filter(age)
    df = df[df["Type"].isin(format_selection)]
    df = df[df["Cluster"] == mood_mapping[f"{mood_selection}"]]
    df = df.sort_values(by=['Popularity', 'Final_Score'], ascending=[True, False]).head(5)
    if len(df) > 5:
        limit = 5
    else:
        limit = len(df)
    col = st.columns(limit, border=True)   
    for i in range(limit): 
        url = f'https://api.jikan.moe/v4/anime/{int(df.iloc[i]["MAL_ID"])}'
        response = requests.get(url)
        data = response.json()
        with col[i]:
            st.image(f"{data['data']['images']['jpg']['image_url']}", use_container_width=True)
            st.markdown(f"**Anime:** {data['data']['title']}")
            match = re.search(r"\b\d{4}\b", data['data']['aired']['string'])
            st.markdown(f"**Aired:** {match.group()}")
            st.markdown(f"**Trailer:** {data['data']['trailer']["embed_url"]}")
            st.markdown(f"**Type:** {df.iloc[i]["Type"]}")
            st.markdown(f"**Episodes:** {data['data']['episodes']}")
            st.markdown(f"**Duration:** {data['data']['duration']}")
            st.markdown(f"**Rank:** {data['data']['rank']}")

