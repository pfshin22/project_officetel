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

def run_chart() :  
    
    
    df_r = df['지역']
    df_year = df.iloc[ : , 1 :  ]
  
    st.subheader('Analysis about : 지역별 오피스텔 가격')

    # fig = px.bar(df['2018'], x = df['지역'] , y='2018', title="2018 monthly rent for city")
    # st.plotly_chart(fig)
    

    selected_year = st.selectbox('select the year :', df_year.columns)
    st.caption('단위 : 1000won')
    
    if selected_year == '2018' :
        selected_radio = st.radio('select the kind of graph', ('bar', 'aria', 'line'))    
        if selected_radio == 'bar' :
            
            fig = px.bar(df, x = df['지역'] , y='2018', title="2018년 월세가격")
            st.plotly_chart(fig)

            fig = px.bar(df2, x = df2['지역'] , y='2018', title="2018년 전세가격")
            st.plotly_chart(fig)

            fig = px.bar(df3, x = df3['지역'] , y='2018', title="2018년 매매가격")
            st.plotly_chart(fig)


        elif selected_radio == 'aria' :
            
            st.area_chart(df['2018'])
            st.area_chart(df2['2018'])
            st.area_chart(df3['2018'])

        elif selected_radio == 'line' :
            
            fig = px.line(df, x = df['지역'] , y='2018', title="2018년 월세가격")
            st.plotly_chart(fig)

            fig = px.line(df2, x = df2['지역'] , y='2018', title="2018년 전세가격")
            st.plotly_chart(fig)

            fig = px.line(df3, x = df3['지역'] , y='2018', title="2018년 매매가격")
            st.plotly_chart(fig)

    elif selected_year == '2019' :
        selected_radio = st.radio('select the kind of graph', ('bar', 'aria', 'line'))    
        if selected_radio == 'bar' :
            
            fig = px.bar(df, x = df['지역'] , y='2019', title="2019년 월세가격")
            st.plotly_chart(fig)
            
            fig = px.bar(df2, x = df2['지역'] , y='2018', title="2019년 전세가격")
            st.plotly_chart(fig)

            fig = px.bar(df3, x = df3['지역'] , y='2018', title="2019년 매매가격")
            st.plotly_chart(fig)

        elif selected_radio == 'aria' :
            
            st.area_chart(df['2019'])
            st.area_chart(df2['2019'])
            st.area_chart(df3['2019'])

        elif selected_radio == 'line' :
            
            fig = px.line(df, x = df['지역'] , y='2019', title="2019년 월세가격")
            st.plotly_chart(fig)
           
            fig = px.line(df2, x = df2['지역'] , y='2018', title="2019년 전세가격")
            st.plotly_chart(fig)
           
            fig = px.line(df3, x = df3['지역'] , y='2018', title="2019년 매매가격")
            st.plotly_chart(fig)
               
    elif selected_year == '2020' :
        selected_radio = st.radio('select the kind of graph', ('bar', 'aria', 'line'))    
        if selected_radio == 'bar' :
            
            fig = px.bar(df, x = df['지역'] , y='2020', title="2020년 월세가격")
            st.plotly_chart(fig)
            
            fig = px.bar(df2, x = df2['지역'] , y='2018', title="2020년 전세가격")
            st.plotly_chart(fig)

            fig = px.bar(df3, x = df3['지역'] , y='2018', title="2020년 매매가격")
            st.plotly_chart(fig)

        elif selected_radio == 'aria' :
            
            st.area_chart(df['2020'])
            st.area_chart(df2['2020'])
            st.area_chart(df3['2020'])

        elif selected_radio == 'line' :
            
            fig = px.line(df, x = df['지역'] , y='2018', title="2020년 월세가격")
            st.plotly_chart(fig)
            
            fig = px.line(df2, x = df2['지역'] , y='2018', title="2020년 전세가격")
            st.plotly_chart(fig)

            fig = px.line(df3, x = df3['지역'] , y='2018', title="2020년 매매가격")
            st.plotly_chart(fig)
    
    elif selected_year == '2021' :
        selected_radio = st.radio('select the kind of graph', ('bar', 'aria', 'line'))    
        if selected_radio == 'bar' :
            
            fig = px.bar(df, x = df['지역'] , y='2021', title="2021년 월세가격")
            st.plotly_chart(fig)
            
            fig = px.bar(df2, x = df2['지역'] , y='2018', title="2021년 전세가격")
            st.plotly_chart(fig)

            fig = px.bar(df3, x = df3['지역'] , y='2018', title="2021년 매매가격")
            st.plotly_chart(fig)

        elif selected_radio == 'aria' :
            
            st.area_chart(df['2021'])
            st.area_chart(df2['2021'])
            st.area_chart(df3['2021'])

        elif selected_radio == 'line' :
            
            fig = px.line(df, x = df['지역'] , y='2018', title="2021년 월세가격")
            st.plotly_chart(fig)
            
            fig = px.line(df2, x = df2['지역'] , y='2018', title="2021년 전세가격")
            st.plotly_chart(fig)
            
            fig = px.line(df3, x = df3['지역'] , y='2018', title="2021년 매매가격")
            st.plotly_chart(fig)


    # st.radio('select the kind of graph', ('지역별', '전국'))  
    
    

    



   
    # selected_city = st.selectbox('select the city :', df['지역'])
    # if selected_city == '전국' :
    #     st.line_chart(df['지역']== '전국')
        
    #     selected_radio = st.radio('select the kind of graph', ('line', 'aria', 'bar'))    
    #     if selected_radio == 'line' :
            
    #         st.line_chart(df['지역']== '전국')

    #     elif selected_radio == 'aria' :
            
    #         st.area_chart(df['지역']== '전국')

    #     elif selected_radio == 'bar' :
            
    #         st.bar_chart(df['지역']== '전국')



   
    
    # selected_chart = st.radio('select the kind of graph :', ('라인차트', '아리아차트', '바차트'))
    # if len(selected_year) > 0 :
    #     st.dataframe(df_year[selected_year])

    #     # 상관계수를 수치로도 구하고, 차트로도 표시하라.
    #   # fig1 = sns.pairplot(data = df_corr[selected_corr])
    #   # st.pyplot(fig1)

    # elected_radio = st.radio('그래프를 선택하세요', ('라인차트', '아리아차트', '바차트'))    
    # if selected_radio == '라인차트' :
    #     chart_data = pd.DataFrame(df[selected_corr])

    #     st.line_chart(chart_data)

    # elif selected_radio == '아리아차트' :
    #     chart_data = pd.DataFrame(df[selected_corr])

    #     st.area_chart(chart_data)

    # elif selected_radio == '바차트' :
    #     chart_data = pd.DataFrame(df[selected_corr])

    #     st.bar_chart(chart_data)
    # # 유저가 컬럼을 선택하지 않은 경우 

    # else : 
    #     st.write('선택한 컬럼이 없습니다.')
        
    # col1, col2 = st.columns([3, 1])
    # data = df['2021']

    # col1.subheader("A wide column with a chart")
    # x_values = df['지역']
    # y_values = df['2021']
    # st.plot(x_values, y_values)	
    # col1.line_chart(data)

    # col2.subheader("A narrow column with the data")
    # col2.write(df)

    
    

    # 셀렉트박스로 장로 선택
    # selected_city = st.selectbox('지역을 선택하세요', (df4['지역']))
    # chart_data = pd.DataFrame(
    #     np.random.randn(50, 1),
    #     columns=[selected_city])

    # st.bar_chart(chart_data)

    # fig = px.bar(df4, x = df4['2020상월세'], y = df4['지역'])
    # st.plotly_chart(fig)
