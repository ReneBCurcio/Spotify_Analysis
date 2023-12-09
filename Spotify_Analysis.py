import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
        layout="wide",
        page_title="Spotify Songs"
)

df= pd.read_csv("01 Spotify.csv")

artist = st.sidebar.selectbox("Artista", df["Artist"].value_counts().index)

df.set_index("Track", inplace=True)

#st.line_chart(df[df["Stream"] > 10000000]["Stream"])

df_Artista = df[df["Artist"] == artist]  
album = st.sidebar.selectbox("Album", df_Artista["Album"].value_counts().index)
df_Album = df[df["Album"] == album] 


col1, col2 = st.columns(2)
col1.bar_chart(df_Album[df_Album["Stream"] > 10000000]["Stream"])
col2.line_chart(df_Album[df_Album["Stream"] > 10000000]["Danceability"])
