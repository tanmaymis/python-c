#to run this 

import streamlit as st

st.title("streamlit demo")
st.header("streamlit is awsome")
st.subheader("it is easy to use")
st.text("this is the simple text example")
st.write("this is a magical function")
st.markdown("this is a **markdown** example")
st.success("this is a success message")
st.info("this is a info message")
st.warning("this is a warning message")
st.error("this is a error message")
st.exception("this is an exception message")

#media function
st.image("ui/images1.jpg")
st.video("https://youtu.be/BORILx1ccBk")
st.audio("ui/sound1.wav")

#widget

name = st.text_input("enter the username")
cost = st.number_input("enter the cost")
comment = st.text_area("enter the remark")
status = st.checkbox("save this data")
gender =st.radio("gender" ,["male","female","other"])

querylist =["how ot use streamlit",
            'is streamlit free or paid',
            'is it gonna rain now?']
query = st.selectbox("what the query",querylist)
rating = st.slider("select the rating" ,1 ,5)
btn = st.button("submit the response")

#if btn is pressed

if btn:
    st.write("Username",name)
    st.write("cost",cost)
    st.write("comment",comment)
    st.write("Status",status)
    st.write("gender",gender)
    st.write("query" ,query)
    st.write("rating",rating)