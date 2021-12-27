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
import plotly.express as px

df = pd.read_csv('data/월세정리.csv')
df2 = pd.read_csv('data/전세정리.csv')
df3 = pd.read_csv('data/매매정리.csv')

def run_datafrme() :

    # x_values = df['지역'], y_values = df.iloc[ : , 1:4+1]
    # plt.plot(x_values, y_values)
    # st.bar_chart()

    # selected_city = st.multiselect('도시를 선택하세요', (df['지역']))
    # if len(selected_city) != 0 :

      
    #   # city = df.loc[df['지역']== selected_city , ]
    #   # st.dataframe(city)
    #   # chart_data = pd.DataFrame(city)
    #   x_values = df['지역'], y_values = df.iloc[ : , 1:4+1]
    #   plt.plot(x_values, y_values)
    #   st.bar_chart()
    st.subheader('Analysis about : 데이터프레임')
    st.write('select the rent kind : ')
    if st.button ('월세') :
        st.caption('평균가격')
        st.dataframe(df) 
        st.caption('단위 : 1000won')   
        
        
         
    if st.button ('전세') :
        st.caption('평균가격')
        st.dataframe(df2)
        st.caption('단위 : 1000won')   

    if st.button ('매매') :
        st.caption('평균가격')
        st.dataframe(df3) 
        st.caption('단위 : 1000won')   

    selected_radio = st.radio('select the city & years : ', ('월세', '전세', '매매'))
    if selected_radio == '월세' :
        selected_year = st.multiselect(' ', df.columns)
        if len(selected_year) != 0 :
            st.caption('평균가격')
            st.dataframe(df[selected_year])
            st.caption('단위 : 1000won')

    if selected_radio == '전세' :
        selected_year = st.multiselect(' ', df2.columns)
        if len(selected_year) != 0 :
            st.caption('평균가격')
            st.dataframe(df2[selected_year])
            st.caption('단위 : 1000won')

    if selected_radio == '매매' :
        selected_year = st.multiselect(' ', df3.columns)
        if len(selected_year) != 0 :
            st.caption('평균가격')
            st.dataframe(df3[selected_year])
            st.caption('단위 : 1000won')


    

    


    

    

    # 셀렉트박스로 장로 선택
    # selected_city = st.selectbox('지역을 선택하세요', (df4['지역']))
    # chart_data = pd.DataFrame(
    #     np.random.randn(50, 1),
    #     columns=[selected_city])

    # st.bar_chart(chart_data)

    # fig = px.bar(df4, x = df4['2020상월세'], y = df4['지역'])
    # st.plotly_chart(fig)

