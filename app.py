from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import joblib
import streamlit as st
import time
import numpy as np
import altair as alt
from vega_datasets import data
from chart import run_chart
from dataframe import run_datafrme

from price import run_price

df = pd.read_csv('data/월세정리.csv')
df2 = pd.read_csv('data/전세정리.csv')
df3 = pd.read_csv('data/매매정리.csv')


def main() :
    menu = ['Home', 'Officetel information', 'Data analysis', 'Chart analysis']

    choice = st.sidebar.selectbox('Choose a menu', menu)

    if choice == 'Home' :
        st.subheader('The Web-site about Officentel')
       
        st.write('the Officentel video in South-Korea : ')
        video_file = open('video/오피스텔.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)
        st.write('<ㅡ Please choose a left menu')
        st.caption('데이터출처 : 한국부동산원')
   
    elif choice == 'Officetel information' :
        run_price()

    elif choice == 'Data analysis' :
        run_datafrme()

    elif choice == 'Chart analysis' :
        run_chart()


   

if __name__ == '__main__' :
    main()