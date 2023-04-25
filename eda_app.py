# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv("data/iris.csv")
    st.markdown("## IRIS 데이터 확인\n")
    st.write(iris)

    submenu = st.sidebar.selectbox("하위메뉴", ["기술 통계량", "그래프 분석", "통계 분석"])
    if submenu == "기술 통계량":
        st.dataframe(iris)

        with st.expander("데이터 타입"):
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander("기술 통계량"):
            result2 = pd.DataFrame(iris.dtypes)
            st.write(result2)
        with st.expander("타겟 빈도수 확인"):
            st.write(iris["species"].value_counts())

    elif submenu == "그래프 분석":
        st.title("Title")
        with st.expander("산점도"):
            fig1 = px.scatter(iris,
                             x = "sepal_width",
                             y = "sepal_length",
                             color="species",
                             size = "petal_width",
                             hover_data=["petal_length"])
            st.plotly_chart(fig1)

        #layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title("seaborn")
            fig, ax = plt.subplots()
            sns.histplot(data=iris, x="sepal_length", color="red")
            st.pyplot(fig)

        with col2:
            st.title("Matplotlib")
            fig, ax = plt.subplots()
            ax.hist(iris["sepal_length"], color="blue")
            st.pyplot(fig)

        tab1, tab2 = st.tabs(["탭1", "탭2"])
        with tab1:
            st.write("탭1")
            species = st.selectbox("종 선택", iris["species"].unique())
            filtered_iris = iris[iris["species"] == species]
            fig2 = px.scatter(filtered_iris,
                              x="sepal_width",
                              y="sepal_length",
                              color="species",
                              size="petal_width",
                              hover_data=["petal_length"])
            st.plotly_chart(fig2)
            #종 선택할 때마다
            #산점도 그래프가 달라지도록 함
            #plotly 그래프로 구현
        with tab2:
            st.write("탭2")
            #캐글 데이터 / 공모전 데이터
            #해당 데이터 그래프 1개만
    elif submenu == "통계 분석":
        pass
    else:
        st.warning("뭔가 없어요")
