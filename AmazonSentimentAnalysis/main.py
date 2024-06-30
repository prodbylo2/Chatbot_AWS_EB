from get import GetData
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

def sentiment(data):
    sia = SentimentIntensityAnalyzer()
    data.reset_index(inplace=True)
    res = {}
    for i, row in tqdm(data.iterrows(), total=len(data)):
        text = row['body']
        myid = row['index']
        res[myid] = sia.polarity_scores(text)
    
    result = pd.DataFrame(res).T
    result.reset_index(inplace=True)
    result = result.merge(data, how='left')
    
    negative = result['neg'].sum()
    positive = result['pos'].sum()
    neutral = result['neu'].sum()
    
    return negative, positive, neutral

url = st.text_input('Enter some text')
if url:
    if st.button('Should I get this?'):
        obj = GetData(url)
        data = obj.get_info()
        neg, pos, neu = sentiment(data)
        
        st.header("Analysis")
        
        image1 = Image.open("negative-face.png")
        image2 = Image.open("neutral-face.png")
        image3 = Image.open("positive-face.png")
        
        text1 = f"{neg}% of reviews suggest you DON'T purchase this product."
        text2 = f"{neu}% of reviews are neutral."
        text3 = f"{pos}% of reviews suggest you DO purchase this product."
        
        
        # Create three columns
        col1, col2, col3 = st.columns(3)

        # Display the first image and text in the first column
        with col1:
            st.image(image1, caption=text1, use_column_width=True)
           

        # Display the second image and text in the second column
        with col2:
            st.image(image2, caption=text2, use_column_width=True)
            

        # Display the third image and text in the third column
        with col3:
            st.image(image3, caption=text3, use_column_width=True)
            
        
    