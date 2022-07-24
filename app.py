import streamlit as st
string = "To check whether the given number is odd or even."
st.set_page_config(page_title=string, page_icon="🔍")

st.title('To check whether the given number is odd or even.')
x = st.number_input('Enter a number')
if (x).is_integer():
    if x%2==0:st.write("Even number.")
    elif x%2!=0:st.write("Odd number")
else:st.write("Enter valid integer")
