import streamlit as st
string = "To check whether the given number is odd or even."
st.set_page_config(page_title=string)

st.title('To check whether the given number is odd or even.')
x = st.number_input('Enter a number')
if (x).is_integer():
    if x%2==0:st.write("The number is an Even number.")
    elif x%2!=0:st.write("The number is an Odd number")
else:st.write("Enter a valid integer number")
