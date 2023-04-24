# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd

def main():
    #title
    st.title("Hi")

    #text
    st.text("This is so good")

    #Header
    st.header("This is Header")

    #Subheader
    st.subheader("This is subheader")

    #Markdown
    st.markdown("## this is Markdown")

    # 색상이 들어간 텍스트 feature
    st.success("성공")
    st.warning("경고")
    st.info("정보와 관련된 탭")
    st.exception("예외 처리")

    #st.write()
    st.write("일반 텍스트")
    st.write(1+2)
    st.write(dir(str))

    st.title(":sunglasses:")

    #help
    st.help(range)

    #데이터 불러오기
    iris = pd.read_csv('data/iris.csv')

    st.title("IRIS 테이블")
    st.dataframe(iris, 500, 100)  # Height, Width

    st.title("table()")
    st.table(iris)

    st.title("write()")
    st.write(iris)







if __name__ == '__main__':
    main()