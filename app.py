# -*- coding:UTF-8 -*-
import streamlit as st


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






if __name__ == '__main__':
    main()