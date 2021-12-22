import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import joblib
df = pd.read_csv('data/월세집값.csv')
st.dataframe(df)



# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
    
    
chart_data = pd.DataFrame(df[['2018상평월보', '2018하평월보' ,'2019상평월보', '2019하평월보', '2020상평월보' ]])

# df.columns()


    
st.line_chart(chart_data)

# from eda_app import run_eda_app
# from ml_app import run_ml_app

def main() :
    pass



    # menu = ['홈', '데이터분석', '신체능력평가하기']

    # choice = st.sidebar.selectbox('메뉴 선택', menu)

    # if choice == '홈' :
    #     st.subheader('당신의 신체능력을 평가합니다.')
    #     st.write('A= 최상, B= 상, C= 중간, D= 하')
    #     st.write('왼쪽의 사이드바에서 "평가하기"를 선택하여 평가하세요')
    
    # elif choice == '데이터분석' :
    #     run_eda_app()

    # elif choice == '신체능력평가하기' :
    #     run_ml_app()


if __name__ == '__main__' :
    main()