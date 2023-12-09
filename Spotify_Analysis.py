import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
        layout="wide",
        page_title="Spotify Songs"
)

df= pd.read_csv("01 Spotify.csv")

artist = st.selectbox("Artista", df["Artist"].value_counts().index)

df.set_index("Track", inplace=True)

#st.line_chart(df[df["Stream"] > 10000000]["Stream"])

df_Artista = df[df["Artist"] == artist]  
album = st.selectbox("Album", df_Artista["Album"].value_counts().index)
df_Album = df[df["Album"] == album] 
st.bar_chart(df_Album[df_Album["Stream"] > 10000000]["Stream"])