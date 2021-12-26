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
from PIL import Image

df = pd.read_csv('data/월세정리.csv')
df2 = pd.read_csv('data/전세정리.csv')
df3 = pd.read_csv('data/매매정리.csv')

def run_price() :
    st.subheader('Information about : 지역별 오피스텔 정보')

    selected_city = st.radio('select the place : ', ('서울', '부산', '인천' , '경기'))
    st.write(selected_city, '을 선택하셨습니다.', selected_city, '소재 오피스텔에 대한 사진과 가격 정보입니다.' )
    

    if selected_city == '서울' :
        with st.expander( "see photo, click + "):
                 
                st.image("http://lesenti.com/wp-content/uploads/2021/01/interior-main-image.jpg")              
                st.write(selected_city, """강동 오피스텔 르센티 원룸""")

        with st.expander( "price, click + "):
                data = df['2021'][3]
                data2 = df2['2021'][3]
                data3 = df3['2021'][3]
                
                st.write(selected_city, '지역 평균 월세가격은 {}천원 입니다.'.format(data))
                
                st.write(selected_city, '지역 평균 전세가격은 {}천원 입니다.'.format(data2))
                
                st.write(selected_city, '지역 평균 매매가격은 {}천원 입니다.'.format(data3)) 
        
    elif selected_city == '부산' :
         with st.expander( "see photo, click + "):
                
                st.image("photos/부산오피스텔.jpg")  
                st.write(selected_city, """해운대 오피스텔""")            

         with st.expander( "price, click + "):
                data = df['2021'][4]
                data2 = df2['2021'][4]
                data3 = df3['2021'][4]
                
                st.write(selected_city, '지역 평균 월세가격은 {}천원 입니다.'.format(data))
                
                st.write(selected_city, '지역 평균 전세가격은 {}천원 입니다.'.format(data2))
                
                st.write(selected_city, '지역 평균 매매가격은 {}천원 입니다.'.format(data3))     
                

    elif selected_city == '경기' :
        with st.expander( "see photo, click + "):
                 
                st.image("photos/경기오피스텔.jpg")              
                st.write(selected_city, """의정부월드메르디앙스마트시티""")
        with st.expander( "price, click + "):
                data = df['2021'][11]
                data2 = df2['2021'][11]
                data3 = df3['2021'][11]
                
                st.write(selected_city, '지역 평균 월세가격은 {}천원 입니다.'.format(data))
                
                st.write(selected_city, '지역 평균 전세가격은 {}천원 입니다.'.format(data2))
                
                st.write(selected_city, '지역 평균 매매가격은 {}천원 입니다.'.format(data3)) 


    else  :
        with st.expander( "see photo, click + "):
                 
                st.image("photos/인천오피스텔.jpg") 
                st.write(selected_city, """석남 브라운스톤 더 프라임 오피스텔""")             

        with st.expander( "price, click + "):
                data = df['2021'][6]
                data2 = df2['2021'][6]
                data3 = df3['2021'][6]
                
                st.write(selected_city, '지역 평균 월세가격은 {}천원 입니다.'.format(data))
                
                st.write(selected_city, '지역 평균 전세가격은 {}천원 입니다.'.format(data2))
                
                st.write(selected_city, '지역 평균 매매가격은 {}천원 입니다.'.format(data3)) 


 
           
        # selected_kind = st.multiselect('종류를 선택하세요', ('월세', '전세', '매매'))
        # st.write('You selected:', selected_kind)
    